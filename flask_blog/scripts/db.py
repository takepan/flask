from flask_script import Command
from flask_blog import db

class InitDB(Command):
    "createdatabase"

    def run(self):
        db.create_all()
