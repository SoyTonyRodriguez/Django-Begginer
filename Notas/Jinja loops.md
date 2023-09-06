# Jinja loops

Jinja2 is a popular templating engine used in web development, often with Python web frameworks like Flask
and Django. It provides a way to generate dynamic content in templates by using constructs like loops.

## Example

We have the projects from models of database in variable and pass to template projects

``` python
def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})
```

### Without loops

And we can display it.

``` html
<h1>Projects</h1>
<p>{{projects}}</p>
```

But the output is like this:

![without loops](./img/projects%20without%20loops.png)

### With loops

To display it using loops we can should be type something like this:

``` html
<h1>Projects</h1>

{% for project in projects %}

<h4>{{ project.name }}</h4>

{% endfor %}
```

Now the output could be like this:

![with loops](./img/projects%20with%20loops.png)

## Example 2

We can use more data from models, the next image is using tasks model

``` python
def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})
```

``` html
<h1>Tasks</h1>

{% for task in tasks %}

<div>
    <h4>{{task.title}}</h4>
    <p>{{task.description}}</p>
    <p>Project: {{task.project.name}}</p>
</div>

{% endfor %}
```

![task loop](./img/task%20loop.png)
