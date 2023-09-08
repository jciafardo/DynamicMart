from django.shortcuts import render
from ecom_store.common_files.shared_models import Products, productData
# Create your views here.


def upload_products(response):  # this function serves a page where superusers can upload products to inventory
    isSuperUser = response.user.is_superuser

    if response.method == 'POST':
        print(response.POST)
        for attr in response.POST:
            print(attr)
            print(response.POST[attr])
            print("")
        new_product = Products(name=response.POST['carName'], quantity=response.POST['carQuantity'],
                               price=response.POST['carPrice'], picture=response.POST['carPicture'],
                               description=response.POST['carDescription'])
        new_product.save()
        new_product_data = productData(product_id=new_product.id, num_sales=0)
        new_product_data.save()

    return render(response, 'upload-products.html', {'isSuperUser': isSuperUser})
