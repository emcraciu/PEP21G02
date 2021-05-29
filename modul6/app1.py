# Create an object for a shop that when iterated will return all of the products in the shop

class Shop:
    # constructor receive list of products in shop
    def __init__(self, products: list):
        self.products = products

    # iter method must return an object that is an iterator or generator
    def __iter__(self):
        # a copy of the products list is sent to the iterator so that the original is not consumed
        return ShopIterator(self.products.copy())


# class for iterator object must implement at least: __iter__ and __next__
class ShopIterator:
    def __init__(self, products: list):
        self.products = products

    # iter method for iterators will always return it's self
    def __iter__(self):
        return self

    def __next__(self):
        if not self.products:
            raise StopIteration
        # we consume the list of products
        return self.products.pop()


if __name__ == '__main__':
    shop = Shop(['books', 'bananas', 'water'])
    print('From constructor:', shop.products)

    # iterate using for loop
    for item in shop:
        print('For loop', item)

    # iterate using methods
    shop_iter = shop.__iter__()
    print('First product:', shop_iter.__next__())
    print('Second product:', shop_iter.__next__())
    print('Third product:', shop_iter.__next__())
    print('Forth product:', shop_iter.__next__())
