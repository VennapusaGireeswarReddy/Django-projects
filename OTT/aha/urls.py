from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('movies/',views.movies,name='movies'),
    path('series/',views.series,name='series'),
    path('devara/<int:id>',views.devara,name='devara'),
    path('display/<int:id>',views.display,name="display"),
    path('signout/',views.signout,name='signout'),
    # path('salaar',views.salaar,name='salaar'),
    # path('ambajipeta',views.ambajipeta,name='ambajipeta'),
    # path('baby',views.baby,name='baby'),
    # path('12thfali',views.fail_12th,name='fail_2th'),
    # path('irugapatru',views.irugapatru,name='irugapatru'),
    path('upload/',views.upload,name='upload'),
    path('uploadd/',views.uploadd,name='uploadd'),
    # path('Download/<int:id>',views.download,name='download')
] 