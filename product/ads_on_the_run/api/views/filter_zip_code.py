import json

from api.const import AGE_RANGE, INCOME_LEVEL, AMENITY, ERROR
from django.http import HttpResponse


def index(request, age_range, income, amenity):
    if age_range not in AGE_RANGE.keys() or income not in INCOME_LEVEL.keys() \
            or amenity not in AMENITY.keys():
        return HttpResponse(ERROR)

    # todo: top-k zip code
    # top5_cands = func(AGE_RANGE[age_range], INCOME_LEVEL[income], AMENITY[amenity], k=5)
    top5_cands = ['10027', '10029']
    return HttpResponse(json.dumps({"val": top5_cands}))