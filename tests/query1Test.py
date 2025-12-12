'''
file: tests/test1.py
ZhaoXiang Lan, 12/8/2025

description:
the test file for query1.py
'''
# add the project root to sys.path
import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from MyMovieExplorer.query1 import Find_Movie_By_Title

def main():
    finder = Find_Movie_By_Title()
    pickle_file_path = '/home/tuv12540/ece_3822/ECE-3822-Final-Project/data/id_to_movieData.pkl'
    movies_array = finder.load_movies_from_csv(pickle_file_path)
    movie_title_table = finder.build_title_hashtable(movies_array)
    user_giving = input("Enter a movie title to search: ")
    result = finder.find_movie_by_title(movie_title_table, user_giving)
    finder.display_movie_info(result)

if __name__ == "__main__":
    main()