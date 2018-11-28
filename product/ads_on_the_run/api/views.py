import pickle
import json
import numpy as np

from api.const import AGE_RANGE, INCOME_LEVEL, AMENITY, ERROR
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is Ads On The Run API!")


def top_zip_code(request, age_range, income, amenity):
    if age_range not in AGE_RANGE.keys() or income not in INCOME_LEVEL.keys() \
            or amenity not in AMENITY.keys():
        return HttpResponse(ERROR)

    # todo: top-k zip code
    # top5_cands = func(AGE_RANGE[age_range], INCOME_LEVEL[income], AMENITY[amenity], k=5)
    top5_cands = ['10027', '10029']
    return HttpResponse(json.dumps({"val": top5_cands}))


def same_cluster(request, zip_code):
    # todo: import the final model in the directory
    clusters = pickle.load(open("clusters.pkl", "rb"))
    
    for c in clusters:
        if zip_code in c:
            return HttpResponse(json.dumps({"same_clusters": list(set(c) ^ {zip_code})}))
    return HttpResponse(ERROR)


def find_segment_kiosk(request, zip_code):
    return HttpResponse("long lat of the kiosk")


def sports_detail(request, zip_code):
    # todo: zip code to age distribution
    # todo: age distribution to report to specific product
    return HttpResponse("specific product")


def get_const_code(request):
    data = {
        "age": AGE_RANGE,
        "income": INCOME_LEVEL,
        "amenity": AMENITY,
    }
    return HttpResponse(json.dumps(data))











