# todosapi
To do rest api with the django rest framework

# command
pip freeze > requirements.txt

# start de migration and database
docker compose run web python manage.py migrate

# connect to container
docker exec -it [container id] /bin/bash

# docker exec -it cab7cc5e083f /bin/bash

# python manage.py createsuperuser
