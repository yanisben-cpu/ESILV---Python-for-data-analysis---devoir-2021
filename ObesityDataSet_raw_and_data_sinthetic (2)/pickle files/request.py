import requests
import json


data = [[1, #   - Gender: Male = 1, Female = 2
        20, #   - Age
        1.91, #   - Height
        60.0, #   - Weight
        1, #   - family_history_with_overweight: yes = 1, no = 0
        1, #   - FAVC: yes = 1, no = 0
        0.0, #   - FCVC - consumption of vegetables
        2.0, #   - NCP - Number of main meals
        3, #   - CAEC: no = 0, Sometimes = 1, Frequently = 2, Always = 3
        0, #   - SMOKE: yes = 1, no = 0
        2.0, #   - CH2O - consumption of water
        0, #   - SCC: yes = 1, no = 0
        0.0, #   - FAF - Physical activity frequency
        2.0, #   - TUE - Time using technology devices
        0, #   - CALC: no = 0, Sometimes = 1, Frequently = 2, Always = 3
        0]] #   - MTRANS: Public_Transportation = 0, Automobile = 1, Walking = 2, Motorbike = 3, Bike = 4


data_2 = [[1, #   - Gender: Male = 1, Female = 2
          25, #   - Age
          1.74, #   - Height
          90.0, #   - Weight
          1, #   - family_history_with_overweight: yes = 1, no = 0
          1, #   - FAVC: yes = 1, no = 0
          0.0, #   - FCVC - consumption of vegetables
          2.0, #   - NCP - Number of main meals
          3, #   - CAEC: no = 0, Sometimes = 1, Frequently = 2, Always = 3
          1, #   - SMOKE: yes = 1, no = 0
          2.0, #   - CH2O - consumption of water
          0, #   - SCC: yes = 1, no = 0
          0.0, #   - FAF - Physical activity frequency
          2.0, #   - TUE - Time using technology devices
          0, #   - CALC: no = 0, Sometimes = 1, Frequently = 2, Always = 3
          0]] #   - MTRANS: Public_Transportation = 0, Automobile = 1, Walking = 2, Motorbike = 3, Bike = 4


headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
j_data   = json.dumps(data)
j_data_2 = json.dumps(data_2)

r  = requests.post('http://127.0.0.1:5000//api/', data = j_data, headers = headers)
r_2 = requests.post('http://127.0.0.1:5000//api/', data = j_data_2, headers = headers)

print()
print("Physical state: ", r.text)
print()
print("Physical state 2: ", r_2.text)
