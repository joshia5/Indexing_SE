import flask
from parseData import parseData
from index import *

index = Index()


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/query', methods=['GET'])
def query_handler():
    query_string = flask.request.args.get("query")
    result = index.find_entry(query_string)
    return flask.jsonify(result)


@app.route('/add_file', methods=['POST'])
def add_file_handler():
    file_json = flask.request.get_json(force=True)
    parseData(file_json, index)
    return flask.jsonify(isError=False,
                         message="Success",
                         statusCode=200,
                         data=""), 200


app.run(host='0.0.0.0', port=80)
