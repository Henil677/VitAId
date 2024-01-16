from flask import Flask, render_template, request

app = Flask(__name__)

# Define the symptoms and medications
symptoms = ["fever", "cough", "headache", "sore throat", "runny nose", "fatigue", "body aches", "chills", "nausea", "vomiting",
            "diarrhea", "shortness of breath", "chest pain", "dizziness", "loss of taste", "loss of smell", "rash", "itching", "joint pain", "muscle cramps"]

medications = {
    "headache": ["ibuprofen"],
    "cough": ["cough syrup"],
    "fever": ["paracetamol"],
    "sore throat": ["amoxicillin"],
    "runny nose": ["antihistamines"],
    "fatigue": ["decongestants"],
    "body aches": ["acetaminophen"],
    "chills": ["aspirin"],
    "nausea": ["antacids"],
    "vomiting": ["probiotics"],
    "diarrhea": ["laxatives"],
    "shortness of breath": ["inhaler"],
    "chest pain": ["nitroglycerin"],
    "dizziness": ["beta blockers"],
    "loss of taste": ["steroids"],
    "loss of smell": ["antifungal cream"],
    "rash": ["calamine lotion"],
    "itching": ["capsaicin cream"],
    "joint pain": ["pain relievers"],
    "muscle cramps": ["muscle relaxants"],
}

# Define the Q-table, hyperparameters, reward function, and Q-learning function here as before
# You can include the code for these components here.

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling user input and getting medication suggestions
@app.route('/get_medication', methods=['POST'])
def get_medication():
    symptom = request.form['symptom'].lower()
    if symptom in medications:
        medication_list = medications[symptom]
        return render_template('result.html', symptom=symptom, medications=medication_list)
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)

