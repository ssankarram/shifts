from django.conf.urls import url
from django.contrib.auth.views import login
from . import views 
from accounts.views import (login_view, logout_view, register_view, options_view)

urlpatterns = [
	#/shift
	url(r'^$', views.index, name='index'), #default home page, go to views and look for function called index
	#url(r'(test)^$', views.index, name='index'), #default home page, go to views and look for function called index
	#url(r'^(groups)/$', views.index2, name='index2'),
	#url(r'^login/$', login, {'template_name': 'accounts/login.html'})
	#/register
	#url(r'^register/$', views.UserFormView.as_view(), name='register'), #default home page, go to views and look for function called index

	#/shift/
	url(r'^(?P<shift_id>[0-9]+)/$', views.detail, name="detail"),
	url(r'^(?P<group_shift_id>[0-9]+)/group/$', views.detail2, name="detail2"),
	url(r'^login/', login_view, name='login'),
	url(r'^logout/', logout_view, name='logout'),
	url(r'^register/', register_view, name='register'),
	url(r'^options/', options_view, name="options"),
	#url(r'^login/', login_view, name='login'),
	#url(r'^logout/', logout_view, name='logout')
]
#url(r'^(?P<group_shift_id>[0-9]+)/group/$', views.detail2, name="detail2"),
