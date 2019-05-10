from django.conf.urls import url
from . import views  

urlpatterns = [
	url(r'^$', views.home),
	url(r'^work$', views.work),
	url(r'^about$', views.about),
	url(r'^contact$', views.contact),
	url(r'^resume$', views.resume),
	url(r'^form_process$', views.form_process),
	url(r'^success$', views.success)
]