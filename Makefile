.PHONY: pylint
pylint:
	docker compose run flask pylint api core app.py --load-plugins pylint_flask pylint_flask_sqlalchemy
