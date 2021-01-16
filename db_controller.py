from sqlalchemy import exc
from flask import jsonify
from db_connector import User


def get_users():
    users = User.query.all()
    users_list = [json_convert(user) for user in users]
    return jsonify({'Users': users_list})


def get_user(id_user):
    user = User.query.get(id_user)
    if user is None:
        return jsonify({'Error': 'No exist'})
    return jsonify(json_convert(user))


def add_user(data):
    try:
        if not data["rating"].isdigit():
            raise TypeError
        user = User(username=data["username"], email=data["email"], rating=data["rating"])
        user.add_to_db()
    except TypeError:
        return jsonify({'Error': 'Wrong type'})
    except exc.IntegrityError:
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
    return jsonify(json_convert(user))


def upd_user(id_user, data):
    user = User.query.get(id_user)
    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    if "rating" in data:
        user.rating = data["rating"]
    if not str(user.rating).isdigit():
        return jsonify({'Error': 'Wrong type'})
    user.upd_db()
    return json_convert(user)


def json_convert(user: User):
    return {'username': user.username, 'email': user.email, 'rating': user.rating}
