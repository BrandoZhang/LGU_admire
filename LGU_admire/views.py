"""
view function
"""
from flask import request, flash, redirect, url_for, render_template

from LGU_admire import app, db
from LGU_admire.models import Message
from LGU_admire.forms import AdmireForm


@app.route("/", methods=["GET", "POST"])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = AdmireForm()
    if form.validate_on_submit():
        name = form.author_name.data
        body = form.body.data
        message = Message(content=body, author_name=name, ip_addr=request.remote_addr)
        db.session.add(message)
        db.session.commit()
        flash("Your message have been sent to LGU!")
        return redirect(url_for('index'))
    return render_template("index.html", form=form, messages=messages)


@app.route("/message/<int:message_id>/delete", methods=['POST'])
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    flash('Message deleted.', 'success')
    return redirect(url_for("index"))


@app.route("/message/<int:message_id>/like", methods=["POST"])
def like_message(message_id):
    message = Message.query.get_or_404(message_id)
    message.likes += 1
    db.session.commit()
    flash("LIKE!", "success")
    return redirect(url_for("index"))
