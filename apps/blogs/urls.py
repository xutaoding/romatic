from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^entry/', views.ShowEntryView.as_view(), name='entry')
]
