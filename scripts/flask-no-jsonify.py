from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <a href='/nojsonify'>dict response</a>
    <br>
    <a href='/jsonify1'>jsonify response</a>
    <br>
    <a href='/testdict'>test response</a>
    <br>
    <a href='/healthcheck'>healthcheck</a>
    <br>
    <a href='/plaindict'>plain</a>
    <br>
    <a href='/jsonify'>jsonify</a>
    <br>
    <a href='/request'>request args</a>
    """

@app.route('/request')
def req():
    return request.args.get('name')

@app.route('/nojsonify')
def nojson():
    return {'jsonify': 'false'}, 201

@app.route('/jsonify1')
def json():
    l = ['user1','user2','user3']
    ll = [l.to_json() for user in l]
    return jsonify(ll)

@app.route('/plaindict')
def testdict():
    test = 'testing'
    name = 'roger'
    age =  30
    lst = [1,2,3]
    #return jsonify(test, name, age)
    return {
            "development": test,
            "name": name,
            "age": age,
            "list": lst
            }


@app.route('/jsonify')
def testjsonify():
    test = 'testing'
    name = 'roger'
    age =  30
    lst = [1,2,3]
    #return jsonify(test, name, age)
    return jsonify({
            "development": test,
            "name": name,
            "age": age,
            "list": lst
            })


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    msg = (
        "this sentence is already halfway over, "
        "and still hasn't said anything at all"
    )
    return {"message": msg}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
