from django.shortcuts import render, redirect

from .forms import formContact
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):

    formCon = formContact()

    if request.method == "POST":
        formCon = formContact(data = request.POST)
        if formCon.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            context = request.POST.get("context")

            email = EmailMessage("Message app django",
            "User with name: {}, with the email: {}, send you...:\n\n {}".format(name,email,context),
            "",["pruebasemre@gmail.com"], reply_to= [email])

            try:
                email.send()
                print("si")
                return redirect("/contact/?valid")

            except:
                print("no")
                return redirect("/contact/?wrong")


    return render(request, "contact/contact.html", {'formConta': formCon})