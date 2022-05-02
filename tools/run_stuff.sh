#!/bin/bash

runServer() {
    uvicorn src.main:app --host 0.0.0.0 --workers 2 --reload
}

runMigrations() {
    until ! nc -z localhost 5432
    do	    	    
        sleep 1
    done

    alembic upgrade head
}

while getopts :sm flag

do
    case $flag in
        s) runServer;;
        m) runMigrations;;
        *) echo "Invalid flag!"; exit 1;;
    esac
done
