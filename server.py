from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    if 'increment' not in session:
        session['increment'] = 2
    return render_template('index.html')

@app.route('/count')
def countTwo():
    session['count'] += int(session['increment'])
    return render_template('index.html') 

@app.route('/increment', methods=['POST'])
def setIncrement():
    session['increment'] = request.form['increment']
    return render_template('index.html') 

@app.route('/destroy_session')
def reset_count():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)