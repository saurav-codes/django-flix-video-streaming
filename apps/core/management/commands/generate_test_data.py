from django.core.management.base import BaseCommand

from ...factories import CountryFactory, DirectorFactory, GenreFactory, MovieFactory


class Command(BaseCommand):

    help = "Generate Random Data for Dflix DB"
    batch_size = 10000

    def add_arguments(self, parser):
        parser.add_argument(
            "no_of_movies", type=int, help="no of movies to generate in database"
        )

    def handle(self, *args, **options):

        print("preparing for creating movies ⚙️")
        CountryFactory.create_batch(100)
        print("created 100 countries ✅")
        GenreFactory.create_batch(21)
        print("created 21 genres ✅")
        DirectorFactory.create_batch(30)
        print("created 30 directors ✅")
        no_of_movies = options["no_of_movies"]

        # create movies in batches of given size
        print(f"creating movies in batches of {self.batch_size}")
        for i in range(0, no_of_movies, self.batch_size):
            MovieFactory.create_batch(self.batch_size)
            print(f"created {i+self.batch_size} movies ✅")
        print(f"successfully created {no_of_movies} movies ✅")
