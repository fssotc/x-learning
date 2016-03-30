from django.conf.urls import url
from .views import StudentList, StudentDetail, ProfList ,home


urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^student/$',StudentList.as_view(),name='StudentList'),
    url(r'^student/(?P<pk>[0-9]+)$', StudentDetail.as_view(), name='student_detail'),
    url(r'^prof/$',ProfList.as_view(),name='ProfList'),
]
