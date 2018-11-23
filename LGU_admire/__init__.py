from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("LGU_admire")
app.config.from_pyfile("config.py")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

