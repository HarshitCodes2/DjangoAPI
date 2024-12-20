from django.urls import path
from . import views

urlpatterns = [
    path("api_home/", views.product_view_api_home, name="product_view_api_home"),
    path("<int:pk>/",views.ProductView.as_view(),  name="product"),
    # path("<int:pk>/",views.getProductDetails,  name="product"), example for functional view
    path("<int:pk>/update",views.ProductUpdateView.as_view(),  name="update_product"),
    path("<int:pk>/delete",views.ProductDestroyView.as_view(),  name="delete"),
    path("create", views.ProductCreateView.as_view(), name="create_product"),
    path("", views.getProductDetails, name="get_details")
]
