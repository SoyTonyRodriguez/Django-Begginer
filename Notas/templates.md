# Templates

In Django, templates are a fundamental component of the framework that allow you to separate the presentation
layer (HTML code) from the Python code that handles business logic, usually there are located in a folder
called **templates**. Templates enable you to generate dynamic HTML content by inserting data from your Python
views into pre-defined HTML templates.

Templates in Django are typically HTML files with placeholders for dynamic content. These placeholders are enclosed
in double curly braces, like ***{{ variable_name }}***, and can also include template tags and filters for more
complex logic.

## Example

Here's a simple Django template example:

In the views file you can put this:

``` python
def index(request):
    title = "Django Course"
    return render(request, "index.html", {"title": title})
```

Now in the html file you can do this:

```html
<h1>{{title}}</h1>

<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis, aliquam id harum nulla, unde illum numquam ab
    porro nihil odio dolore sunt totam nobis reprehenderit corrupti soluta ad veritatis dignissimos?</p>
```

The result should be a website that displays the content of the variable as header 1 text.
