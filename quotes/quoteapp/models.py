from django.db import models


# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.tag}"


class Author(models.Model):
    fullname = models.CharField(max_length=25, null=False, unique=True)
    born_date = models.CharField(null=False)
    born_location = models.CharField(null=False)
    description = models.CharField(null=False)

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    quote = models.TextField(unique=True, null=False)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quote}'


