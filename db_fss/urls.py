from django.conf.urls import url
from .views import StudentList, StudentDetail, ProfList, ProfDetail, home, MatiereList

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^student/$', StudentList.as_view(), name='StudentList'),
    url(r'^student/(?P<pk>[0-9]+)$', StudentDetail.as_view(), name='student_detail'),
    url(r'^prof/$', ProfList.as_view(), name='prof_list'),
    url(r'^prof/(?P<pk>[0-9]+)$', ProfDetail.as_view(), name='prof_detail'),
    url(r'^matiere/$', MatiereList.as_view(), name='matiere_list'),
]
