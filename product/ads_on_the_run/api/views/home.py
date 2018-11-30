import json

from api.const import AGE_RANGE, INCOME_LEVEL, AMENITY
from django.http import HttpResponse


def index(request):
    data = {
        "title": "This is Ads On The Run API!",
        "selections": {
            "age": AGE_RANGE,
            "income": INCOME_LEVEL,
            "amenity": AMENITY,
        }
    }
    return HttpResponse(json.dumps(data))