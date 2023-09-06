# Jinja conditionals

Jinja2, a popular templating engine used in web development, supports conditional statements to control the flow
of content within templates. You can use if, elif, and else statements to create conditional logic.

## Examples

Here's how you can use conditionals in Jinja2 templates:

We add a field in model Task:

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # New boolean field
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + " - " + self.project.name
```

Next you should apply makemigration and migrations

```sh
python manage.py makemigrations
```

```sh
pyton manage.py migrate
```

### Basic 'if' statement

We can show a message when a task is not done

```html
<h1>Tasks</h1>

{% for task in tasks %}

<div>
    <h4>{{task.title}}</h4>

    {% if task.done == False %}
    <p>Tarea pendiente</p>
    {% else %}
    <p>Tarea Realizada</p>
    {% endif %}
</div>
```

### if-else Statement

```html
<h1>Tasks</h1>

{% for task in tasks %}

<div>
    <h4>{{task.title}}</h4>

    {% if task.done == False %}
    <p>Tarea pendiente</p>
    {% endif %}
</div>
```
