# Change the best_buy function we have created in module 4 into a class so that we can dynamically add new shops
# and items to our shopping list and recalculate best place to buy our product

shop1 = {'mere': 10, 'pere': 15, 'prune': 7, 'ananas': 20}
shop2 = {'mere': 11, 'pere': 15, 'prune': 6}
shop3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}


class BestBuy:
    shops = dict()
    cart = dict()

    def __init__(self):
        pass

    def add_shop(self, shop_name, shop_items, ):
        self.shops.update({shop_name: shop_items})

    def add_item_to_buy(self, item_to_buy, quantity):
        self.cart.update({item_to_buy: quantity})

    def best_buy(self):
        total = {}
        smallest_cost = None
        _best_buy = ''

        for product, quantity in self.cart.items():
            for shop_name, shop_products in self.shops.items():
                price = shop_products.get(product)
                cost = quantity * price
                saved_cost = total.get(shop_name, 0)
                new_saved_cost = saved_cost + cost
                total[shop_name] = new_saved_cost

        for shop_name, total_cost in total.items():
            if smallest_cost is None or smallest_cost > total_cost:
                smallest_cost = total_cost
                _best_buy = shop_name

        print(smallest_cost, _best_buy)


if __name__ == '__main__':
    best_buy = BestBuy()

    # add items to buy
    best_buy.add_item_to_buy('mere', 2)
    best_buy.add_item_to_buy('pere', 3)
    best_buy.add_item_to_buy('prune', 6)

    # add shops with products
    best_buy.add_shop('profi', shop1)
    best_buy.best_buy()
    best_buy.add_shop('lidl', shop2)
    best_buy.best_buy()

    # add item and recalculate
    best_buy.add_item_to_buy('mere', 10)
    best_buy.best_buy()
