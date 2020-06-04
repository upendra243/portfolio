from django.urls import path, re_path
from django.conf.urls import url

from api import views

urlpatterns = [
    path('', views.api_root, name="api-root"),
    path('skills/', views.skill_list),
    path('skills/<int:pk>/', views.skill_detail),
    path('v2/skills/', views.SkillList.as_view(), name="skill-list-v2"),
    path('v2/skills/<int:pk>/', views.SkillDetail.as_view(), name='skill-detail-v2')
]

