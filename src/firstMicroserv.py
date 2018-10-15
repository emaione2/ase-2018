from flask import Flask, jsonify, request, url_for, render_template
from werkzeug.routing import BaseConverter, ValidationError
#from flakon import JsonBlueprint
from src.bluefile import blueIstance

_USERS = {'1': 'Barabba', '2': 'Bubba'}
_IDS = {val: id for id, val in _USERS.items()}


class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if (value in _USERS):
            return _USERS


app = Flask(__name__)
app.register_blueprint(blueIstance)


#, methods=['PUT', 'DELETE','GET']
@app.route('/api')  # questa e' un'annotazione, che indica all'istanza "app" che se gli arrivano richieste con '/api' deve chiamare la funzione seguente (, methods=['PUT', 'DELETE','GET'])
def my_microservice():
    print(request)
    response = jsonify({'Hello': 'world'})
    print(response)
    print(response.data)
    return response

with app.test_request_context():
    my_microservice_url:str=url_for('my_microservice')


@app.route('/api/person/<person_id>')
def person(person_id):
    response = jsonify({'Hello': person_id})
    return response

with app.test_request_context():
    person_url: str = url_for('person',person_id='your_name')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/help')
def give_help():
    print('#request: ',request)
    usage_str:str=str(app.url_map)
    return render_template('help.html', usage=usage_str)

if __name__ == '__main__':
    print(my_microservice_url)
    print(person_url)

    print(app.url_map)

    app.run(host='0.0.0.0',port='80')
