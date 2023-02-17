from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, LessonCreateView, LessonDeleteView, \
    LessonListView, LessonDetailView, LessonUpdateView

urlpatterns = [
    path('create/', LessonCreateView.as_view()),
    path('delete/<int:pk>/', LessonDeleteView.as_view()),
    path('', LessonListView.as_view()),
    path('detail/<int:pk>/', LessonDetailView.as_view()),
    path('update/<int:pk>/', LessonUpdateView.as_view()),

]

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns += router.urls
