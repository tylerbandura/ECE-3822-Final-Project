"""
Docstring for cli.shell

This is the code that will be used for the user interface

"""

import sys
from MyMovieExplorer.query1 import Find_Movie_By_Title
from MyMovieExplorer.query2 import FindByActor

def main():
    print("Initializing Movie Data Explorer... Please wait.\n")

    # each query loads its own data internally
    q1 = Find_Movie_By_Title()
    q2 = FindByActor()

    movie_file = "data/prototype_data/movies_metadata_small.csv"
    movies_array = q1.load_movies_from_csv(movie_file)
    q1.build_title_hashtable(movies_array)

    print("Done! Lets Get Started!\n")

    while True:
        print("Welcome to GLP's Movie Data Explorer, please choose from the menu below :)\n")
        print("1. Find movie by title")
        print("2. Find Movie by actor")
        print("7. Quit Explorer")

        choice = input("\nEnter your choice (1-7): ").strip()

        # ---------------------------------------------------------
        # Query 1 Placeholder
        # ---------------------------------------------------------
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

        # ---------------------------------------------------------
        # Query 2: Find all movies by actor (ACTIVE)
        # ---------------------------------------------------------
        elif choice == "2":
            while True:
                actor = input("\nEnter actor name: ").strip()
                result_array = q2.find_movies(actor)

                if result_array is not None:
                    print(f"\nMovies featuring {actor}:")
                    for i in range(result_array.size()):
                        print("-", result_array.get(i))
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

        # ---------------------------------------------------------
        # Query 3 Placeholder
        # ---------------------------------------------------------
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

        # ---------------------------------------------------------
        # Query 4 Placeholder
        # ---------------------------------------------------------
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

        # ---------------------------------------------------------
        # Query 5 Placeholder
        # ---------------------------------------------------------
        elif choice == "5":
            while True:
                print("\n--- Query 5: Find Movies by Director ---")
                print("NOT DONE YET!\n")
                _ = input("Enter director name: ").strip()
                print("\n[Placeholder] Director search results would appear here.\n")

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

        # ---------------------------------------------------------
        # Query 6 Placeholder
        # ---------------------------------------------------------
        elif choice == "6":
            while True:
                print("\n--- Query 6: Find Top Grossing Movies ---")
                print("NOT DONE YET!\n")
                _ = input("Enter number of top movies to display (example: 10): ").strip()
                print("\n[Placeholder] Top grossing movies would appear here.\n")

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

        # ---------------------------------------------------------
        # Quit
        # ---------------------------------------------------------
        elif choice == "7":
            print("\nGoodbye!\n")
            break

        else:
            print("\nInvalid choice. Please enter 1–7.\n")


# ---------------------------------------------------------
# Run CLI
# ---------------------------------------------------------
if __name__ == "__main__":
    main()