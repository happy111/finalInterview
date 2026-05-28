from rest_framework.generics import(
        CreateAPIView,
        ListAPIView,
        UpdateAPIView,
        )

from .serializers import AreaSerializer
from .models import Area


class ActiveAreaListing(ListAPIView):
    """
    Active Area Listing GET API

	    Service Usage and Description : This API is used to list active areas.
	    Authentication Required : YES

	    Response : {
	        "data" : final_data
	    }
    """

    # permission_classes = (IsAuthenticated,)
    serializer_class = AreaSerializer
    def get_queryset(self):
        queryset = Area.objects.filter(active_status=True).values('name')
        print(queryset.query)
        print(type(queryset))
        return queryset