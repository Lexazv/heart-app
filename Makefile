run_server:
	uvicorn src.main:app --workers 2 --reload

run_tests:
	pytest -vv -s

run_migrations:
	alembic upgrade head

drop_tables:
	alembic downgrade -1

cov:
	coverage report -m

cov_html:
	coverage html
