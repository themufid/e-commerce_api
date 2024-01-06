from django.shortcuts import render, get_object_or_404
from .models import Product, Purchase
from .forms import PurchaseForm
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def purchase_form(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = PurchaseForm()

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():

            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity

            return render(request, 'purchase_success.html', {'product': product, 'quantity': quantity, 'total_price': total_price})

    return render(request, 'purchase_form.html', {'product': product, 'form': form})

def checkout(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    return render(request, 'checkout.html', {'purchase': purchase})

def process_payment(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)

    return render(request, 'payment_success.html', {'purchase': purchase})