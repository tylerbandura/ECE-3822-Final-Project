import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from MyMovieExplorer.query3 import FindMoviesByGenre

def main():
    movie_list = FindMoviesByGenre()
    cvs_file_path = '/home/tuv12540/ece_3822/ECE-3822-Final-Project/data/prototype_data/movies_metadata_small.csv'
    movies_array = movie_list.load_movies_from_csv(cvs_file_path)
    year_bst = movie_list.build_year_bst(movies_array)
    user_genre = input("Enter a genre to search: ")
    user_start_year = int(input("Enter the start year: "))
    user_end_year = int(input("Enter the end year: "))

    result = movie_list.find_movies_by_genre_in_two_given_year(year_bst, user_genre, user_start_year, user_end_year)
    movie_list.display(result)

if __name__ == "__main__":
    main()