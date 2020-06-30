The Lord of the Rings RESTful API
==================================

**Note:** This project is under development.

This project provides a restful interface to search and access data from the novel `The Lord of the Rings`_.

Installing with Docker
----------------------

Create a ``.env`` file:

.. code-block:: text

    touch .env

Add your ``SECRET_KEY`` to the ``.env`` file

.. code-block:: text

    SECRET_KEY=your-secret-key

Download and install project dependencies

.. code-block:: text

    docker-compose up --build

You can specify the ``-d`` switch to start in detached mode. This will bind port ``80`` and ``443``. Unfortunately, unlike the docker command, there is no command line arguments to specify ports. If you want to change them, edit the ``docker-compose.yml`` file.

After that, start the migration process

.. code-block:: text

    docker-compose exec web python manage.py migrate

Database Seeding
----------------

Use the ``build_all()`` method in the django shell to populate the database

.. code-block:: text

    docker-compose exec web python manage.py shell

.. code-block:: python

    from data.build import build_all
    build_all()


Running
-----------------

.. code-block:: curl

    CURL -X GET http://localhost:8000/api/v2/character/?limit=5&offset=5

.. code-block:: json

    {
        "count": 15,
        "next": "http://localhost:8000/api/v2/character/?limit=5&offset=10",
        "previous": "http://localhost:8000/api/v2/character/?limit=5",
        "results": [
            {
                "name": "sauron",
                "url": "http://localhost:8000/api/v2/character/6/"
            },
            {
                "name": "boromir",
                "url": "http://localhost:8000/api/v2/character/7/"
            },
            {
                "name": "gimli",
                "url": "http://localhost:8000/api/v2/character/8/"
            },
            {
                "name": "galadriel",
                "url": "http://localhost:8000/api/v2/character/9/"
            },
            {
                "name": "samwise gamgee",
                "url": "http://localhost:8000/api/v2/character/10/"
            }
        ]
    }


Browse ``localhost/api/v2/``

.. _`The Lord of the Rings`: https://en.wikipedia.org/wiki/The_Lord_of_the_Rings
