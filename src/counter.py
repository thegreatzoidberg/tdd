"""Module docstring for counter.py"""
# Import third-party modules before first-party modules
from flask import Flask
from src import status

app = Flask(__name__)

COUNTERS = {}

@app.route('/counters/<name>',methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT

    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED

@app.route('/counters/<name>',methods=['PUT'])
def update_counter(name):
    """Update a counter"""
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS
    COUNTERS[name] += 1

    return {name: COUNTERS[name]}, status.HTTP_200_OK

@app.route('/counters/<name>',methods=['GET'])
def read_counter(name):
    """Read a counter"""
    app.logger.info(f"Request to read counter: {name}")
    global COUNTERS
    x = {name: COUNTERS[name]}

    return x, status.HTTP_200_OK

@app.route('/counters/<name>',methods=['DELETE'])
def delete_counter(name):
    """Delete a counter"""
    app.logger.info(f"Request to delete counter: {name}")
    global COUNTERS
    del COUNTERS[name]
    if name not in COUNTERS:
        return name, status.HTTP_204_NO_CONTENT
