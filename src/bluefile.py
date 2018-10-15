from flask import Blueprint, render_template

blueIstance = Blueprint('blueName', __name__, url_prefix='/blue')

@blueIstance.route('im')
def imBlue():
    return render_template('hello.html',name='YO Listen up  here`s story\n About a little guy that live in a blue world')

@blueIstance.route('/dabbadee')
def dabbada():
    return render_template('hello.html',name='I`m blue dabba dee-a dabba da da ba dee dabba da')

