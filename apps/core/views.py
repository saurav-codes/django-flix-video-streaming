# python specific imports
import operator
from functools import reduce

# django imports
from django.db.models import Q

# 3rd party imports
from haystack.query import SearchQuerySet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

# local imports
from .models import Movie
from .serializers import MovieHayStackSerializer


class SearchViewElk(APIView, LimitOffsetPagination):

    default_limit = 10
    serializer_class = MovieHayStackSerializer

    def get(self, request):

        # get the query params
        query = request.GET.get("q", None)
        highlight = request.GET.get("highlight", None)
        facets = request.GET.get("facets", None)

        # prepare a initial elk SearchQuerySet from Movie Model
        sqs = SearchQuerySet().models(Movie)

        if query:
            query_list = query.split(" ")  # split the query string
            qs_item = reduce(
                operator.and_, (Q(text__contains=item) for item in query_list)
            )  # filter by every item in query_list - ( using OR filter)
            sqs = sqs.filter(qs_item)

            if highlight:
                # if any value is passed to highlight then highlight the query
                sqs = sqs.highlight()

        if facets:
            sqs = self.filter_sqs_by_facets(sqs, facets)

        page = self.paginate_queryset(sqs, request, view=self)
        movie_serializer = self.serializer_class(
            page, many=True, context={"request": request}
        )
        facets = self.get_facet_fields(sqs)
        summary = self.prepare_summary(sqs)
        data = {"movies": movie_serializer.data, "facets": facets, "summary": summary}
        return Response(data, status=HTTP_200_OK)

    def filter_sqs_by_facets(self, sqs, facets):
        facet_list = facets.split(",")
        for facet in facet_list:
            facet_key, facet_value = facet.split(":")
            # narrow down the results by facet
            sqs = sqs.narrow(f"{facet_key}:{facet_value}")
        return sqs

    def get_facet_fields(self, sqs):
        # return all the possible facet fields from given SQS
        facet_fields = (
            sqs.facet("year")
            .facet("rating")
            .facet("global_ranking")
            .facet("length")
            .facet("revenue")
            .facet("country")
            .facet("genre")
        )
        return facet_fields.facet_counts()

    def prepare_summary(self, sqs):
        # return the summary of the search results
        summary = {
            "total": sqs.count(),
            "next_page": self.get_next_link(),
            "previous_page": self.get_previous_link(),
        }
        return summary
