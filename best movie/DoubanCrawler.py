import expanddouban


class Movie:
	pass
	def __init__(self, name, rate, location, category, info_link, cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link	


name = "肖申克的救赎"
rate = 9.6
location = "美国"
category = "剧情"
info_link = "https://movie.douban.com/subject/1292052/"
cover_link = "https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg"

m = Movie(name, rate, location, category, info_link, cover_link)

#print(m.cover_link)

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = "https://movie.douban.com/tag/#/?tags="
	url += ",".join([category, location])
	return url

#print(getMovieUrl("剧情","大陆"))	
url = getMovieUrl("剧情","大陆")
#html = expanddouban.getHtml(url)

#print(html)
