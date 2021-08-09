from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "value" not in session:
        session['value'] = 1
    if "string" not in session:
        session['string'] = ''
    if "total" not in session:
        session['total'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def checkout():
    if request.form['building'] == 'farm':
        session['value'] = randint(10, 20)
        session['total'] += session['value']
        session['string'] += f"<li style='color: green'>Earned {session['value']} from the {request.form['building']}</li>"
    elif request.form['building'] == 'cave':
        session['value'] = randint(5, 10)
        session['total'] += session['value']
        session['string'] += f"<li style='color: green'>Earned {session['value']} from the {request.form['building']}</li>"
    elif request.form['building'] == 'house':
        session['value'] = randint(2, 5)
        session['total'] += session['value']
        session['string'] += f"<li style='color: green'>Earned {session['value']} from the {request.form['building']}</li>"
    else:
        randVal = randint(-50, 50)
        if randVal < 0:
            session['value'] = randVal
            session['total'] += session['value']
            session['string'] += f"<li style='color: red'>Entered a casino and lost... Ouch.. {session['value']} gold</li>"
        else:
            session['value'] = randVal
            session['total'] += session['value']
            session['string'] += f"<li style='color: green'>Earned {session['value']} from the {request.form['building']}</li>"
    
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)