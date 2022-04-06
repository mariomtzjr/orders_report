import requests
import os

def get_orders():
    url = os.getenv('ORDERS_URL')
    print("ORDERS_URL: ", url)
    response = requests.get(url)
    print("Response: ", response.text)
    return response.json()


def get_operator(operator_id):
    url = os.getenv('OPERATOR_URL') + str(operator_id)
    print("OPERATOR_URL: ", url)
    response = requests.get(url)
    print("Response: ", response.text)
    return response.json()


def get_comensal(comensal_id):
    url = os.getenv('COMENSAL_URL') + str(comensal_id)
    print("COMENSAL_URL: ", url)
    response = requests.get(url)
    print("Response: ", response.text)
    return response.json()