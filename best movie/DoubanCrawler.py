import expanddouban
from bs4 import BeautifulSoup
import csv

"""
Task 1
Return a string corresponding to the URL of douban movie lists given category and location.
Support rate range since it is called by task 5 
"""
def getMovieUrl(category, location, rate_range=None):
	url = "https://movie.douban.com/tag/#/?tags="
	
	url += ",".join([category, location])
	
	if rate_range:
		url += '&range=' + str(rate_range[0]) + ',' + str(rate_range[1])	
	
	return url

"""
 Task 3 to create Movie class
"""
class Movie:
	def __init__(self, name, rate, location, category, info_link, cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link

	def __repr__(self):
		return str(self)	

	def __str__(self):
		return ','.join([self.name, self.rate, self.location, self.category, self.info_link, self.cover_link])		


name = "肖申克的救赎"
rate = "9.6"
location = "美国"
category = "剧情"
info_link = "https://movie.douban.com/subject/1292052/"
cover_link = "https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg"

m = Movie(name, rate, location, category, info_link, cover_link)


def log(message):
	debug = True
	if debug:
		print(message)

"""
return locations list by looking up the locations in Douban, will called by Task 5
"""
def getLocations():
	locations = []
	url = 'https://movie.douban.com/tag/#/'
	html = expanddouban.getHtml(url)
	soup = BeautifulSoup(html, "html.parser")
	categories = soup.find_all('ul', class_='category')
	
	for span in categories[2].find_all('span', class_='tag'):
		locations.append(span.string)
	
	return locations[1:]	



"""
Task 4 to get movies by category and location
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location, rate_range=None):
	url = getMovieUrl(category, location, rate_range)
	log('Request url:' + url)
	"""
	 Task 2 to get html from Douban by imported expanddouban
	"""
	html = expanddouban.getHtml(url)
	soup = BeautifulSoup(html, "html.parser")
	movies = []

	for item in soup.find_all("a", class_="item"):
		name = item.find('span', class_='title').string
		rate = item.find('span', class_='rate').string
		info_link = item.get("href")
		cover_link = item.find('img').get('src')
		movie = Movie(name, rate, location, category, info_link, cover_link)
		movies.append(movie)

	return movies


"""
 Task 5 to get 3 categories high rating movies(greater than 9) for all locations and write to a csv file - movies.csv
"""
categories = ['剧情', '动作', '爱情']
#categories = ['剧情']
log('categories:' + str(categories))
all_locations = getLocations()
#all_locations = ['韩国']
log('locations:' + str(all_locations))

all_movies = []
#all_movies.extend([m,m])

for category in categories:
	for location in all_locations:
		movies = getMovies(category, location, [9,10])
		all_movies.extend(movies)

with open("movies.csv", 'w', newline='') as resultFile:
  wr = csv.writer(resultFile)
  for movie in all_movies:
  	wr.writerow([movie.name, movie.rate, movie.location, movie.category, movie.info_link, movie.cover_link])

log('Search result {0} movies had been written to movies.csv.'.format(str(len(all_movies))))