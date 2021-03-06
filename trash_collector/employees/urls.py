from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('daily_tasks/', views.select_day, name='daily_tasks'),
    path('charge/<int:customer_id>', views.confirm, name='charge'),
    path('select_day/<str:day_of_the_week>', views.select_day, name ='select_day')
]