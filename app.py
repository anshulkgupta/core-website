from flask import Flask, redirect, render_template, request, url_for
from flask_mail import Mail
from flask.ext.mail import Message


app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)


from config import SECRET_KEY
from forms import ContactForm


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calendar")
def calendar():
    return render_template('calendar.html')

@app.route("/initiatives")
def initiatives():
    return render_template('initiatives.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(form.subject.data,
                    recipients=['coreboard@columbia.edu'],
                    sender=(form.name.data, form.email.data))
        msg.body = form.message.data
        mail.send(msg)
        return redirect(url_for('index'))
    return render_template('contact.html',
                            form=form)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")