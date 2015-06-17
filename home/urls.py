from django.conf.urls import url

from . import views

urlpatterns = [
    # /home/
    url(
        regex=r'^$', view=views.index_view, name='home',
    ),
    url(regex=r'^about/$', view=views.AboutView.as_view(), name='about'),
    url(regex=r'^contact/$', view=views.ContactView.as_view(), name='contact'),
]
