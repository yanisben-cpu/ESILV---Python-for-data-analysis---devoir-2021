from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import pickle as p

# here, put the model's pickle file location:
    
file_model = 'C:/Users/yYaNn/Documents/A4/Data Analysis Python/ObesityDataSet_raw_and_data_sinthetic (2)/pickle files/my_preds.pickle' 


model = p.load(open(file_model, 'rb'))
app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def obes_predict():
    
     v_data = request.get_json()
     prediction = model.predict(v_data)
     res = prediction[0]
     return jsonify(res)

if __name__ == '__main__':
     app.run(debug=True)
     
     

