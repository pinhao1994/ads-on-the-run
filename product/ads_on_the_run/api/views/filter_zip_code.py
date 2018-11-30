import json
import pandas as pd
import os

from api.const import AGE_RANGE, INCOME_LEVEL, AMENITY, ERROR, MODELS_PATH
from django.http import HttpResponse


def index(request, age_range, income, amenity):
    """``GET http://<domain>/filter/<age_range>/<income>/<amenity>``

    :param request: HTTP GET Request
    :type request: requests
    :param age_range: age range
    :type age_range: int
    :param income: income level
    :type income: int
    :param amenity: amenity type
    :type amenity: int
    :return: list of ranked zip codes
    :rtype: list[str]
    """
    if age_range not in AGE_RANGE.keys() or income not in INCOME_LEVEL.keys() \
            or amenity not in AMENITY.keys():
        return HttpResponse(ERROR)

    top5_cands = filter_zip_code(AGE_RANGE[age_range], INCOME_LEVEL[income], AMENITY[amenity], top_n=5)
    return HttpResponse(json.dumps({"input": [AGE_RANGE[age_range], INCOME_LEVEL[income], AMENITY[amenity]],
                                    "val": top5_cands}))


def filter_zip_code(age, wealth, product, top_n):
    csv_path = os.path.join(MODELS_PATH, 'csv_for_filtering.csv')
    df = pd.read_csv(csv_path, index_col='Unnamed: 0')

    df1 = df.copy()
    df1['score'] = (df[age] + df[wealth] + df[product]) / 3
    df1 = df1.sort_values('score', ascending=False)
    rank_list = df1.index.tolist()
    return rank_list[:top_n] if top_n < len(rank_list) else rank_list
