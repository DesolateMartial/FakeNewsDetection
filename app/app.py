from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)
model = joblib.load(os.path.join('..', 'models', 'logistic_model.pkl'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ''
    if request.method == 'POST':
        news_text = request.form['text']
        prediction = model.predict([news_text])[0]
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
