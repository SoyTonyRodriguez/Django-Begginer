from django.db import models

# Create your models here.


# In this file, the model is like the table's name on the database
class Project(models.Model):
    # In this file, we have been created the fields of the table
    name = models.CharField(max_length=200)

    # This method is used to define a human-readable string representation of an instance of the class
    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    # TextField is like the long text
    description = models.TextField()
    # This field is related with the prject model
    # on_delete=models.CASCADE means that when a data is delete, the rest
    # that has related to it will also be deleted
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + " - " + self.project.name
