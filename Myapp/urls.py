from django.urls import path
from Myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('details',views.details,name='details'),
    path('fetch',views.fetch,name='fetch'),
    path('update',views.update,name='update'),
    path('button1', views.button1, name='button1'),
    path('home',views.home,name='home'),
    path('home1', views.home1, name='home1'),
    path('fetchname',views.fetchname,name='fetchname'),
    path('submi',views.submi),
    path('addData',views.addData,name='addData'),
    path('updateData/<int:u_id>',views.updateData,name='updateData'),
    path('update_form',views.update_form,name='update_form'),
    path('deleteData/<int:id>',views.deleteData,name='deleteData'),
    path('view/<int:u_id>',views.view,name='view'),
    
    
    # path('search',views.search,name='search'),
   
    
    
    

]