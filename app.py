from flask import request
from flask_name import app
import db_controller


@app.route('/')
def index():
    return 'Hello, i Index.' \
           "i just sit here, and i'm fine"


@app.route('/users')
def get_users():
    return db_controller.get_users()


@app.route('/users/<id_user>')
def get_user(id_user):
    return db_controller.get_user(id_user)


@app.route('/users', methods=['POST'])
def add_user():
    return db_controller.add_user(request.get_json(force=True))


@app.route('/users/<id_user>', methods=['DELETE'])
def del_user(id_user):
    return db_controller.del_user(id_user)


@app.route('/users/<id_user>', methods=['PUT'])
def upd_user(id_user):
    return db_controller.upd_user(id_user, request.get_json(force=True))
