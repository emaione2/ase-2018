import _json

from flakon import JsonBlueprint
from flask import request, jsonify, abort
from simplejson import JSONDecoder

from myservice.classes.poll import Poll, NonExistingOptionException, UserAlreadyVotedException

doodles = JsonBlueprint('doodles', __name__, url_prefix='/doodles')

_ACTIVEPOLLS = {} # list of created polls
_POLLNUMBER = 0 # index of the last created poll

@doodles.route('', methods=['POST', 'GET']) #TODO: complete the decoration
def all_polls():

    if request.method == 'POST':
        result = create_doodle(request)

    elif request.method == 'GET':
        result = get_all_doodles(request)
    
    return result


@doodles.route('/<id>', methods=['GET', 'DELETE', 'PUT']) #TODO: complete the decoration
def single_poll(id):
    global _ACTIVEPOLLS
    result = ""
    A=_ACTIVEPOLLS

    exist_poll(id) # check if the Doodle is an existing one

    if request.method == 'GET': # retrieve a poll
        result = jsonify(_ACTIVEPOLLS[id].serialize())

    elif request.method == 'DELETE': 
        #TODO: delete a poll and get back winners
        ACTIVEPOLLS:dict = _ACTIVEPOLLS
        poll:Poll=ACTIVEPOLLS.pop(id)
        winners:list=poll.get_winners()
        result=jsonify({ 'winners': winners })

    elif request.method == 'PUT':
        #vote in a poll
        result=vote(id,request)


    return result

@doodles.route('/<id>/<person>', methods=['GET', 'DELETE', 'PUT']) #TODO: complete the decoration
def person_poll(id, person):
    result=None
    #TODO: check if the Doodle exists
    exist_poll(id)
    pool:Poll=_ACTIVEPOLLS[id]
    if request.method == 'GET':
        #TODO: retrieve all preferences cast from <person> in poll <id>
        votedoptions:list=pool.get_voted_options(person)
        result=jsonify({'votedoptions': votedoptions})

    if request.method == 'DELETE':
        if(pool.delete_voted_options(person)):
            result=jsonify({'removed':True})
        else:
            result = jsonify({'removed': False})
        #TODO: delete all preferences cast from <person> in poll <id>

    return result
       

def vote(id, request):
    result = ""
    #TO DO: extract person and option fields from the JSON request
    jreq = request.get_json(silent=True)
    if (jreq == None):
        abort(400)
        return
    person:str=jreq['person']
    vote:str=jreq['option']

    try:
        # TODO: cast a vote from person in  _ACTIVEPOLLS[id]
        poll:Poll=_ACTIVEPOLLS[id]
        poll.vote(person, vote)
        winners: list = poll.get_winners()
        result = jsonify({'winners': winners})

    except UserAlreadyVotedException:
        abort(400) # Bad Request
    except NonExistingOptionException:
        # TODO: manage the NonExistingOptionException
        abort(400)

    return result


def create_doodle(request):
    global _ACTIVEPOLLS, _POLLNUMBER
    #TODO: create a new poll in _ACTIVEPOLLS based on the input JSON. Update _POLLNUMBER by incrementing it.
    jreq=request.get_json(silent=True)
    if(jreq==None):
        abort(400)
        return

    try:
        _POLLNUMBER += 1
        title:str=jreq['title']
        opts:dict= jreq['options']
        id:str=str(_POLLNUMBER)

        poll:Poll=Poll(id,title,opts)
        _ACTIVEPOLLS[id] = poll

    except:
        return abort(400)

    return jsonify({'pollnumber': _POLLNUMBER})


def get_all_doodles(request):
    global _ACTIVEPOLLS
    return jsonify(activepolls = [e.serialize() for e in _ACTIVEPOLLS.values()])

def exist_poll(id):
    A=_ACTIVEPOLLS
    if int(id) > _POLLNUMBER:
        abort(404) # error 404: Not Found, i.e. wrong URL, resource does not exist
    elif not(id in _ACTIVEPOLLS):
        abort(410) # error 410: Gone, i.e. it existed but it's not there anymore