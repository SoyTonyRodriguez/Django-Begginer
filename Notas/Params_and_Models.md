# Params and Models

We can use the params and models together
This is an example of use:

We import our models, and the modulo for error 404
And create our views with this models

```py
from .models import Project, Task
from django.shortcuts import get_object_or_404


def projects(request):
    projects = list(Project.objects.values())
    # The JsonResponse is to show all values, in a correct format to the web
    return JsonResponse(projects, safe=False)


def tasks(request, id):
    # get_object_or_404 is to get error 404 if it is not found
    task = get_object_or_404(Task, id=id)
    return HttpResponse("task: %s" % task.title)
```

And now we create our urls to this views

```py
from django.urls import path

urlpatterns = [
    path("projects/", views.projects),
    path("tasks/<int:id>", views.tasks),
]
```

Now, when you go to the url projects/ you can see all records in a json form

![url projects](./img/url%20projects%20params.png)

When you go to the url task/<int:id> you can see the name's task related with this id

![url task](./img/url%20task%20params.png)
