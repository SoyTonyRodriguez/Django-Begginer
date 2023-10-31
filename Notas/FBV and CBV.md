# FBV and CBV

In Django, "FBV" and "CBV" stand for Function-Based Views and Class-Based Views, which are two different approaches to defining views in web applications. 
They have different syntax and structures, each with its own advantages and use cases.

## Function-Based Views (FBV)

* Approach: FBV is the traditional way of defining views in Django. It involves defining view functions as Python functions. Each function represents a view and takes an HttpRequest object as an argument.
* Flexibility: FBVs are highly flexible and allow you to write custom view logic for each view by defining a function. They are ideal for simple views and scenarios where you need fine-grained control over the request and response.

### Example

```python
Copy code
from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    # View logic here
    return render(request, 'template.html', context_data)
```

## Class-Based Views (CBV)

* Approach: CBV is a more recent approach to defining views in Django, introduced to provide a more organized and reusable way to define views. Views are defined as classes, and each class provides methods that handle different HTTP methods (e.g., get(), post()) or actions.
* Reusability: CBVs promote reusability because you can extend and customize existing generic class-based views. Django provides many built-in generic views for common tasks, such as creating, updating, and deleting objects.

### Example
```py
from django.shortcuts import render
from django.http import HttpRequest

# Importar TemplateView para CBV
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"

    # Como sobreescribir el diccionario de contexto con CBV
    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, self.template_name, {"title": "Mi super web playground"})
```

How to reference CBV from a URL file

```py
from django.urls import path
from .views import HomePageView, SamplePageView

# Nueva forma de colocar las URL's con CBV
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
```

## Choosing Between FBV and CBV

The choice between FBV and CBV depends on the specific requirements of your project:

* FBV is a good choice when you need fine-grained control over view logic, especially for simple views. It's easier to get started with and can be more straightforward for small, custom views.
* CBV is suitable for more complex applications where you want to reuse and extend common view patterns. It helps maintain a clean and organized codebase. Django provides a wide range of generic class-based views to streamline common tasks.
