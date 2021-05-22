shop1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}
shop2 = {'mere': 11, 'pere': 15, 'prune': 6}
shop3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}

need_to_buy = {'mere': 2, 'pere': 3, 'prune': 6}

available_shops = {'pofi': shop1, 'kauf': shop2, 'lidl': shop3}


def best_buy(shops: dict, cart: dict):
    total = {}
    smallest_cost = None
    _best_buy = ''
    for product, quanty in cart.items():
        # print(product, quanty)
        for shop_name, shop_products in shops.items():
            # print(shop_name, shop_products)
            price = shop_products.get(product)
            # print(product, quanty, price)
            cost = quanty * price
            # print(shop_name, product, cost)
            saved_cost = total.get(shop_name, 0)
            new_saved_cost = saved_cost + cost
            total[shop_name] = new_saved_cost
    for shop_name, total_cost in total.items():
        print(shop_name, total_cost)
        if smallest_cost is None or smallest_cost > total_cost:
            smallest_cost = total_cost
            _best_buy = shop_name
    print(smallest_cost, _best_buy)

best_buy(available_shops, need_to_buy)

print(__name__)
