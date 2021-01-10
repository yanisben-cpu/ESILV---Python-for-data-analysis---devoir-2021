import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# here, put the model's pickle file location:

file_model = 'C:/Users/yYaNn/Documents/A4/Data Analysis Python/ObesityDataSet_raw_and_data_sinthetic (2)/pickle files/my_preds.pickle'

model = pickle.load(open(file_model, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = prediction[0]

    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
    
    