from django.urls import path
import edu.views as view
urlpatterns = [
    path('',view.home,name='homepage'),
    path('about/',view.about,name='aboutpage'),
    path('student',view.studentlist,name='studentlist')
    
]



# from .views import member

# path('member/', views.member, name='getmember')