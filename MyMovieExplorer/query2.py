"""
query2.py

Purpose: Find all movies by a given actor, movie info will also be displayed

key feature: Each movie will be sorted by rating

This file will build two hashtables:
1. actor: actor_name(lower) -> [movie_id...]
2. id_to_title: movie_id -> title

To keep our load factor less than 0.75 (aiming for a = 0.65)
    actorTable: buckets = 60000/0.65 = 92000 (bucket size = 100000)
    id_to_title: buckets = 45000/0.65 = 69000 (bucketsize = 70000)

"""
from DataStructures.array import array

class FindByActor:
    def __init__(self, actorTable, id_to_movieData, id_to_rating):
        # getting prebuilt hash tables from main.py
        self.actorTable = actorTable
        self.id_to_movieData = id_to_movieData
        self.id_to_rating = id_to_rating

    # find all movies from an actors name
    def find_movies(self, actor_name):
        if not actor_name:
            return None
        
        actor_key = actor_name.strip().lower() # make lowercase for case sensitivity
        movies_entries = self.actorTable.lookup(actor_key)
        if not movies_entries:
            return None
        
        results = []

        for entry in movies_entries:
            movie_id = entry.get("movie_id")
            movie_data = self.id_to_movieData.lookup(movie_id)
            rating = self.id_to_rating.lookup(movie_id)

            if movie_data is None:
                continue

            movie_info = {}
            for key in movie_data:
                movie_info[key] = movie_data[key]

            movie_info["rating"] = rating if rating is not None else 0.0
            results.append(movie_info)

        # sort by rating (highest first)
        results.sort(key=lambda m: m["rating"], reverse=True)
        return results
    
    def display_movie_info(self, movie):
        if not movie:
            print("\nMovie not found.")
            return
        
        #title
        title = movie.get("title") or movie.get("original_title") or "Unknown Title"
        print(f"Title: {title}")

        # release year
        # --- Release Year ---
        release_date = movie.get("release_date", "")
        year = release_date[:4] if len(release_date) >= 4 else "Unknown"

        # --- Runtime ---
        runtime = movie.get("runtime")
        if runtime:
            try:
                runtime = int(float(runtime))
                hours = runtime // 60
                minutes = runtime % 60
                runtime_str = f"{hours}h {minutes}m"
            except:
                runtime_str = "Unknown"
        else:
            runtime_str = "Unknown"

        # --- Language ---
        lang = movie.get("original_language", "Unknown")
        if isinstance(lang, str):
            lang = lang.upper()

        print(f"{year} | {runtime_str} | {lang}")

        # --- Genres ---
        genres = movie.get("genres")
        if genres and isinstance(genres, str):
            print(f"Genres: {genres}")

        # --- Budget ---
        budget = movie.get("budget")
        if budget:
            try:
                budget = int(float(budget))
                print(f"Budget: ${budget:,}")
            except:
                print(f"Budget: {budget}")

        # --- Revenue ---
        revenue = movie.get("revenue")
        if revenue:
            try:
                revenue = int(float(revenue))
                print(f"Revenue: ${revenue:,}")
            except:
                print(f"Revenue: {revenue}")

        # --- Rating ---
        rating = movie.get("rating", None)
        if rating is not None:
            print(f"Rating: {rating:.2f} / 10 stars")

        # --- Overview ---
        overview = movie.get("overview")
        if overview and str(overview).lower() != "nan":
            print("Synopsis:", overview)
