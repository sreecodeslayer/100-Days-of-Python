from toapi import Item, XPath


class MovieData(Item):
	title = XPath('//h1/text()')
	year = XPath('//h2[1]/text()')
	genre = XPath('//h2[2]/text()')
	imdb_rating = XPath('//span[@itemprop="ratingValue"]/text()')

	def clean_genre(self, genre):
		genre = [gen.strip() for gen in genre.split('/')]
		return genre

	class Meta:
		source = XPath('//div[@id="movie-info"]')
		route = {'/movie_data?href=:href': '/movie/:href'}
