from toapi import Api
from items.list import MovieList, MovieListPage
from items.data import MovieData
from settings import MySettings

api = Api('https://yts.am/', settings=MySettings)
api.register(MovieListPage)
api.register(MovieList)
api.register(MovieData)

if __name__ == '__main__':
	api.serve()
