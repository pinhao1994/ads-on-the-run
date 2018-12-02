import json
import os
import pandas as pd

from api.kiosk import rank_kiosk
from api.const import MODELS_PATH, ERROR
from django.http import HttpResponse


def index(request, zip_code):
    """ ``GET http://<domain>/api/kiosk/<zip_code>``

    Given a zip code, find other similar zip codes within the same k-means clusters. For these zip codes, rank kiosks based on their distances from
    Strava segments. Return this ranked list of kiosks as suitable locations for advertisements.

    :param request: HTTP GET Request
    :type request: requests
    :param zip_code: zip code
    :type zip_code: str
    :return: same cluster zip codes and the closest kiosks latitude and longitude to Strava segments
    :rtype: dict[list]
    """

    validation = pd.read_csv(os.path.join(MODELS_PATH, 'zip_vs_age.csv'),
                             index_col='Unnamed: 0').index
    if int(zip_code) not in validation:
        return HttpResponse(ERROR)

    clusters_zip_code = pd.read_pickle(os.path.join(MODELS_PATH, 'cluster_zip_code_final.pkl'))

    candidate_zip_code = set()
    for _, c in clusters_zip_code.items():
        if int(zip_code) in c:
            candidate_zip_code = set(c) - {int(zip_code)}
            break
    candidate_zip_code = list(candidate_zip_code)

    kiosks = list()
    for zc in candidate_zip_code:
        kiosks.extend(rank_kiosk(zc)[:3])

    return HttpResponse(json.dumps({"zip_code": zip_code,
                                    "same_cluster_zip_code": candidate_zip_code,
                                    "kiosk_lat_lon": kiosks}))



