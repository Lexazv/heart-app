#!/bin/bash

runServer() {
    uvicorn src.main:app --host 0.0.0.0 --workers 2 --reload
}

runMigrations() {
    sleep 2
    alembic upgrade head
}

while getopts :sm flag

do
    case $flag in
        s) runServer;;
        m) runMigrations;;
    esac
done
