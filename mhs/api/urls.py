from django.urls import path

from . import views

urlpatterns = [
    path("item", views.ItemView.as_view()),
    path("get-all-items", views.get_all_items),
    path("delete-item/<int:id>", views.delete_item),
    path("add-item", views.add_item),
]
