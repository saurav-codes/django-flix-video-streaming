from django.db import models

# Model Structure for our Movie Database


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    rating = models.FloatField()
    global_ranking = models.IntegerField()
    length = models.CharField(max_length=50)
    revenue = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    length = models.CharField(max_length=50)

    def __str__(self):
        return self.title
