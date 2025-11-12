from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Cart, CartItem
from bazar.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def buy_cart(request):
    if request.method == "POST":
        cart = Cart.objects.get(user=request.user)
        #some purchase logic here
        ###
        cart.delete()
        messages.info(request, "Your order has been received. Thank you!")
    return redirect(request.META.get("HTTP_REFERER", "/bazar/products"))


@login_required
def add_to_cart(request, slug):
    if request.method == "POST":
        product = get_object_or_404(Product, slug=slug)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        input_item_quantity = request.POST.get("item_quantity")
        isSuccess = True

        if input_item_quantity != None and input_item_quantity != item.quantity:
            item.quantity = int(input_item_quantity)
        else:
            if not created:
                item.quantity += 1

        if product.product_qty < item.quantity:
            item.quantity = product.product_qty
            isSuccess = False

        item.save()
        if isSuccess:
            messages.info(
                request, f"Product '{product.title}' has been added to your cart."
            )
        else:
            messages.info(
                request, "You've selected the maximum available quantity for this item."
            )

        return redirect(request.META.get("HTTP_REFERER", "/bazar/products"))


@login_required
def remove_from_cart(request, slug):
    if request.method == "POST":
        cart = Cart.objects.get(user=request.user)
        product = get_object_or_404(Product, slug=slug)
        item = get_object_or_404(CartItem, cart=cart, product=product)
        product_delete = request.GET.get("product_delete") == "true"
        if item.quantity <= 1 or product_delete:
            item.delete()
        else:
            item.quantity -= 1
            item.save()

        return redirect(request.META.get("HTTP_REFERER", "/bazar/products"))


@login_required
def get_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all().order_by("product")
    total = cart.get_total_price()
    print(cart.pk)
    return render(
        request, "cart/cart.html", {"cart": cart, "items": items, "total": total}
    )
