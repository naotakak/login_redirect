'''
Jasper Cheung, Naotaka Kinoshita
SoftDev1 pd7
HW08 -- Do I Know You - with redirect?
2017-10-06
'''

from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
#secret key created for session specific to computer
app.secret_key = os.urandom(32)

#hardcoded account username and password
username = "bob"
pw = "bye"

def authen(u, p):
    if u == username and p == pw:
        return "good"
    return "bad"

@app.route('/')
def hello():
    print session
    if 'username' not in session:
        return render_template('login.html') #add error messages here
    return redirect(url_for('login'))
    
@app.route("/auth", methods = ['POST'])
def auth():
    username = request.form['user']
    password = request.form['password']
    
    print ("USERNAME: " + username)
    print ("PASSWORD: " + password)

    authd = authen(username, password);
    
    print ("AUTHD: " + authd)

    if authd == "good":
        session['username'] = username
        return redirect(url_for('login'))
    
    else:
        #return redirect(url_for('hello'))
        return render_template('login.html', error = "Bad username or password")

@app.route("/login")
def login():
    if 'username' not in session:
        return redirect(url_for('hello'))
    return render_template('welcome.html', username = session['username'])

@app.route("/logout", methods = ['POST'])
def logout():
    print ("\n\n\nLOGOUT")
    print session
    if 'username' in session:
        session.pop('username')
        print "LOGGED OUT"
        print session
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.debug = True
    app.run()
