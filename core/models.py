
from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254,unique=True)
    password=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.first_name+' '+ self.last_name

class Movie(models.Model):

    movie_types=(
        ('Adventure','Adventure'),
        ('Comedy','Comedy'),
        ('Drama','Drama'),
        ('Horror','Horror'),
        ('Science fiction','Science fiction')
    )
    status_choice=(
    ('private','private'),
    ('public','public')
    )
    user=models.ForeignKey(Registration, null=True,default=1,on_delete=models.CASCADE)
    Title=models.CharField(max_length=600)
    Year=models.DateField()
    imdbID=models.CharField(max_length=200)
    Type=models.CharField(max_length=200,choices=movie_types)
    Poster=models.CharField(max_length=1000)
    Status=models.CharField(max_length=100,choices=status_choice)

    def __str__(self) -> str:
        return self.Title
