from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import Create_NewTask, Create_NewProject


# Create your views here.
def index(request):
    title = "Django Course"
    # use a dictionary to pass variables or data
    return render(request, "index.html", {"title": title})


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def about(request):
    username = "TONY"
    return render(request, "about.html", {"username": username})


def projects(request):
    # projects = list(Project.objects.values())
    # The JsonResponse is to show all values, in a correct format to the web
    # return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})


def tasks(request):
    # def tasks(request, id): old definition with id parameter
    # get_object_or_404 is to get error 404 if it is not found
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("task: %s" % task.title)

    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": tasks})


def create_Task(request):
    # To show by console the input sent by user
    # print(request.GET["title"])
    # print(request.GET["description"])
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": Create_NewTask()})
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        return redirect("tasks")


def create_Project(request):
    if request.method == "GET":
        return render(
            request, "projects/create_project.html", {"form": Create_NewProject()}
        )
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect("projects")


# The parameter, id_Parameter must have the same name as in the urls.py file
def project_Detail(request, id_Parameter):
    project = get_object_or_404(Project, id=id_Parameter)
    tasks = Task.objects.filter(project_id=id_Parameter)
    return render(request, "projects/detail.html", {"project": project, "tasks": tasks})
