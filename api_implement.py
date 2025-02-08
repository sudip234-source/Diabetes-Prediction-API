# import json
# import requests


# url = 'http://127.0.0.1:8000'
# pg= int(input("pregnancies"))
# gl= int(input("Glucose"))
# bp= int(input("Blood Pressure : "))
# sk= int(input("Skin Thickness: "))
# ins= int(input("Insulin: "))
# bmi= float(input("BMI: "))
# dpf= float(input("Diabetes Pedigree Function: "))
# age= int(input("Age: "))

# input_data_for_model = {
    
#     'pregnancies' : pg,
#     'Glucose' : gl,
#     'BloodPressure' : bp,
#     'SkinThickness' : sk,
#     'Insulin' : ins,
#     'BMI' : bmi,
#     'DiabetesPedigreeFunction' : dpf,
#     'Age' : age
    
#     }

# input_json = json.dumps(input_data_for_model)

# response = requests.post(url, data=input_json)
# print(response.text)

import requests
import json

input_data = {
    'pregnancies': 2,
    'Glucose': 23,
    'BloodPressure': 23,
    'SkinThickness': 2,
    'Insulin': 323,
    'BMI': 33.0,
    'DiabetesPedigreeFunction': 3.0,
    'Age': 45
}

url = 'http://127.0.0.1:8000/diabetes_prediction'  # Ensure the correct port

response = requests.post(url, json=input_data)

# Print detailed response
print("Status Code:", response.status_code)
print("Response Text:", response.text)
