# Static Files

In Django, static files refer to files such as CSS, JavaScript, images, and other assets that are used in your
web application's front-end. These files are typically served directly by the web server (e.g., Nginx or Apache)
or through a dedicated static file server (e.g., Amazon S3, a CDN) to improve performance. Django provides a
built-in mechanism to manage and serve static files during development and deployment.

## Setting Up Your Static Files Directory

First, you need to define where your static files are located. In your Django project, create a directory named static at the top level (same level as your manage.py file) or within each app. You can organize static files by app or by purpose, depending on your project's structure.

For example, you might have a structure like this:

```bash
myproject/
├── myproject/
├── myapp/
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── ...
├── templates/
└── ...
```

## Configuring Static File Handling

In your project's settings (settings.py), make sure that you have the STATIC_URL and STATICFILES_DIRS settings
defined. STATIC_URL specifies the URL prefix for serving static files,

```py
STATIC_URL = '/static/'
```

## Using static files in templates

In your HTML templates, you can reference static files using first {% load static %} at the begining of the template
and the {% static 'path/to/your/static/file' %} template tag.

```html
{% extends 'layouts/base.html' %}

{% load static %}

{% block content %}

<h1>{{title}}</h1>

<img src="{% static 'assassins.png' %}" width="100">

<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis, aliquam id harum nulla, unde illum numquam ab
    porro nihil odio dolore sunt totam nobis reprehenderit corrupti soluta ad veritatis dignissimos?
</p>

{% endblock %}
```
