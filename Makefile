.PHONY: install
install:
	poetry install

.PHONY: shell
shell:
	poetry shell

.PHONY: run
run:
	poetry run python snkrs_scrap/app.py

.PHONY: format
run:
	poetry run blue snkrs_scrap