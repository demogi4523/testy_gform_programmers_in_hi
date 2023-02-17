def find_athlets(know_english, sportsmen, more_than_20_years):
	return list(set(know_english) & set(sportsmen) & set(more_than_20_years))
