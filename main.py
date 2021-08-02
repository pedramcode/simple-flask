from os import stat
from flask import Flask, Response, request
import json
import data

# Create the web server, simply by this line of code
# __name__ is current module name, so we tell to flask that
# your module is "__name__" or current module. it needs it
# to find routes and settings and etc :) okay!?
app = Flask(__name__)


@app.route("/list", methods=["GET"])
def list_of_contacts():
    # Read data from file - Its a list of dicts
    _res = data.read_data()
    # Dump json data to string and send as response
    return Response(json.dumps(_res), status=200, content_type="application/json")


@app.route("/new", methods=["POST"])
def add_new_contact():
    # Read json data from HTTP request
    _req = request.json
    # Check if is there any json data!
    if _req == None:
        return Response("Bad request!", status=400)
    # Check required keys in the JSON
    if "firstname" not in _req.keys() or "lastname" not in _req.keys() or "phone" not in _req.keys():
        return Response("Bad request!", status=400)
    # Prepare the dictionary to add in file
    data_to_add = {
        "firstname":_req["firstname"],
        "lastname":_req["lastname"],
        "phone":_req["phone"],
    }
    # Insert data to file
    data.write_data(data_to_add)
    # And response!
    return Response("Data inserted!", status=201)


if __name__ == "__main__":
    # Entry point of the Python app. I bet you know about it.

    # "0.0.0.0" is host. I used "0.0.0.0" instead of "127.0.0.1" because "0.0.0.0" is
    # visible for any device outside of local system. so you can use this web server
    # from other computers or networks! and "8080" is port
    app.run("0.0.0.0", 8080)
