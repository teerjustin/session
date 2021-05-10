from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route('/')
def index():
    if "counter" not in session:
        session['counter'] = 1
    session['counter'] += 1
    return render_template("index.html")

@app.route('/add_two', methods = ['POST'])
def add_two():
    if request.form['button'] == "button":
        session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    if request.form['button'] == "reset":
        session['counter'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)