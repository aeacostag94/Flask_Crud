from app import app
from utils.db import db

import config

#This fuction create the tables when te app is initializate
with app.app_context():
    db.create_all()



# This line let run python like py app.py and activate debug mode.
if __name__ == "__main__":
    app.run(debug=True)
