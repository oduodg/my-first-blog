from django.urls import path
from . import views

urlpatterns = [ # URL 패턴 추가
    path('',views.post_list, name='post_list'), 
    # post_list 라는 view가 루트 URL에 할당됨.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]