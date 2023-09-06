from django.urls import path

# The period (.) that we import something from located in the directory of the current file
from . import views

urlpatterns = [
    # '' Significa la ruta principal, es decir la pagina de inicio,,
    path("", views.index, name="index"),
    # Cuando en el link pongamos /about se vera este view
    path("about/", views.about, name="about"),
    path("hello/<str:username>", views.hello, name="hello"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:id_Parameter>", views.project_Detail, name="projects_detail"),
    path("tasks/", views.tasks, name="tasks"),
    path("create_task/", views.create_Task, name="create_task"),
    path("create_a_project/", views.create_Project, name="create_project"),
]
