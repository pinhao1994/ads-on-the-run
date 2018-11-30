import json
import os
import pandas as pd

from api.const import MODELS_PATH, ERROR
from django.http import HttpResponse


def index(request, zip_code):
    """ ``GET http://<domain>/sports/<zip_code>``

    :param request: HTTP GET Request
    :type request: requests
    :param zip_code: zip code in NYC
    :type zip_code: str

    :return: list of sports products
    :rtype: list[str]
    """
    validation = pd.read_csv(os.path.join(MODELS_PATH, 'zip_vs_age.csv'),
                             index_col='Unnamed: 0').index
    if int(zip_code) not in validation:
        return HttpResponse(ERROR)

    zip_codes = sports_detail(int(zip_code), 0, 5)
    return HttpResponse(json.dumps({"input": zip_code,
                                    "val": zip_codes}))


def sports_detail(zip_code, i, j):
    report_path = os.path.join(MODELS_PATH, 'report.csv')
    zc_path = os.path.join(MODELS_PATH, 'zip_vs_age.csv')

    report = pd.read_csv(report_path, index_col='Detailed Activity')
    df_zc = pd.read_csv(zc_path, index_col='Unnamed: 0')

    df_with_score = pd.DataFrame(report.values * df_zc.loc[zip_code, :].values,
                                 columns=report.columns, index=report.index)
    df_with_score['score'] = df_with_score.sum(axis=1)
    df_with_score1 = df_with_score.sort_values('score', ascending=False)
    rank_list = df_with_score1.index.tolist()
    return rank_list[i:j] if j-i < len(rank_list) else rank_list













