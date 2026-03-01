from flask import Flask,request,jsonify
from flask_cors import CORS
import pickle
from suggestion import suggest

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl","rb"))

@app.route('/predict',methods=['POST'])
def predict():

    data = request.json

    cgpa = data['cgpa']
    internship = data['internship']
    project = data['project']
    technical = data['technical']
    communication = data['communication']

    prediction = model.predict_proba([[cgpa,internship,project,technical,communication]])

    prob = prediction[0][1]*100

    suggestions = suggest(cgpa,internship,project,technical,communication)

    return jsonify({
        "Placement Chance":str(prob)+"%",
        "Suggestions":suggestions
    })

if __name__=="__main__":
    app.run(debug=True)