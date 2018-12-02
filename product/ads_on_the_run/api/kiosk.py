import polyline
import os
import pandas as pd

from api.const import MODELS_PATH
from shapely.geometry import Point, LineString


def kiosk_distance(kiosk):
    path = os.path.join(MODELS_PATH, 'NYC_Strava.csv')
    strava = pd.read_csv(path)
    seg_list_poly = strava['map_polyline'].values.tolist()
    seg_list_gpd = list(map(lambda x: LineString(polyline.decode(x)), seg_list_poly))

    return min(list(map(lambda x: x.distance(kiosk), seg_list_gpd)))


def rank_kiosk(zip_code):
    path = os.path.join(MODELS_PATH, 'LinkNYC_Kiosk_Status.csv')
    kiosk = pd.read_csv(path, index_col="SITE ID")

    if zip_code not in kiosk['ZIP'].tolist():
        return []

    kiosk = kiosk.loc[kiosk['ZIP'] == zip_code]
    kiosk['lat_lon'] = list(zip(kiosk['LATITUDE'], kiosk['LONGITUDE']))
    kiosk['Point'] = list(map(Point, list(zip(kiosk['LONGITUDE'], kiosk['LATITUDE']))))
    kiosk['Distance'] = kiosk.apply(lambda row: kiosk_distance(row['Point']), axis=1)
    kiosk = kiosk.sort_values('Distance')
    kiosk_lat_lon_list = kiosk['lat_lon'].tolist()
    return kiosk_lat_lon_list

