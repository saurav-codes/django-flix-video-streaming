# 3rd party imports
from drf_haystack.serializers import HaystackSerializer

# local imports
from .search_indexes import MovieIndex


class MovieHayStackSerializer(HaystackSerializer):
    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [MovieIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
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
        ]

    def __init__(self, *args, **kwargs):
        super(MovieHayStackSerializer, self).__init__(*args, **kwargs)
        # get the query params
        fields_in_url_params = self.context["request"].GET.get("fields", None)
        if fields_in_url_params:
            # split the params from comma to make a list
            fields_in_url_parmas_list = fields_in_url_params.split(",")
            existing_fields = set(self.fields)  # -> keys of all fields

            # get all the fields which are not in params but declared in meta class above
            # our_fields = {'title', 'description', 'year', '....'}
            # fields_from_urls = {'title', 'year'}
            # operation = our_fields - fields_from_url => {'description', '.....'}
            fields_to_remove = existing_fields - set(fields_in_url_parmas_list)

            # now since we have fields 
            for field in fields_to_remove:
                self.fields.pop(field)  # remove this field
