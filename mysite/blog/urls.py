from django.urls import path
from .views import blog_list,blog_detail,blog_delete,blog_create,blog_update

urlpatterns =[
    path('',blog_list),
    path('create/', blog_create),
    path('<id>/update/', blog_update),
    path('<id>/',blog_detail),
    path('<id>/delete/',blog_delete),
]   