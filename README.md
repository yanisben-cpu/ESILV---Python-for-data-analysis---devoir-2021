# ESILV - Python-for-data-analysis - 2021
Python for data analysis project made by Yanis BENABDESSLAM

## Project's goal
This project consists in the deployment of a Flask API using a Machine Learning model on an "Obesity level" dataset.

### Prerequisites

You must have the following libraries installed:
  - Pandas
  - Numpy
  - Matplotlib
  - Seaborn
  - Scikit Learn
  - Flask (for API)

### Project Structure
This project has 5 major parts :
1. Proj python Yanis Benabdesslam.ipynb - This contains our data visualizations and the tested Machine Learning models to predict people's obesity types based on our csv file.
2. app_test.py - This contains Flask APIs that receives someones's physical features (Gender, height, etc.), computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. app.py - This also contains a Flask API that computes the precited value based on our model and returns it in an explorer.
5. templates/index.html - This folder contains the HTML page on which the user will enter the values he wants for model's prediction.

### Running the project
1. First, open the Jupyter Notebook file and run every row, in order to create the "converted dataset" and the model's pickle file.

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000 (in general, it will be http://127.0.0.1:5000)

Enter valid numerical values in all 16 input boxes and hit Predict to see the result.

You should be able to see the predcited obesity type on the HTML page!

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to run the console version off the app, with no html page support
```
python app_test.py
```
Then run the request.py file and lauch the program to see the result in python console.

### Visuals
All the vizuals can be found in the Jupyter Notebook file called "Proj Python Yanis Benabdesslam.ipynb".

### Model
The model is in the pickle file named "my_preds.pickle" : you can generate it again by launching the jupyter notebook file.
The notebook also attests of all the models that I have tested in this project.

### Conclusion
In our case, Stochastic Gradient Boosting seemed to be the best model, with an accuracy of 96.8%, but a little bit better than the other ones. When we tried to test the models several times, there were some attempts where the Bagging model gave a better accuracy: the results are really close.
