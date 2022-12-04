#zyk's stuff please don't touch!! :]
#main

from flask import Flask,render_template,session,request,redirect,g,url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for("home"))

    return render_template('login.html')
@app.route('/home')
def home():
    if g.user:
        return render_template('home.html',user=session['user'])
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user=None

    if 'user' in session:
        g.user = session['user']

if __name__ == '__main__':
    app.run(debug=True)