class Profile:
    def __init__(self):
        self.liked_genres = []
        self.disliked_genres = []
        self.movies = [] # {'id': 'rating': 'liked/favorited/passed'}
    
    def get_liked_movies(self):
        return list(filter(lambda x: x.rating in ['liked', 'favorited'], self.movies))
    
    def get_favorited_movies(self):
        return list(filter(lambda x: x.rating == 'favorited', self.movies))