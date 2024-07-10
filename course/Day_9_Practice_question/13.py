# class to represent the attribute of the movie such as title director and rating

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}, Rating: {self.rating}"
    
    def get_title(self):
        return self.title
    
    def get_director(self):
        return self.director
    
    def get_rating(self):
        return self.rating
    
    def update_rating(self, new_rating):
        self.rating = new_rating
    
    def get_info(self):
        return {"title": self.title, "director": self.director, "rating": self.rating}
    
    @staticmethod
    def from_json(json_data):
        return Movie(json_data["title"], json_data["director"], json_data["rating"])
    
    def to_json(self):
        return self.get_info()

# Example usage:
movie_instance = Movie("Inception", "Christopher Nolan", 8.8)
print(movie_instance)  
print(movie_instance.get_info())  
movie_instance.update_rating(9.0)
print(movie_instance)  
print(movie_instance.to_json())  