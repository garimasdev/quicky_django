from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('book_now/', views.contact_submit, name='book_now'),
]
