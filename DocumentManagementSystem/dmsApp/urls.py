from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    path('hello/', views.say_hello),
    path('homepage/', views.home_page),
    path('getDoc/', views.get_documents),
    path('submitDoc/', views.add_docs_to_list),
    path('removeDoc/', views.remove_docs),
    path('updateDoc/', views.update_single_doc)
]
