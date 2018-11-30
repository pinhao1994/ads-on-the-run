import pandas as pd
from shapely.geometry import Point, LineString
import geopandas
import polyline

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