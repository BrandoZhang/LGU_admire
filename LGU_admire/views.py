"""
view function
"""
from flask import flash, redirect, url_for, render_template

from LGU_admire import app, db
from LGU_admire.models import Message
from LGU_admire.forms import AdmireForm



