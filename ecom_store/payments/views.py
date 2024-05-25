from django.shortcuts import render, redirect
import time
import stripe
from django.conf import settings
import ssl
import smtplib
from email.message import EmailMessage
import sys

sys.path.append("/home/jciafardo/official-car-store/ecom_store")
print("path", sys.path)
from common_files.views import get_cart_attrs
from common_files.shared_models import productData
from django.http import HttpResponseRedirect


# creates checkout session and sends user receipt through email
def create_checkout_session(response):
    stripe_products = []
    line_items = []
    stripe.api_key = settings.STRIPE_SECRET_KEY  # stripe api key
    cart_items = get_cart_attrs(response)[0]

    # iterate though items in cart to create stripe objects, deplete product quantity, and add sale for product
    for i, item in enumerate(cart_items):
        stripe_products.append(stripe.Product.create(name=item.name))
        stripe_product_prices = stripe.Price.create(product=stripe_products[i], unit_amount=int(
            item.price * 100), currency='usd', tax_behavior='exclusive')

        line_item = {'price': stripe_product_prices, 'quantity': 1}
        if item.quantity > 0:
            line_items.append(line_item)

    if len(line_items) == 0:  # if nothing is in cart redirect to prev page
        url = '/'
        return url

        item.quantity -= 1
        item.save()

        sale = productData.objects.get(product_id=item.id)
        sale.num_sales += 1
        sale.save()

    # stripe payments session

    checkout_session = stripe.checkout.Session.create(
        line_items=line_items,
        payment_method_types=['card'],
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout-success',
        cancel_url='http://127.0.0.1:8000/checkout-cancel',
        automatic_tax={'enabled': True},
        expires_at=int(time.time() + 2000),  # Configured to expire after 30 mins

    )

    session_id = checkout_session.id

    # here we send confirmation email commented out because stripe can take care of sendimg emails

    '''
    email_sender = 'email sender'
    email_password = 'this is not the password'
    email_recipient = 'sender email'

    subject = 'My Store'
    body = 'Receipt'

    email_object = EmailMessage()
    email_object['From'] = email_sender
    email_object['To'] = email_recipient
    email_object['subject'] = subject
    email_object.set_content(body)

    context = ssl.create_default_context()

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_recipient, email_object.as_string())
    '''



    if checkout_session.url is None:
        return HttpResponseRedirect('/')

    return checkout_session.url


# Failed payments
def checkout_cancel(response):
    return render(response, 'cancel-payments.html')


# Successful payments
def checkout_success(response):
    # make sure to delete items out of users cart also dont lower the quantity of the item unitl the checkout is
    # successful also don't add sale unitl payment is good thru
    from time import sleep
    sleep(5)
    try:
        session_id = create_checkout_session(response)['session_id']
        session = stripe.checkout.Session.retrieve(session_id)
    except:
        pass



    if session["payment_status"] == "paid":
        response.session['checkout_session'] = None
    if session["payment_status"] == "unpaid":
         return render(response, 'checkout-success.html', {})
