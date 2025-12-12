'''
file: tests/test4.py
ZhaoXiang Lan, 12/10/2025

description:
the test file for query4.py
'''
# add the project root to sys.path
import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from MyMovieExplorer.query4 import Top10_Movies

def main():
    finder = Top10_Movies()
    cvs_file_path = '/home/tuv12540/ece_3822/ECE-3822-Final-Project/data/prototype_data/movies_metadata_small.csv'
    print("Loading movies from CSV file...")
    finder.load_movies_from_csv(cvs_file_path)
    print(f"Loaded {finder.movies_array.size()} movies.\n")

    print("Find the top-10 movies by:")
    print("  1) rating")
    print("  2) revenue")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        key = "vote_average"
    else:
        key = "revenue"

    top10 = finder.top_10_by_key(key, size=10)
    finder.display(top10, key)

if __name__ == "__main__":
    main()