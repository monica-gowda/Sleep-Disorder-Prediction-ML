import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
import pickle
from flask import Flask, render_template, request
import pandas as pd

 

app = Flask(__name__) #Initialize the flask App

boost = pickle.load(open('sleep_boost.pkl','rb'))
Quadra = pickle.load(open('sleep_Quadra.pkl','rb'))
@app.route('/')

@app.route('/index')
def index():
	return render_template('index.html')

 

#@app.route('/future')
#def future():
#	return render_template('future.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)	

 

@app.route('/prediction')
def prediction():
	return render_template('prediction.html')
    
 

# Load the model (ensure this path is correct)
 

@app.route('/predict', methods=['POST'])
def predict():
    resul = {}  # Default empty dictionary
    result = ''  # Default empty string

    if request.method == 'POST': 
            resul = request.form.to_dict()
            print(resul)
       
            
              
                                      
            Gender = request.form['Gender']
            if Gender == '0':
                Depa = 'Male'
            elif Gender == '1':
                Depa = 'Female'
            
            Age = request.form['Age']   
            Occupation = request.form['Occupation']
            if Occupation == '0':
                Edu = 'Software Engineer'
            elif Occupation == '1':
                Edu = 'Doctor'
            elif Occupation == '2':
                Edu = 'Sales Representative'
            elif Occupation == '3':
                Edu = 'Teacher'
            elif Occupation == '4':
                Edu = 'Nurse'
            elif Occupation == '5':
                Edu = 'Engineer'     
            elif Occupation == '6':
                Edu = 'Accountant'   
            elif Occupation == '7':
                Edu = 'Scientist'   
            elif Occupation == '8':
                Edu = 'Lawyer'  
            elif Occupation == '9':
                Edu = 'Salesperson'   
            elif Occupation == '10':
                Edu = 'Manager'   
                              

            Sleep_Duration = request.form['Sleep_Duration']
            Quality_of_Sleep = request.form['Quality_of_Sleep']
            Physical_Activity_Level = request.form['Physical_Activity_Level']
            Stress_Level = request.form['Stress_Level']
           

            BMI_Category = request.form['BMI_Category']
            if BMI_Category == '0':
                Job = 'Overweight'
            elif BMI_Category == '1':
                Job = 'Normal'
            elif BMI_Category == '2':
                Job = 'Obese' 
            elif BMI_Category == '3':
                Job = 'Normal Weigh'
              

             
            Blood_Pressure = request.form['Blood_Pressure']
            if Blood_Pressure == '0':
                jobs = '126/83'
            elif Blood_Pressure == '1':
                jobs = '125/80'
            elif Blood_Pressure == '2':
                jobs = '140/90'
            elif Blood_Pressure == '3':
                jobs = '120/80' 
            elif Blood_Pressure == '4':
                jobs = '132/87'
            elif Blood_Pressure == '5':
                jobs = '130/86'
            elif Blood_Pressure == '6':
                jobs = '117/76' 
            elif Blood_Pressure == '7':
                jobs = '118/76'
            elif Blood_Pressure == '8':
                jobs = '128/85'
            elif Blood_Pressure == '9':
                jobs = '131/86' 
            elif Blood_Pressure == '10':
                jobs = '128/84'
            elif Blood_Pressure == '11':
                jobs = '115/75'
            elif Blood_Pressure == '12':
                jobs = '135/88'   
            elif Blood_Pressure == '13':
                jobs = '129/84' 
            elif Blood_Pressure == '14':
                jobs = '129/84'
            elif Blood_Pressure == '15':
                jobs = '130/85'
            elif Blood_Pressure == '16':
                jobs = '115/78' 
            elif Blood_Pressure == '17':
                jobs = '119/77'
            elif Blood_Pressure == '18':
                jobs = '121/79'
            elif Blood_Pressure == '19':
                jobs = '125/82' 
            elif Blood_Pressure == '20':
                jobs = '135/90'
            elif Blood_Pressure == '21':
                jobs = '122/80'
            elif Blood_Pressure == '22':
                jobs = '142/92'   
            elif Blood_Pressure == '23':
                jobs = '140/95'
            elif Blood_Pressure == '24':
                jobs = '139/91'
            elif Blood_Pressure == '25':
                jobs = '118/75'           
            Heart_Rate = request.form['Heart_Rate']
            
                        
            Daily_Steps = request.form['Daily_Steps']
              
            Model = request.form['Model']
            # Ensure input data is in the correct format
            input_variables = pd.DataFrame([[Gender,Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level, Stress_Level, BMI_Category, Blood_Pressure, Heart_Rate,Daily_Steps]],
                                            columns=['Gender','Age','Occupation','Sleep_Duration','Quality_of_Sleep','Physical_Activity_Level','Stress_Level','BMI_Category','Blood_Pressure','Heart_Rate','Daily_Steps'],
                                            index=['input'])

            # You may need to preprocess 'Company', 'Location', etc. if they are categorical variables
            # Assuming preprocessing is not required for simplicity
            
            # Convert the dataframe to the format required by the model
            final_features = input_variables.to_numpy()
            print(final_features)

           
            if Model == 'GradientBoostingClassifier':
                prediction = boost.predict(final_features)
                output =prediction[0]
         
            elif Model == 'QuadraticDiscriminantAnalysis':
                prediction = Quadra.predict(final_features)
                output =prediction[0]
                
             

         
        
                                         
    
    return render_template('result.html', prediction_text=output, model=Model,Depa=Depa,Age=Age,Edu=Edu,Sleep_Duration=Sleep_Duration,Quality_of_Sleep=Quality_of_Sleep,Physical_Activity_Level=Physical_Activity_Level,Stress_Level=Stress_Level,Job=Job,jobs=jobs,Heart_Rate=Heart_Rate,Daily_Steps=Daily_Steps)



@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')

 
    
if __name__ == "__main__":
    app.run(debug=True)
