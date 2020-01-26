from . import db


class User(db.Model):
    """
    Model for users and their birthdays
    """
    # __tablename__ = "users"
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(100),
                         unique=True,
                         nullable=False,
                         index=True,)
    date_of_birth = db.Column(db.DateTime(100),
                              nullable=True)

    def __init__(self, username, date_of_birth):
        self.username = username
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # @mm.validates('username')
    # def validate_username(self, username):
    #   # assert only contains letters
    #   bool(re.match("^[A-Za-z]*$", username))
    #   return username

    #   @mm.validates('date_of_birth')
    #   def validate_date_of_birth(self, date_of_birth, value):
    #     # assert date is earlier than today
    #     # assert it's of the format "YYYY-MM-DD"
    #     return value
