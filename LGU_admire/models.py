"""
class Message
author: str
content: str
time: datetime
IP_addr: str
likes: int
"""
from datetime import datetime
from LGU_admire import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140), nullable=False)
    author_name = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    ip_addr = db.Column(db.String)
    likes = db.Column(db.Integer, default=0)
