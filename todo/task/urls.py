from django.urls import path
from . import views


urlpatterns = [
   path('sigunp', views.signup,name='signup'),
   path('login',views.login,name='login'),
   path('task',views.task,name='task'),
   path('edit<int:id>',views.edit,name='edit'),
   path('display',views.display,name='display'),
   path('delete<int:id>',views.delete,name='delete'),
   path('finished<int:id>',views.finished,name='finished'),
   path('finishedtasks',views.finishedtasks,name='finishedtasks'),
   path('inprogress<int:id>',views.inprogress,name='inprogress'),
   path('search',views.search,name='search'),
   path('due',views.due,name='due'),
   path('signout',views.signout,name='signout'),
   path('',views.home,name='home')

]