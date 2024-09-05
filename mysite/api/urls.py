from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-view-create"),
    path("notes/<int:pk>/", views.NoteRetrieveUpdateDestroy.as_view(), name="note-update-destroy"),
    path("notes/query/", views.NoteList.as_view(), name="note-query"),
]
