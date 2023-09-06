# URL names

In Django, URL names are used to uniquely identify and reference URLs within your web application. They play
a crucial role in URL routing and reverse URL resolution. Naming your URLs makes it easier to change the URL
structure of your application without affecting the code that references those URLs.

## Defining URL patterns

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("hello/<str:username>", views.hello, name="hello"),
    path("projects/", views.projects, name="projects"),
    path("tasks/", views.tasks, name="tasks"),
    path("create_task/", views.create_Task, name="create_task"),
    path("create_project/", views.create_Project, name="create_project"),
]
```

## Referencing URLs in Templates

```html
<nav>
    <ul>
        <li>
            <a href="{% url 'index' %}">Home</a>
        </li>
        <li>
            <a href="{% url 'projects' %}">Projects</a>
        </li>
        <li>
            <a href="{% url 'tasks' %}">Tasks</a>
        </li>
        <li>
            <a href="{% url 'about' %}">About</a>
        </li>
        <li>
            <a href="{% url 'create_task' %}">New Task</a>
        </li>
        <li>
            <a href="{% url 'create_project' %}">Create Project</a>
        </li>
    </ul>
</nav>
```

### Redirect URL

```python
def create_Project(request):
    if request.method == "GET":
        return render(
            request, "projects/create_project.html", {"form": Create_NewProject()}
        )
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect("projects")
```
