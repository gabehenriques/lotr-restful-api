The Lord of the Things RESTful API
==================================

This project provides a restful interface to search and access data from the novel `The Lord of the Rings`_.

Installing with Docker
----------------------

Download and install project dependencies

.. code-block:: text

    docker-compose up --build

You can specify the ``-d`` switch to start in detached mode. This will bind port ``80`` and ``443``. Unfortunately, unlike the docker command, there is no command line arguments to specify ports. If you want to change them, edit the ``docker-compose.yml`` file.

After that, start the migration process

.. code-block:: text

    docker-compose exec web python manage.py migrate

Database Seeding
----------------

Use the ``build_all()`` method using the django shell to populate the database

.. code-block:: text

    docker-compose exec web python manage.py shell

.. code-block:: python

    from data.build import build_all
    build_all()


Browse ``localhost/api/v2/``

.. _`The Lord of the Rings`: https://en.wikipedia.org/wiki/The_Lord_of_the_Rings
