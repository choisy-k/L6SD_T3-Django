#where we defined the paths to different pages
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about_us/", views.about_us, name="about us"),
    path("shop/", views.shop, name="shop"),
    path("contact_us/", views.contact_us, name="contact us"),
    path("<int:id>", views.shop_note, name="shop note"),
    path("create/", views.create, name="create"),
]
