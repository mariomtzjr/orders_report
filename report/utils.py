import requests
import os

def get_orders():
    url = os.getenv('ORDERS_URL')
    response = requests.get(url)

    return response.json()


def get_operator(operator_id):
    url = os.getenv('OPERATOR_URL') + str(operator_id)
    response = requests.get(url)

    return response.json()


def get_comensal(comensal_id):
    url = os.getenv('COMENSAL_URL') + str(comensal_id)
    response = requests.get(url)

    return response.json()


def get_product(product_id):
    url = os.getenv('PRODUCT_URL') + str(product_id)
    response = requests.get(url)

    return response.json()


def get_dates_from_params(orders_data, params):
    import pandas as pd
    from datetime import datetime

    dates_interval = [date.strftime("%Y-%m-%d") for date in pd.date_range(start=params.get("start_date"),end=params.get("end_date"))]
    orders = [order for order in orders_data if order.get("date") in dates_interval]
    
    return orders


def generate_order_report(orders):
    # Importing defaultdict
    from collections import defaultdict

    orDict = defaultdict(list)
    sold_product_dict = {}

    products = []
    orders_data = [order.pop("comensal") for order in orders]
    
    for order in orders:
        for order_item in order.get("order_items"):
            products.append((order_item.get("name"), float(order_item.get("unit_price")), order_item.get("quantity")))
    
    # iterating over list of tuples
    for key, val, _ in products:
        orDict[key].append({"quantity": _, "price": val})

    for k, v in orDict.items():
        sold_product_dict[k] = [{"total_quantity": sum(item.get("quantity") for item in v), "total": sum(item.get("price") for item in v)}]

    return sold_product_dict