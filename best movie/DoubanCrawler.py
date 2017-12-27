"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = "https://movie.douban.com/tag/#/?tags="
	url += ",".join([category, location])
	return url

print(getMovieUrl("剧情","大陆"))	