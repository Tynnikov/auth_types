.PHONY: install
install:
	poetry install --no-dev

.PHONY: update
update:
	poetry update

.PHONY: install-dev-deps
install-dev-deps:
	poetry install

.PHONY: install-dev
install-dev: install-dev-deps
	poetry run pre-commit install --install-hooks --hook-type pre-commit --hook-type prepare-commit-msg

.PHONY: format
format:
	poetry run isort ./
	poetry run black ./