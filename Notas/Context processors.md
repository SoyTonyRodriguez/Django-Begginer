# Context processors

In Django, context processors are Python functions used to add specific data to the template context globally. 
These context processors run each time a template is rendered, making additional data available in all templates without 
the need to explicitly pass it from each view. Context processors are particularly useful for providing common data such as the current 
user's information, navigation menus, or application settings to all templates.

To create and use a context processor in Django, follow these steps:

## Define the Context Processor

Create a Python function that will act as a context processor. This function must accept a request as an argument and return a 
dictionary of data that you want to add to the template context.

```py
def mi_procesador_de_contexto(request):
    # Lógica para obtener datos del contexto
    datos = {
        'nombre_de_usuario': request.user.username,
        'menu_principal': obtener_menu_principal(),
    }
    return datos
```

## Register the Context Processor

In your settings.py configuration file, add the context processor to the context_processors list. 
This ensures that the context processor is executed on each request

```py
TEMPLATES = [
    {
        # ...
        'OPTIONS': {
            'context_processors': [
                # ...
                'mi_app.context_processors.mi_procesador_de_contexto',
            ],
        },
    },
]
```

## Using Data in Templates

The data provided by the context processor is now available in all your templates. 
You can access this data using the variables in the templates.

```html
<p>Bienvenido, {{ nombre_de_usuario }}</p>
<ul>
    {% for item in menu_principal %}
        <li><a href="{{ item.url }}">{{ item.label }}</a></li>
    {% endfor %}
</ul>
```
