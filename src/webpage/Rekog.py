import boto3
from django.shortcuts import redirect

def Rekog(image):
    client = boto3.client('rekognition', region_name='ap-southeast-2')

    car_pic = open(image,'rb').read()

    rekresp = client.detect_labels(Image={'Bytes': car_pic},
                                MinConfidence=50)
    
    car_type_dict = {}

    for label in rekresp['Labels']:
        if label['Name'] == 'Sedan' or label['Name'] == 'Suv' or label['Name'] == 'Coupe' or label['Name'] == 'Truck' or label['Name'] == 'Van' or label['Name'] == 'Convertible':
            car_type_dict[label['Name']] = label['Confidence']
       

        
    if not car_type_dict:
        return False
    
    car_type = []
    for items in car_type_dict.keys():
        car_type.append(items)
    
    return car_type[0]