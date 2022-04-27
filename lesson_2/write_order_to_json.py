import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'товар': item,
        'количество': quantity,
        'цена': price,
        'покупатель': buyer,
        'дата': date
    }

    with open('orders.json', 'r') as f:
        orders_dict = json.load(f)
        orders_list = orders_dict['orders']
        orders_list.append(data)

    with open('orders.json', 'w') as f:
        json.dump(orders_dict, f, indent=4)
