import pickle
import json

from django.http import HttpResponse


def index(request, zip_code):
    # todo: import the final model in the directory
    clusters = pickle.load(open("clusters.pkl", "rb"))

    cands = set()
    for c in clusters:
        if zip_code in c:
            cands = set(c) - {zip_code}
            break
    cands = list(cands)

    # todo: cluster + segements + kiosk
    # todo levenshtein algo, geopanda to calculate the distance
    # todo find the top-k best kiosk location, return me a list of (long, lat)

    return HttpResponse(json.dumps({'vals': [['long1', 'lat1'],
                                             ['long2', 'lat2']]}))
