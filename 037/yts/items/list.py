from toapi import Item, XPath


class MovieListPage(Item):
	next_page = XPath('//ul[contains(@class,"tsc_pagination tsc_paginationA tsc_paginationA06")]//li/a[starts-with(text(), "Next")]/@href')

	def clean_next_page(self, next_page):
		next_page = next_page[0] if next_page else 1
		return next_page

	class Meta:
		source = None
		route = {'/movie_list?page=:page': '/browse-movies?page=:page'}

class MovieList(Item):
	names = XPath('//a[@class="browse-movie-link"]/@href')

	def clean_names(self, names):
		names = [name.split('https://yts.am/movie/')[-1] for name in names]
		return names

	class Meta:
		source = XPath('//div[@class="browse-content"]')
		route = {'/movie_list?page=:page': '/browse-movies?page=:page'}