from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import notes.views as views

urlpatterns = [
    path('notes/', views.NotesList.as_view()),
    path('note/<int:pk>/', views.NoteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
