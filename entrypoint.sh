#!/bin/sh

echo "-- flask db init --"
flask db init

echo "-- flask db migrate --"
flask db migrate

echo "-- flask db upgrade --"
flask db upgrade

echo "-- start flask server --"
flask run --host=0.0.0.0