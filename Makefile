.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m website.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m website.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python -m website.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m website.manage createsuperuser

.PHONY: update
update: install migrate ;