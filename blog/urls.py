from django.urls import path
from blog import views
app_name='blog'
urlpatterns=[
    path('',views.PostList.as_view(),name='post_list'),
    path('page/<int:page>/',views.PostList.as_view(),name='home'),
    path('postdetail/<int:year>/<int:month>/<int:day>/<slug:post>',views.postdetail,name='post_detail'),
    path('category/<slug:slug>',views.category,name='category'),
    path('category/<slug:slug>/page/<int:page>',views.category,name='category')
]