import re
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import *
from .serializers import *


class ListOrDetailSerialRelation:
    """
    Mixin to allow association with separate serializers
    for list or detail view.
    """

    list_serializer_class = None

    def get_serializer_class(self):
        if self.action == "list" and self.list_serializer_class is not None:
            return self.list_serializer_class
        return self.serializer_class


class NameOrIdRetrieval:
    """
    Mixin to allow retrieval of resources by
    pk (in this case ID) or by name
    """

    idPattern = re.compile(r"^-?[0-9]+$")
    namePattern = re.compile(r"^[0-9A-Za-z\-\+]+$")

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        lookup = self.kwargs["pk"]

        print('lookup', lookup)

        if self.idPattern.match(lookup):
            resp = get_object_or_404(queryset, pk=lookup)

        elif self.namePattern.match(lookup):
            resp = get_object_or_404(queryset, name=lookup)

        else:
            raise Http404

        return resp


class LotrApiCommonViewset(
    ListOrDetailSerialRelation, NameOrIdRetrieval, viewsets.ReadOnlyModelViewSet
):
    pass


class CharacterResource(LotrApiCommonViewset):
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    list_serializer_class = CharacterSummarySerializer


class RaceResource(LotrApiCommonViewset):
    queryset = Race.objects.all()
    serializer_class = RaceDetailSerializer
    list_serializer_class = RaceSummarySerializer
