from django import urls
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path("", views.home_page,name="home"),
	path("rental/",views.rental,name="rental"),
	path("tiffin/",views.tiffin,name="tiffin"),
	path("miscellaneous",views.misc,name="misc"),
	path("register/",views.register,name="register"),
	path("login/",views.login,name="login"),
	path("logout/",views.logout,name="logout"),
	path("laundry/",views.laundary,name="laundry"),
	path("library/",views.lib,name="library"),
	path("checkout/",views.check_out,name="checkout"),
	path("aboutus/",views.about,name="aboutus"),
	path("complete/",views.paymentsuccess,name="complete"),
	path("message/",views.message,name="message"),
    path("<int:hostel_id>/hostel_detail/",views.hostel_description_page,name="hosteldesc"),
	path("<int:tiffinservice_id>/tiffin_detail/",views.tiffin_description_page,name="tiffindesc"),
	path("<int:library_id>/library_detail/",views.library_description_page,name="librarydesc"),
	path("<int:laundry_id>/laundry_detail/",views.laundry_description_page,name="laundrydesc"),
]
