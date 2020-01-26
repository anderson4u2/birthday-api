from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://birthdays@postgres/birthdays'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
mm = Marshmallow(app)

# User Class/Model
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True)
  dob = db.Column(db.DateTime(100))

  def __init__(self, username, dob):
    self.username = username
    self.dob = dob

  # @mm.validates('username')
  # def validate_username(self, username):
  #   # assert only contains letters
  #   bool(re.match("^[A-Za-z]*$", username))
  #   return username

#   @mm.validates('dob')
#   def validate_dob(self, dob, value):
#     # assert date is earlier than today
#     # assert it's of the format "YYYY-MM-DD"
#     return value

# User Schema
class UserSchema(mm.Schema):
  class Meta:
    fields = ('id', 'username', 'dob')

# Init schema
user_schema = UserSchema()

# Create a User
@app.route('/hello', methods=['POST'])
def add_user():
  # Parse payload's expected fields into vars
  username = request.json['name']
  dob = request.json['dateOfBirth']

  # Create new_user object from payload
  new_user = User(username, dob)

  # Add new user to session and commit to db
  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

# Update/add a birthday to an existing User
@app.route('/hello/<username>', methods=['PUT'])
def update_user(username):
  # Get user object from db by searching for `username`
  user = db.session.query(User).filter_by(username=username).first()

  # Parse DOB field from payload
  updated_dob = request.json['dateOfBirth']

  # Update/create DOB field in `username` and commit to db
  user.dob = updated_dob
  db.session.commit()

#   return user_schema.jsonify(new_user)
  return make_response("",204)

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

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
