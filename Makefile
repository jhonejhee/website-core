.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall && poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

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
update: install migrate install-pre-commit;
