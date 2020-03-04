from django.conf.urls import url
from . import views 

urlpatterns = [
        url('add-note', views.add_note),
        url('update-note', views.update_note),
        url('get-all-note', views.get_all_note)
]