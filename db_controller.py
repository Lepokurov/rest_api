import sqlalchemy
from flask import jsonify
from db_connector import User


def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {'name': user.username, 'email': user.email, }
        output.append(user_data)
    return jsonify({'Users': output})


def get_user(id_user):
    user = User.query.get(id_user)
    if user is None:
        return jsonify({'Error': 'No exist'})
    return jsonify({'name': user.username, 'email': user.email})


def add_user(data):
    try:
        user = User(username=data["username"], email=data["email"])
        user.add_to_db()
    except TypeError:
        return jsonify({'Error': 'TypeError'})
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'Error': 'No unique'})
    except KeyError:
        return jsonify({'Error': 'Wrong attributes'})
    except Exception:
        return jsonify({'Error': 'Unknown Exception'})
    return jsonify(data)



def del_user(id_user):
    user = User.query.get(id_user)
    if user is None:
        return jsonify({'Error': 'No exist'})
    user.del_from_db()
    return jsonify({'name': user.username, 'email': user.email})
