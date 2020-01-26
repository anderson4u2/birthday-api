from flask import current_app as app
from flask_marshmallow import Marshmallow, fields

# Init Marshmallow
mm = Marshmallow(app)

def validate_username(username):
    if bool(re.match("^[A-Za-z]*$", username)):
        return True
    else:
        raise ValidationError("username's fucked")

def validate_date():
    pass

def validate_username(self, username):
    # assert only contains letters
    # bool(re.match("^[A-Za-z]*$", username))
    return username

# User Schema
class UserSchema(mm.Schema):
    class Meta:
        fields = ("id", "username", "date_of_birth")
    username = fields.fields.Str(validate=validate_username)
    # date_of_birth = fields.fields.DateTime(format="%Y-%m-%d")

# Init schema
user_schema = UserSchema()
