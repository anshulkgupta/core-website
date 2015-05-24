from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')


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

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")