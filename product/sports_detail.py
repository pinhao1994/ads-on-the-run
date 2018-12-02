import pandas as pd

def filter1(zipcode, i, j):

	df3 = pd.read_csv('csv_for_filtering_sports_1.csv', index_col = 'Detailed Activity')
	df4 = pd.read_csv('sport_vs_age.csv', index_col = 'Unnamed: 0')

	df_with_score = pd.DataFrame(df3.values*df4.loc[zipcode].values, columns=df3.columns, index=df3.index)
	df_with_score['score'] = df_with_score.sum(axis=1)
	df_with_score1 = df_with_score.sort_values('score', ascending=False)
	rank_list = df_with_score1.index.tolist()
	return rank_list[i:j]