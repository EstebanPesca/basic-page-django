def import_total_car(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["car"].items():
            total = total + float(value["price"])
    else:
        total = "First login in the page"

    return {"import_total_car":total}