from flask import Flask, render_template, request
import joblib

model = joblib.load('best_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/events')
def events():
    return "You are on the events page."

@app.route('/Stories')
def stories():
    return render_template('stories.html')

@app.route('/Topics')
def topics():
    return render_template('topics.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Process the form data here
    preg = eval(request.form.get('preg'))
    plas = eval(request.form.get('plas'))
    pres = eval(request.form.get('pres'))
    skin = eval(request.form.get('skin'))
    test = eval(request.form.get('test'))
    mass = eval(request.form.get('mass'))
    pedi = eval(request.form.get('pedi'))
    age = eval(request.form.get('age'))

    # Make a prediction using the loaded model
    prediction = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if(prediction[0]==0):
        return render_template('non_diabetic.html')
    else:
        return render_template('diabetic.html')

app.run(host="0.0.0.0", port=5000)