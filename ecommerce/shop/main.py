
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from django.db import models
from fastapi import Form
from django.shortcuts import get_object_or_404
from shop.models import Product, Purchase
from shop.forms import PurchaseForm
from shop.serializers import ProductSerializer, PurchaseSerializer
from django.contrib.auth.decorators import login_required
from django.db import transaction

app = FastAPI()
templates = Jinja2Templates(directory="shop/templates")

@app.get("/purchase-form/{product_id}", response_class=HTMLResponse)
async def purchase_form(request: Request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return templates.TemplateResponse("purchase_form.html", {"request": request, "product": product})

@app.get("/", response_class=HTMLResponse)
async def index(request):
    products = Product.objects.all()
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.post("/purchase/{product_id}", response_model=PurchaseSerializer)
async def purchase(product_id: int, form: PurchaseForm = Depends(PurchaseForm)):
    product = get_object_or_404(Product, id=product_id)
    quantity = form.quantity
    total_price = product.price * quantity

    with transaction.atomic():
        purchase = Purchase.objects.create(product=product, quantity=quantity, total_price=total_price)

    return purchase

@app.get("/checkout/{purchase_id}", response_class=HTMLResponse)
async def checkout(request: Request, purchase_id: int):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    return templates.TemplateResponse("checkout.html", {"request": request, "purchase": purchase})

@app.post("/checkout/{purchase_id}", response_class=HTMLResponse)
async def process_payment(purchase_id: int):
    purchase = get_object_or_404(Purchase, id=purchase_id)

    # Proses pembayaran (tambahkan logika pembayaran sesuai kebutuhan Anda)

    return templates.TemplateResponse("payment_success.html", {"purchase": purchase})
