import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'товар': item,
        'количество': quantity,
        'цена': price,
        'покупатель': buyer,
        'дата': date
    }

    with open('orders.json', 'r', encoding='utf-8') as f:
        orders_dict = json.load(f)
        orders_list = orders_dict['orders']
        orders_list.append(data)

    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(orders_dict, f, indent=4, ensure_ascii=False)


write_order_to_json('product_1', 25, 4300, 'user_1', '20.03.2021')
