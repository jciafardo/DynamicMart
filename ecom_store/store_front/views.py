from django.http import HttpResponseRedirect
from ecom_store.common_files.views import get_cart_attrs
from ecom_store.common_files.shared_models import Products, productData, cartItems
from django.shortcuts import render
from fuzzywuzzy import fuzz
from django.shortcuts import redirect


# Create your views here.

# Homepage for browsing and about company
def home(response):
    if response.method == 'POST':
        print('POSTED', response.POST)
        if 'add-cart-item-id' in response.POST or 'remove-item-id' in response.POST or 'checkout' in response.POST:
            return cart_post_handler(response, 'home')

    return render(response, 'home.html',
                  {'ordered_products': get_best_sellers()[:3], 'cart_items': get_cart_attrs(response)[0],
                   'total': get_cart_attrs(response)[1]})


# view products and filter through them
def products(response):
    if response.method == 'POST':

        if 'add-cart-item-id' in response.POST or 'remove-item-id' in response.POST or 'checkout' in response.POST:
            return cart_post_handler(response, 'products')
    return render(response, 'products.html',
                  {'ordered_products': get_best_sellers(), 'cart_items': get_cart_attrs(response)[0],
                   'total': get_cart_attrs(response)[1]})


#  function is responsible for the logic of searching or a product
def search_results(response):
    results = []
    search = None  # search is none by default unless post request is made

    try:
        search = response.POST['search']
        search = str(search).lower()
        search = response.session['search'] = search

    except KeyError:
        try:
            if response.session['search'] is not None:
                search = response.session['search']
        except KeyError:
            pass

    for car in get_best_sellers():
        car_name = str(car.name.lower())
        match_strength = fuzz.ratio(car_name, search)
        if match_strength >= 45:
            if car.quantity > 0:
                results.append(car)
    if len(results) == 0:
        results = 'No Matches Found'

    if 'add-cart-item-id' in response.POST or 'remove-item-id' in response.POST or 'checkout' in response.POST:
        return cart_post_handler(response, 'search_results')

    return render(response, 'search-results.html', {'results': results, 'ordered_products': get_best_sellers(),
                                                    'cart_items': get_cart_attrs(response)[0],
                                                    'total': get_cart_attrs(response)[1]})


# View product user clicked on, can also add to cart
def single_view(response, id):
    try:
        for product in get_best_sellers():

            if product.name == id:
                product = product
                break
    except:
        product = 'no product'

    if response.method == 'POST':
        if 'add-cart-item-id' in response.POST or 'remove-item-id' in response.POST or 'checkout' in response.POST:
            if 'checkout' in response.POST:
                if len(get_cart_attrs(response)[0]) <= 0:  # checks if cart is empty if so ask user to add item to cart
                    return render(response, 'view_product.html',
                                  {'product': product, 'cart_items': get_cart_attrs(response)[0],
                                   'total': get_cart_attrs(response)[1], 'error_msg': 'Please Add Items To Cart !'})

            return cart_post_handler(response, '/view/' + id)

    return render(response, 'view_product.html', {'product': product, 'cart_items': get_cart_attrs(response)[0],
                                                  'total': get_cart_attrs(response)[1]})


# returns products in declining order by how many sales the product has
def get_best_sellers():
    sales = []  # list of dicts to determine best sellers

    # loop thorough all products to see what sells the best
    for i, product in enumerate(Products.objects.all()):
        sales.append({'id': product.id, 'num_sales': productData.objects.get(product_id=product.id).num_sales,
                      'price': product.price})

    sales = sorted(sales, key=lambda d: d['num_sales'], reverse=True)  # sort list in best sales to least

    #  loop through sales makes sure product is in stock
    sales = [sale for sale in sales if Products.objects.get(id=sale['id']).quantity > 0]

    ordered_products = []
    for i, sale in enumerate(sales):
        ordered_products.append(Products.objects.get(id=sale['id']))

    return ordered_products  # return list of products from best selling to least selling (excluded products with no quantity)


def add_cart(response):
    product_id = Products.objects.get(id=response.POST.get('add-cart-item-id'))
    if response.user.is_authenticated:
        user_id = response.user.id
        cart_item = cartItems(product_id=product_id.id, user_id=user_id)

    else:
        # response.set_cookie(settings.SESSION_COOKIE_NAME, response.session.session_key)
        response.session.save()
        session = response.session.session_key
        cart_item = cartItems(product_id=product_id.id, session=session)

    cart_item.save()  # add item to cart



    if get_cart_attrs(response)[1] > 999999:
        cart_item.delete()




def remove_cart(response):
    id = response.POST.get('remove-item-id')  # Products object returned by html form
    if response.user.is_authenticated:
        user_id = response.user.id
        remove_cart_item = cartItems.objects.filter(product_id=id, user_id=user_id)
    else:
        remove_cart_item = cartItems.objects.filter(product_id=id, session=response.session.session_key)
    remove_cart_item[0].delete()


def cart_post_handler(response, view_name):
    if 'add-cart-item-id' in response.POST:  # add item to cart
        add_cart(response)

        return redirect(view_name)



    elif 'remove-item-id' in response.POST:  # remove item from cart
        remove_cart(response)

        return redirect(view_name)  # change this line so that we dont get redirected to /view/view/gtr


    elif 'checkout' in response.POST:
        from ecom_store.payments.views import create_checkout_session
        return HttpResponseRedirect(create_checkout_session(response))


def test(response):
    return render(response, 'delete.html', {})
