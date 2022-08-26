from django.urls import path

#import my_view from todo Aplication
from . import views

app_name = 'todo'
urlpatterns = [

    #url for index page
    path('', views.my_viewss, name="index"), #name = ".." for (..) name of file template.html

    #url for detail page
    path('<int:task_id>', views.detail_view, name="detail"), #name = ".." for (..) name of file template.html

    #url for add page
    path('create',views.create_view, name='create'),

    #url for edit task page
    path('update/<int:task_id>', views.update_view, name='update'),

    #url for delete task
    path('delete/<int:task_id>', views.delete_view, name='delete'),

]