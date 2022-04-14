from fastapi import FastAPI

from src.app.urls import router
from connections.db_connect import init_db_connection, close_db_connection


app = FastAPI()


app.include_router(router, prefix='/api')


@app.on_event('startup')
def start_db():
    init_db_connection(app)


@app.on_event('shutdown')
def stop_db():
    close_db_connection(app)


# TODO:
#     - setup logging; search by 'print' word
#     - implement heart data calculations
#     - replace docker run_stuff script with wait-for-it.sh (investigate)