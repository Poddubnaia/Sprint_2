class Movies:
    def __init__(self):
        self.movies = []
    
    def add_movies(self,movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self,movie):
        self.add_movies(movie)
        return f'Комедии: {self.movies}'


class Drama(Movies):
    def add_movie(self,movie):
        self.add_movies(movie)
        return f'Драма: {self.movies}'


comedy = Comedy()
print(comedy.add_movie('Большой куш')) 
drama = Drama()
print(drama.add_movie('Оружейный барон'))  