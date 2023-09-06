# Forms (Formularios)

In Django, forms are a fundamental part of building web applications. They provide a convenient way to handle
user input, validate data, and interact with your application's database. Django forms make it easy to create,
render, and process HTML forms while abstracting much of the underlying complexity.

Instead create a forms with html classic like this:

```html
<input type="text">

<textarea name="description" id="" cols="30" rows="10"></textarea>
```

We can do it with python. In this case I created a new file called forms.py with the next:

```python
from django import forms

# To create a new form
class Create_NewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(
        label="Descripcion de la tarea", widget=forms.Textarea
    )
```

And put it inside the html file

```html
{% extends 'layouts/base.html' %}

{% block content %}

<h1>Create a new task</h1>

<!-- show form -->
<form method="POST">

    <!-- For CSRF verification -->
    {% csrf_token %}
    <!-- as_p: To each field should be in a <p></p> tag -->
    {{ form.as_p }}

    <button>
        Save
    </button>
</form>

{% endblock %}
```

And in the views file:

```python
def create_Task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": Create_NewTask()})
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        return redirect("/tasks/")
```

And we created a new task using our own form
