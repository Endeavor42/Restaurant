import json
import sys

from flask import Flask
from flask import make_response

from flask_cors import CORS
from flask_cors import cross_origin


app = Flask(__name__)

cors = CORS(app)
app.config["CORS HEADERS"] = "Content-type"


@app.errorhandler(404)
@cross_origin()
def not_found(error):
    return make_response(
        {"error": "endpoint is not valid"}
    )  # make_response is used for error handling and standardization


# sample endpoint
@app.route("/foo", methods={"GET"})
@cross_origin()
def foo():
    return {
        "foo": "bar"
    }  # you don't need to return using the make_response method as long as what's being returned is a dict


@app.route("/bar/<int:qux>", methods={"GET"})
@cross_origin()
def bar(qux):
    if qux % 2 == 0:
        return {"input": "even"}
    return {"input": "odd"}


def main():
    debug_state = True if "-d" in sys.argv or "--debug" in sys.argv else False
    app.run(host="0.0.0.0", debug=debug_state)


if __name__ == "__main__":
    main()
