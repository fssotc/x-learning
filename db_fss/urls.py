from django.conf.urls import url
from .views import StudentList, StudentDetail,ProfList

urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^student/$', StudentList.as_view(), name='student_list'),
    url(r'^student/(?P<pk>[0-9]+)$', StudentDetail.as_view(), name='student_detail'),
    url(r'^prof/$', ProfList.as_view(), name='prof_list'),
]
