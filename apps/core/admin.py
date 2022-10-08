from django.contrib import admin

from .models import Country, Genre, Director, Movie, Actor, Song


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "year",
        "rating",
        "global_ranking",
        "length",
        "revenue",
        "genre",
        "country",
        "director",
    )
    list_filter = ("genre", "country", "director")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age")
    raw_id_fields = ("movies",)
    search_fields = ("name",)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "movie", "length")
    list_filter = ("movie",)
