"""
Docstring for cli.shell

This is the code that will be used for the user interface

"""

import sys
from MyMovieExplorer.query1 import Find_Movie_By_Title
from MyMovieExplorer.query2 import FindByActor
from MyMovieExplorer.query4 import Top10_Movies
from MyMovieExplorer.query5 import MovieDatabase, load_movie_database
from MyMovieExplorer.query6 import path_for_2_actors
from MyMovieExplorer.fav_list import UserProfile

user_profile = UserProfile()

# this is the function for the fav/watch later list, it will be called with each query
def handle_add_to_list(user_profile, movie_title):
    """
    Helper for adding a movie to favorites or watch-later list.
    """
    list_choice = input("Add to (fav/watch)? ").strip().lower()

    if list_choice == "fav":
        if user_profile.add_favorite(movie_title):
            print(f"Added '{movie_title}' to Favorites.\n")
        else:
            print("That movie is already in Favorites.\n")

    elif list_choice == "watch":
        if user_profile.add_watch_later(movie_title):
            print(f"Added '{movie_title}' to Watch-Later list.\n")
        else:
            print("That movie is already in Watch-Later.\n")

    else:
        print("Invalid choice. Please type 'fav' or 'watch'.\n")


def main():
    print("Initializing Movie Data Explorer... Please wait.\n")

    # load pickled data
    import os, pickle

    DATA_DIR = "data"
    MOVIE_PATH = os.path.join(DATA_DIR, "id_to_movieData.pkl")
    RATING_PATH = os.path.join(DATA_DIR, "id_to_rating.pkl")
    ACTOR_PATH = os.path.join(DATA_DIR, "actorTable.pkl")

    print("Loading pickles...")

    with open(MOVIE_PATH, "rb") as f:
        id_to_movieData = pickle.load(f)
    with open(RATING_PATH, "rb") as f:
        id_to_rating = pickle.load(f)
    with open(ACTOR_PATH, "rb") as f:
        actorTable = pickle.load(f)

    # each query loads its own data internally
    q1 = Find_Movie_By_Title()
    q2 = FindByActor(actorTable, id_to_movieData, id_to_rating)
    q5 = load_movie_database()

    movie_file = "data/prototype_data/movies_metadata_small.csv"
    movies_array = q1.load_movies_from_csv(movie_file)
    q1.build_title_hashtable(movies_array)

    print("Done! Lets Get Started!\n")

    while True:
        print("Welcome to GLP's Movie Data Explorer, please choose from the menu below :)\n")
        print("1. Find movie by title")
        print("2. Find Movie by actor")
        print("3. Finds all movies between two years by given genre")
        print("4. Top 10 movies (ratings or revenue)")
        print("5. Get suggested Movie")
        print("6. Find the shortest path between two actors")
        print("7. Manage favorites / Watch-Later Lists")
        print("8. Quit Explorer")

        choice = input("\nEnter your choice (1-8): ").strip()

        # Query 1 Placeholder
        if choice == "1":
            while True:
                print("\n--- Query 1: Find Movie by Title ---")
                title = input("Enter movie title: ").strip()

                movie = q1.find_movie_by_title(q1.movie_title_table, title)
                q1.display_movie_info(movie)

                again = input("\nAre you finished with your search? (yes/no): ").strip().lower()

                if again == "no":
                    print("\nReturning to main menu...\n")
                    break
                elif again == "yes":
                    print("\nExiting program. Goodbye!\n")
                    return
                else:
                    print("\nInvalid input. Returning to main menu.\n")
                    break

        # Query 2: Find all movies by actor (ACTIVE)
        elif choice == "2":
            while True:
                actor = input("\nEnter actor name: ").strip()
                result_array = q2.find_movies(actor)

                if result_array:
                    print(f"\nMovies featuring {actor} (sorted by rating):")
                    for movie in result_array:
                        q2.display_movie_info(movie)

                add_choice = input("\nWould you like to add one of these movies to your favorites or watch-later list? (yes/no): ").strip().lower()
                if add_choice == "yes":
                    movie_title = input("Enter the exact movie title: ").strip()
                    handle_add_to_list(user_profile, movie_title)

                else:
                    print(f"\nNo movies found for {actor}.")

                again = input("\nAre you finished with your search? (yes/no): ").strip().lower()
                if again == "no":
                    print("\nReturning to main menu...\n")
                    break
                elif again == "yes":
                    print("\nExiting program. Goodbye!\n")
                    return
                else:
                    print("\nInvalid input. Returning to main menu.\n")
                    break

        # Query 3 Placeholder
        elif choice == "3":
            while True:
                print("\n--- Query 3: Find Movies by Genre ---")
                print("NOT DONE YET!\n")
                _ = input("Enter genre (example: Comedy, Action, Drama): ").strip()
                print("\n[Placeholder] Genre search results would appear here.\n")

                again = input("\nAre you finished with your search? (yes/no): ").strip().lower()
                if again == "no":
                    print("\nReturning to main menu...\n")
                    break
                elif again == "yes":
                    print("\nExiting program. Goodbye!\n")
                    return
                else:
                    print("\nInvalid input. Returning to main menu.\n")
                    break

        # Query 4 Placeholder
        elif choice == "4":
            while True:
                print("\n--- Query 4: Find Movies by Year ---")
                print("NOT DONE YET!\n")
                _ = input("Enter year (example: 1995): ").strip()
                print("\n[Placeholder] Year-based search results would appear here.\n")

                again = input("\nAre you finished with your search? (yes/no): ").strip().lower()
                if again == "no":
                    print("\nReturning to main menu...\n")
                    break
                elif again == "yes":
                    print("\nExiting program. Goodbye!\n")
                    return
                else:
                    print("\nInvalid input. Returning to main menu.\n")
                    break

        # Query 5
        elif choice == "5":
            while True:
                print("\nQuery 5: Suggested movies")
                # Make sure the movie database is loaded
                if q5 is None:
                    print("Movie suggestion database not loaded. Please check your pickle file.")
                    break

                movie_title = input("Enter a movie title you like: ").strip()

                # Get suggestions
                suggestions = q5.suggest_movies(movie_title)

                # Display results
                if suggestions:
                    print(f"\nTop suggestions for '{movie_title}':")
                    for i, title in enumerate(suggestions, start=1):
                        print(f"{i}. {title}")

                    # Let user add a suggestion to favorites or watch-later
                    add_choice = input(
                        "\nWould you like to add one of these movies to your favorites or watch-later list? (yes/no): "
                    ).strip().lower()

                    if add_choice == "yes":
                        movie_to_add = input("Enter the exact movie title: ").strip()
                        handle_add_to_list(user_profile, movie_to_add)
                else:
                    print(f"\nNo suggestions found for '{movie_title}'.")

                # Loop control
                again = input("\nWould you like to get more suggestions? (yes/no): ").strip().lower()
                if again == "no":
                    print("\nReturning to main menu...\n")
                    break
                elif again == "yes":
                    continue
                else:
                    print("\nInvalid input. Returning to main menu.\n")
                    break

        # Query 6
        elif choice == "6":
            import io, sys

            while True:
                print("\nQuery 6: Find Shortest Path Between Two Actors")

                print("Enter two actor names to find their shortest connection (shared movie path):")
                actor1 = input("Actor 1: ").strip().lower()
                actor2 = input("Actor 2: ").strip().lower()

                old_argv = sys.argv
                old_stdout = sys.stdout
                buffer = io.StringIO()

                # Run the query6 function directly
                try:
                    sys.argv = ["query6.py", actor1, actor2]
                    sys.stdout = buffer

                    # Run your teammate’s code exactly as written
                    from MyMovieExplorer import query6
                    query6.path_for_2_actors()

                except SystemExit:
                    # Ignore sys.exit() calls from their script
                    pass
                except Exception as e:
                    print(f"\nError running Query 6: {e}")
                finally:
                    # Restore state
                    sys.argv = old_argv
                    sys.stdout = old_stdout

                # Print captured output to the CLI
                output = buffer.getvalue().strip()
                print("\n" + output + "\n")

                # Optional: add connecting movie to favorites or watch-later
                add_choice = input("Would you like to add one of these connecting movies to your favorites or watch-later list? (yes/no): ").strip().lower()
                if add_choice == "yes":
                    movie_title = input("Enter the exact movie title: ").strip()
                    handle_add_to_list(user_profile, movie_title)

                again = input("\nWould you like to find another path? (yes/no): ").strip().lower()
                if again == "no":
                    print("\nReturning to main menu...\n")
                    break
                elif again != "yes":
                    print("\nInvalid input. Returning to main menu.\n")
                    break


        elif choice == "7":
            print("\nManage Favorites & Watch-Later Lists")
            print("Available commands:")
            print("  add fav <title>")
            print("  add watch <title>")
            print("  remove fav <title>")
            print("  remove watch <title>")
            print("  show favs")
            print("  show watchlist")
            print("  clear favs")
            print("  clear watchlist")
            print("  quit  (to exit back to main menu)\n")

            running = True
            while running:
                command = input("Enter command: ").strip().lower()
                running = user_profile.handle_command(command)

            print("\nReturning to main menu...\n")
                  
        # Quit
        elif choice == "8":
            print("\nGoodbye!\n")
            break

        else:
            print("\nInvalid choice. Please enter 1–8.\n")


# Run CLI
if __name__ == "__main__":
    main()