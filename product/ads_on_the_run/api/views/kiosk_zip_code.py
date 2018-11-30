import pickle
import json
import pandas as pd
from shapely.geometry import Point, LineString
import polyline

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


def kiosk_distance(kiosk):
	strava = pd.read_csv('../data-collect/NYC_Strava.csv')
	seg_list_poly = strava['map_polyline'].values.tolist()
	seg_list_gpd = list(map(lambda x: LineString(polyline.decode(x)), seg_list_poly))

	return min(list(map(lambda x: x.distance(kiosk), seg_list_gpd)))


def rank_kiosk(zipcode):
	kiosk = pd.read_csv('../data-collect/LinkNYC_Kiosk_Status.csv', index_col="SITE ID")

	kiosk = kiosk.loc[kiosk['ZIP'] == zipcode]
	kiosk['lat_lon'] = list(zip(kiosk['LATITUDE'], kiosk['LONGITUDE']))
	kiosk['Point'] = list(map(Point, list(zip(kiosk['LONGITUDE'], kiosk['LATITUDE']))))
	kiosk['Distance'] = kiosk.apply(lambda row: kiosk_distance(row['Point']), axis=1)
	kiosk = kiosk.sort_values('Distance')
	kiosk_lat_lon_list = kiosk['lat_lon'].tolist()
	return kiosk_lat_lon_list
