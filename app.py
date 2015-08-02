from flask import Flask, redirect, render_template, request, url_for
from flask_mail import Mail
from flask.ext.mail import Message
import config
import json

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)
data = {}

from forms import ContactForm

# import data from relevant JSON
def load_data():
    global data
    for name, path in app.config['DATA_FILENAMES'].iteritems():
        with open(path, 'r') as data_file:
            data[name] = json.loads(data_file.read())

@app.route('/')
def index():
    return render_template('index.html', **data)

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/initiatives')
def initiatives():
    return render_template('initiatives.html')

@app.route('/team')
def team():
    return render_template('team.html', **data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # Bypassing form for now
    return render_template('contact.html')

    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(form.subject.data,
                    recipients=['coreboard@columbia.edu'])
        msg.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

load_data()

if __name__ == '__main__':
    app.run(debug = config.DEBUG, host=config.HOST, port=config.PORT)
