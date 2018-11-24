from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask("LGU_admire")
app.config.from_pyfile("config.py")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from LGU_admire import views, errors, commands
