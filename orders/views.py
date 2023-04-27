from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from car.car import Car
from orders.models import Order, LineOrder
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url = "/authenticaiton/login")
def order_process(request):
    order = Order.objects.create(user=request.user)
    car = Car(request)
    order_lines = list()

    for key, value in car.car.items():
        order_lines.append(LineOrder(


            product_id=key,
            quantity=value["quantity"],
            user=request.user,
            order =order 

        ))

    LineOrder.objects.bulk_create(order_lines)

    send_email(
        order=order,
        order_lines=order_lines,
        username=request.user.username,
        emailuser=request.user.email
        )

    messages.success(request, "Order maked correctly")

    return redirect("../store")


def send_email(**kwargs):
    subject="Thanks for the order"
    message=render_to_string("emails/order.html",{
        "order":kwargs.get("order"),
        "order_lines": kwargs.get("order_lines"),
        "username":kwargs.get("username")
    })
    messages_text=strip_tags(message)

    # Here put the email woth you send the buy confirmation
    
    from_email="pruebasemre@gmail.com" 
    to=kwargs.get("emailuser")

    send_mail(subject,messages_text,from_email,[to],html_message=message)