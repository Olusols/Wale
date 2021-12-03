from .views import index, blog, about, PostDetail,  DeletePostView, CategoryList, CategoryDetail, search
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('search/', search, name='search'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('<int:pk>/<slug:slug>/',
         CategoryDetail.as_view(), name='category-detail'),

    path('<int:pk>/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    #path('add-post/', AddPostView.as_view(), name='add-post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
]
