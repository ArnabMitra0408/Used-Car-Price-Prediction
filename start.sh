#!/bin/sh
# start.sh

# Start the Flask application
python db_creation.py &
flask run --host=0.0.0.0 --port=5000