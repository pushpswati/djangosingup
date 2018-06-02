from django.conf.urls import url
from projectapp import views
urlpatterns=[
url(r'^projectapp$',views.PostList.as_view(),name='PostList'),
]
