from .models import Country, Genre, Director, Movie

import factory


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Faker("country")


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker("word")


class DirectorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Director

    name = factory.Faker("name")


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("text")
    year = factory.Faker("year")
    rating = factory.Faker("pyfloat", left_digits=2, right_digits=1, positive=True)
    global_ranking = factory.Faker("pyint", min_value=0, max_value=1000)
    length = factory.Faker("time")
    revenue = factory.Faker("pyfloat", left_digits=3, right_digits=1, positive=True)
    genre = factory.SubFactory(GenreFactory)
    country = factory.SubFactory(CountryFactory)
    director = factory.SubFactory(DirectorFactory)
