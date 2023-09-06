from django import forms


# To create a new form
class Create_NewTask(forms.Form):
    title = forms.CharField(
        label="Titulo de tarea",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
    description = forms.CharField(
        label="Descripcion de la tarea", widget=forms.Textarea(attrs={"class": "input"})
    )


class Create_NewProject(forms.Form):
    name = forms.CharField(
        label="Nombre del proyecto",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
