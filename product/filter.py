import pandas as pd

def filter(age, wealth, product, top_n):
	df = pd.read_csv('csv_for_filtering.csv', index_col = 'Unnamed: 0')
	df1 = df.copy()
	df1['score'] = (df[age] + df[wealth] + df[product]) / 3
	df2 = df1.sort_values('score', ascending=False)
	rank_list = df2.index.tolist()
	return rank_list[:top_n]