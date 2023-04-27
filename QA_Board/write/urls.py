from django.urls import path, include
from write import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", views.question_list), # address:8080/question/
    path("form/", views.question_form), # address:8080/question/form
    path("delete/<int:id>", views.question_delete, name="question_delete"),
]
