# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#    path('course/', views.CourseList.as_view(), name="course"),
#    path('course/<int:pk>' , views.CourseDetailView.as_view() , name ='course-detail'),
#    path('course/<int:pk>/update/', views.CourseDetailView.as_view() , name ='course-update'),
#    path('course/<int:pk>/delete/' , views.CourseDetailView.as_view() , name ='course-delete'),
#    path('module/', views.ModuleList.as_view(), name="module"),
#    path('scholarships/',views.ScholarshipListCreateView.as_view(),name='scholarships'),
#    path('scholarships/<int:pk>',views.ScholarshipDetailView.as_view , name= 'detail_scholarship' ), 
#    path('scholarships/<int:pk>/update/' , views.ScholarshipDetailView.as_view() , name ='scholarship-update'),
#    path('scholarships/<int:pk>/delete/' , views.ScholarshipDetailView.as_view() , name ='scholarship-delete'),

# #
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authentication.views import ModuleViewSet, CourseViewSet , ScholarshipViewSet

router = DefaultRouter()
router.register(r'modules', ModuleViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'scholarships', ScholarshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('courses/<int:pk>/', CourseViewSet.as_view({
       'get':'retrieve', # Retrieve course
       'put':'update', #update the course
       'patch': 'partial_update', #Partial update of course (only fields passed in request are
       'delete':'destroy' # Delete Course
    }))
]