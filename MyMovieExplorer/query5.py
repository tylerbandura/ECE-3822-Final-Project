'''
file path: ECE-3822-Final-Project/MyMovieExplorer/query5.py

description: This code will output titles of suggested movies:
            it will do this by using a hash with genre in it and then filtering out
            mvies base on ratings and spew out a list of movies

author: tony mejia-cuba

'''

# imorts things
import os
import sys
import pickle
import ast

# Add project root to sys.path so Python can find DataStructures
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from DataStructures.hashTable import HashTable

# movie class to hold movie data and use in hash table
class Movie:
    # constructor
    def __init__(self, movie_id,title,genre_list,rating):
        self.movie_id = movie_id
        self.title = title
        self.genre_list = genre_list
        self.rating = float(rating) if rating else 0.0

# movie database class to hold movies and will do the suggesting
class MovieDatabase:
    # constructor
    def __init__(self):
        # store movies by title for quick lookup, call HashTable
        self.movies_by_title = HashTable(size=100000)
        # st ore movies by genre for suggesting
        self.movies_by_genre = HashTable(size=200)

    # method to add movie to database
    def add_movie(self, movie):
        self.movies_by_title.insert(movie.title, movie)

        for genre in movie.genre_list:
            genre_list = self.movies_by_genre.lookup(genre) # get list of movies in genre
            # if genre not in hash table, create new list
            if genre_list is None:
                genre_list = []
                self.movies_by_genre.insert(genre, genre_list) # insert new list into hash table
    
            genre_list.append(movie) # add movie to genre list

    # method to suggest movies based on title
    def suggest_movies(self, movie_title, top_k=5):
        # lookup movie by title
        movie = self.movies_by_title.lookup(movie_title)
        # error handling if movie not found
        if movie is None:
            print(f"Movie '{movie_title}' not found in database.")
            return []
        
        # get movies in same genre
        candidates = []

        # for each genre in movie, get list of movies in that genre and add to candidates list
        for genre in movie.genre_list:
            genre_bucket = self.movies_by_genre.lookup(genre)
            if genre_bucket is not None:
                for m in genre_bucket:
                    if m not in candidates:
                        candidates.append(m)
        
        # heart of it, computing suggesting base on score
        candidates = [m for m in candidates if m.title != movie_title]
        
        if not candidates:
            return []
        
        scored_candidates = []
        '''
        what this for loop will do:
        for each candidate movie m in the same genre:
            if m is the same as the input movie, skip it
            initialize score to 0
            add 5 points for genre match
            calculate rating difference between input movie and m
            if rating difference <= 1.0:
                add (1 - rating_diff) * 5 points to score
            append (score, m) to scored_candidates list

        I used this scoriung system becacuyse it will keep sugested movies
        based on genre and the it will filter based on rating closeness
        5 points for genre match ensures that only movies of the same genre are considered
        '''
        for m in candidates:
            score = 5
            diff = abs(movie.rating - m.rating)

            if diff <= 1.0:
                score += (1 - diff) * 5  # max 5 points for rating match
            scored_candidates.append((score, m))

            # simple bubble sort to sort scored candidates by score descending, mergesort.py was not finished
        for i in range(len(scored_candidates)):
            for j in range(i+1, len(scored_candidates)):
                if scored_candidates[j][0] > scored_candidates[i][0]:
                    scored_candidates[i], scored_candidates[j] = scored_candidates[j], scored_candidates[i]

        return [m.title for score, m in scored_candidates[:top_k]]

# function to load pickled movie database
def load_movie_database():
    # load the pickle movie database, copy from query6 just chnage
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    pickle_path = os.path.join(project_root, "pickled_things", "pickled_movie_db.pkl")
    
    # error handling if pickle file not found
    if not os.path.exists(pickle_path):
        print("Pickled movie database not found. Please run the pickling script first.")
        return None
    
    try:   
        with open(pickle_path, "rb") as f:
            db = pickle.load(f)
        return db
    except Exception as e:
        print(f"Error loading pickled movie database: {e}")
        return None

# main fuction to call everything and interact with user to get movie suggestions
def movie_suggestion():
    # load movie database
    db = load_movie_database()
    if db is None:
        print("Failed to load movie database.")
        return
    
    print("What movie would you like suggestions for?")
    movie_title = input("Enter movie title: ").strip()

    # get suggestions
    suggestions = db.suggest_movies(movie_title)

    # if suggestions found, print them
    if suggestions:
        print(f"Top suggestions for '{movie_title}':")
        for idx, title in enumerate(suggestions, start=1):
            print(f"{idx}. {title}")
    else:
        print("No suggestions found.")

        

if __name__ == "__main__":
    movie_suggestion()

# end of file