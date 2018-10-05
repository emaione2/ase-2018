from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter, ValidationError
from flakon import
_USERS = {'1':'Barabba','2':'Bubba'}
_IDS = {val:id for id, val in _USERS.items()}

class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if(value in _USERS):
            return _USERS
app = Flask(__name__)

@app.route('/api', methods=['PUT','DELETE','GET']) # questa e' un'annotazione, che indica all'istanza "app" che se gli arrivano richieste con '/api' deve chiamare la
def my_microservice():
    print(request)
    response = jsonify({'Hello':'world'})
    print(response)
    print(response.data)
    return response

@app.route('/api/person/<person_id>')
def person(person_id):
    response = jsonify({'Hello':person_id})
    return response

if __name__=='__main__':
    app.run()