from django.urls import path
from . import views

app_name="car"

urlpatterns = [
    path("add/<int:product_id>/", views.add_product, name="add"),
    path("delete/<int:product_id>/", views.delete_product, name="delete"),
    path("reduct/<int:product_id>/", views.reduct_product, name="reduct"),
    path("clear/", views.clean_car, name="clear"),
]