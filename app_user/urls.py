from django.conf.urls import url

from app_user.views import login, logout

urlpatterns = [
    url(r'^login/$', login, name='login_page'),
    url(r'^logout/$', logout, name='logout_page'),
]