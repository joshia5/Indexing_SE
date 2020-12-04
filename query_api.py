import flask










app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/query', methods=['GET'])
def query_handler():
        query_string = flask.request.args.get("query")
        return query_string 
@app.route('/add_file', methods=['POST'])
def add_file_handler():
    file_json = flask.request.get_json(force=True)
    print(file_json)
    return flask.jsonify(isError= False,
                        message= "Success",
                        statusCode= 200,
                        data= ""), 200
app.run(host='0.0.0.0',port=80)
