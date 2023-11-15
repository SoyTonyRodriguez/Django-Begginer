# Mixin

In Django, a mixin is a way to reuse a particular set of functionalities in multiple classes. Mixins are commonly used in class-based views (CBVs) to
share and extend behavior across different views without the need for multiple inheritance.

Here are the key characteristics and use cases of mixins in Django:

## Composition over Inheritance

Django encourages the use of composition over multiple inheritance. Instead of creating complex class hierarchies, you can compose classes with different functionalities using mixins.

## Composition over Inheritance

Django encourages the use of composition over multiple inheritance. Instead of creating complex class hierarchies, you can compose classes with different functionalities using mixins.

## Reusable Functionality

A mixin is a class that provides specific functionality or behavior. This behavior can be reused by incorporating the mixin into other classes.

## No Standalone Use:

Mixins are not intended to be used as standalone classes. They are meant to be mixed in with other classes that inherit from Django's built-in views or other base classes.

## Order of Inheritance Matters

The order in which mixins are inherited is significant. If two mixins or classes provide the same method or attribute, the method or attribute from the class appearing first in 
the inheritance chain takes precedence.

## Example

### Mixin declaration

```python
class StaffRequiredMixin(object):
    # Este mixin requerirá que el usuario sea miembro del staff
    def dispatch(self, request, *args: Any, **kwargs: Any):
        # si no estamos logueados nos mandara a la pagina de login
        if not request.user.is_staff:
            return redirect(reverse("admin:login"))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
```

### Mixin implementation

```python
# Dando prioridad al mixin
class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
```

Mixins are a flexible and powerful way to share and extend functionality in Django. They contribute to a more modular and maintainable codebase by allowing you 
to compose classes with the specific behavior you need for each view.




