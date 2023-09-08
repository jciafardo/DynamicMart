from django.http import HttpResponseRedirect
from ecom_store.common_files.shared_models import Products, productData, cartItems


# Used for functions used by both apps

# returns products in declining order by how many sales the product has
def get_best_sellers():
    sales = []  # list of dicts to determine best sellers

    # loop thorough all products to see what sells the best
    for i, product in enumerate(Products.objects.all()):
        sales.append({'id': product.id, 'num_sales': productData.objects.get(product_id=product.id).num_sales,
                      'price': product.price})

    sales = sorted(sales, key=lambda d: d['num_sales'], reverse=True)  # sort list in best sales to least
    print(sales)
    #  loop through sales makes sure product is in stock
    sales = [sale for sale in sales if Products.objects.get(id=sale['id']).quantity > 0]

    ordered_products = []
    for i, sale in enumerate(sales):
        ordered_products.append(Products.objects.get(id=sale['id']))
    print(ordered_products)
    return ordered_products  # return list of products from best selling to least selling (excluded products with no quantity)


# returns all items in users cart and total price (used by store_front and payments app)
def get_cart_attrs(response):
    # returns all items in users cart
    total = 0
    user_id = response.user.id
    cart_items = []  # list of Products objects that belong to user
    if response.user.is_authenticated:
        users_cart_items = cartItems.objects.filter(
            user_id=user_id)  # list of cartItems objects that belong to user
    else:
        users_cart_items = cartItems.objects.filter(session=response.session.session_key)

    for item in users_cart_items:
        total += Products.objects.get(id=item.product_id).price
        cart_items.append(Products.objects.get(id=item.product_id))

    return [cart_items, total]


# add or remove items from carts

