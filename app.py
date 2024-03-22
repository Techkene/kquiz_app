from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/contact_us')
def contact_us():
    return render_template("contact_us.html")

@app.route('/set_question')
def set_question():
    return render_template("set_question.html")

@app.route('/answer_question')
def answer_question():
    return render_template("answer_question.html")

@app.route('/logout')
def logout():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug= True)