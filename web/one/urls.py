from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('blog/',views.blog,name='post-list'),
    path('search/',views.search, name='search'),
    path('searchInterviews/',views.searchInterviews, name='searchInterviews'),
    path('post/<id>/',views.post,name='post-detail'),
    path('interviews/<id>/',views.interviews,name='interviews-detail'),
    path('interview-form/',views.interview_form, name='interview_form'),
    path('interview-experience/',views.interview_experience, name='interview_experience')
]