DOCKER_COMPOSE:=docker compose
EXEC_CORE:=$(DOCKER_COMPOSE) exec auth_api


# work with docker

build:
#	export DOCKER_BUILDKIT=1 && docker build -f auth_service/Dockerfile -t async_api_image .
	$(DOCKER_COMPOSE) build

ps:
	$(DOCKER_COMPOSE) ps

up:
	$(DOCKER_COMPOSE) up


restart:
	$(DOCKER_COMPOSE) restart

down:
	$(DOCKER_COMPOSE) down

pull:
	$(DOCKER_COMPOSE) pull

shell:
	$(EXEC_CORE) bash

flake8:
	$(EXEC_CORE) flake8

test:
	$(EXEC_CORE) pytest

# Scheduler

makemigrations:
	$(DOCKER_COMPOSE) exec scheduler python3 manage.py makemigrations

migrate:
	$(DOCKER_COMPOSE) exec scheduler python3 manage.py migrate

createsuperuser:
	$(DOCKER_COMPOSE) exec scheduler python3 manage.py createsuperuser

flake8-scheduler:
	$(DOCKER_COMPOSE) exec scheduler flake8

# makemigrations_auth:
# 	$(EXEC_CORE) alembic revision --autogenerate -m "$(NAME)"
# #     example make makemigrations_auth NAME='Init database'
#
# migrate_auth:
# 	$(EXEC_CORE) alembic upgrade head
#
# roles_auth:
# 	$(EXEC_CORE) python src/create_roles.py
#
# social_networks_auth:
# 	$(EXEC_CORE) python src/create_social_networks.py
#
# superuser_auth:
# 	$(EXEC_CORE) python src/superuser.py

