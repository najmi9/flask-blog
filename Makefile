.PHONY: pylint
pylint:
	docker compose run flask pylint core app.py --load-plugins pylint_flask pylint_flask_sqlalchemy
