from django.urls import path
from .views import bajarildi, delete, edit, todo
from .api_views import IshListView, IshDetailView

urlpatterns = [
    path('', todo, name='home'),
    path('<int:id>/delete/', delete,name="delete"),
    path('<int:id>/bajarildi/', bajarildi,name="bajarildi"),
    path('<int:id>/edit/', edit,name="edit"),
    path('api/v1/', IshListView.as_view()),
    path('api/v1/<int:pk>/', IshDetailView.as_view()),
]