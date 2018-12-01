import json

from api.const import AGE_RANGE, INCOME_LEVEL, AMENITY
from django.http import HttpResponse


def index(request):
    """ ``GET http://<domain>/api/``

    List all the selection options for frontend design.

    :param request: HTTP GET Request
    :type request: requests
    :return: dictionary of selection
    :rtype: dict[dict]
    """
    data = {
        "title": "This is Ads On The Run API!",
        "selections": {
            "age": AGE_RANGE,
            "income": INCOME_LEVEL,
            "amenity": AMENITY,
        }
    }
    return HttpResponse(json.dumps(data))
