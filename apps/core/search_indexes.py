from haystack import indexes
from .models import Movie


class MovieIndex(indexes.SearchIndex, indexes.Indexable):
    id = indexes.IntegerField(model_attr="id")
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")
    description = indexes.CharField(model_attr="description")
    year = indexes.IntegerField(model_attr="year")
    rating = indexes.FloatField(model_attr="rating")
    global_ranking = indexes.IntegerField(model_attr="global_ranking")
    length = indexes.CharField(model_attr="length", faceted=True)
    revenue = indexes.FloatField(model_attr="revenue", faceted=True)
    genre = indexes.CharField(model_attr="genre", faceted=True)
    country = indexes.CharField(model_attr="country", faceted=True)
    director = indexes.CharField(model_attr="director", faceted=True)

    def get_model(self):
        return Movie

    def prepare_director(self, obj):
        return obj.director.name

    def prepare_genre(self, obj):
        return obj.genre.name

    def prepare_country(self, obj):
        return obj.country.name

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
