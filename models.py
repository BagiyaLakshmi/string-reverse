'''
Created on 

@author: Bagiya

source:
'''

import json

def reverse_string(str1):

    return(str1[::-1])

def addition(a,b):
    sum= a + b
    return sum

def update_json(name, age, city):
    new_data ={
        name :{
            "age":age,
            "city":city
        }
    }
    with open('data.json') as file:
        data_dict = json.load(file)
        print(data_dict)
    data_dict.update(new_data)
    print(data_dict)
    with open ("data.json", "w")as f:
        json.dump(data_dict, f,  indent = 4)


if __name__ == '__main__':

    # resut = reverse_string("Ganesh")
    update_json('Deepika', 17, 'Los Vegas')


