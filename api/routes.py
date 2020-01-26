from flask import request, jsonify, make_response
from flask import current_app as app
# from flask_marshmallow import Marshmallow
from .models import db, User
from .schemas import user_schema
# from flask_marshmallow import Marshmallow


# Init ma
# mm = Marshmallow(app)

# User Schema
# class UserSchema(mm.Schema):
#   class Meta:
#     fields = ('id', 'username', 'date_of_birth')

# Init schema
# user_schema = UserSchema(mm.Schema)

# Create a User
@app.route('/hello', methods=['POST'])
def add_user():
  # Parse payload's expected fields into vars
  username = request.json['name']
  date_of_birth = request.json['dateOfBirth']

#   Create new_user object from payload
  new_user = User(username, date_of_birth)

  # Add new user to session and commit to db
#   db.session.add(new_user)
#   db.session.commit()
  data = user_schema.dump(new_user)

  return user_schema.jsonify(data)

import json
# Saves/updates the given user's name and date of birth in the database
@app.route('/hello/<username>', methods=['PUT'])
def update_user(username):
    json_input = request.get_json()

#   data = user_schema.load(json_input)
#   # ffs = json.load(data)
#   print(json.dumps(data, indent=4))
#   # user = User.create(
#   #   username=username,
#   #   date_of_birth=data["dateOfBirth"]
#   # )

#   # data = user_schema.dump(user)
#   # return data, 201
#   return json.dumps(data, indent=4)
  # Get user object from db by searching for `username`
  # user = db.session.query(User).filter_by(username=username).first()
    return "bazinga"
#   Parse date_of_birth field from payload
#   updated_date_of_birth = request.json['dateOfBirth']

#   # Update/create date_of_birth field in `username` and commit to db
#   user.date_of_birth = updated_date_of_birth
#   db.session.commit()

#   return user_schema.jsonify(new_user)
#   return make_response("",204)

# Get User's birthday
@app.route('/hello/<username>', methods=['GET'])
def get_user_birthday(username):
#   user = User.query.get(username)
    user = db.session.query(User).filter_by(username=username).first()
    return user_schema.jsonify(user)


# # Delete Product
# @app.route('/product/<id>', methods=['DELETE'])
# def delete_product(id):
#   product = Product.query.get(id)
#   db.session.delete(product)
#   db.session.commit()

#   return product_schema.jsonify(product)
