# Welcome to Team GLP's Movie Data Explorer!
The Movie Data Explorer is a program that serves to enhance the way a movie buff can access all the information they want
regarding various movies. Movies are stored in a large database that consists of over 45,000 films located in the `data` folder, and each film has data associated with it, such as genre, revenue, rating (out of 10), year released, a synopsis, and runtime.  The
Movie Explorer uses efficient data structures and algorithms to easily sort through it and give the user
exactly what they're searching for.

All code is done using Python.


# Main Features:
* Allows users to find movies based on the title, or a particular actor
  * The list of movies by actor will be sorted based on rating, increasing usefulness
* Finds movies of a certain genre (such as Action) that released between 2 different years
* Finds the top 10 movies based on rating or revenue
* Suggests similar movies
* Finds the shortest connection between 2 actors
* Allows to save movies to a favorites list as well as a Watch Later list, and to view and clear it.

# How to use:
To use the program, clone the repo into VS code by typing ` git clone https://github.com/tylerbandura/ECE-3822-Final-Project` into your VS code terminal, then run the `main.py` file located in the CLI folder. This is done by typing `python -m cli.main` in the terminal. It may take a bit to initialize.

After initialization is complete, you will be brought to the menu, with a list of queries/actions you can run.
Each query/action is represented by a number:
```
Welcome to GLP's Movie Data Explorer, please choose from the menu below :)
1. Find movie by title
2. Find Movie by actor
3. Finds all movies between two years by given genre
4. Finds top 10 movies (rating or revenue)
5. Get suggested movie
6. Find the shortest path between two actors
7. Manage favorites / Watch-Later lists
8. Quit Explorer
Enter your choice(1-8)
```

## Example 1: Find movies by actor
Let's say, for example, you want to find all movies an actor was in. To do this, type "2".
You will be asked to input an actor. As an example, let's do Tom Hanks. Type "Tom Hanks" when prompted.
The resulting output is each film Tom Hanks is in.

You will also be asked if you would like to add one of his movies to your favorites/watch later list.
```
Would you like to add one of these movies to your favorites or watch-later list? (yes/no):
```
Type "yes" if you want to add to your list, then type the title of the movie you would like to add.

You will then be asked if you are finished with your search. Type 'yes' to exit the program, or type 'no' to return to the menu and select another action.

## Example 2: Find all movies in a given genre between 2 years
If you want to use the Movie Explorer to find movies of a certain genre released between 2 years, follow these instructions:
* Type '3'
* Type the genre you would like to search for (Example: Action)
* Input your start year (Example: 2009)
* Input your end year (Example: 2011)

The resulting output will be the list of action films released between 2009 and 2011.
Just as in the previous example, you can add one of these films to your lists.

You will again be asked if you are finished with your search. Type 'yes' to exit the program, or type 'no' to return to the menu and select another action.

## Example 3: Managing lists
One key feature of the Movie Explorer is the ability to create and manage a list of favorite movies and a list of movies to watch later.
To manage your list(s), type '7' while in the menu, and the following commands will be shown:
```
add fav <title of movie>
add watch <title of movie>
remove fav <title of movie>
remove watch <title of movie>
show favs
show watchlist
clear favs
clear watchlist
quit
```
### Adding to list
For example, if you want to add the acclaimed animated film Toy Story (1995) to your favorites (you should), type `add fav Toy Story`,
and it will be added to your list.
### Remove from list
If you want to remove it from your favorites (how could you?) type `remove fav Toy Story`.
The same applies to the watch later list. Simply replace 'fav' with 'watch'.
### Show list
type `show favs` or `show watchlist` to show all the films you have added to your list(s).
### Clear list
type `clear favs` or `clear watchlist` to remove all movies from your lists.

# Quitting the program
If you are finished with the Movie Explorer and would like to quit the program:
* Type '8' while at the menu. The program will wish you goodbye and end.
  * Alternatively, when running Queries 1 or 2, the program will ask if you if you are finished with your search.
```
Are you finished with your search? (yes/no):
```
Typing 'yes' will exit the program.

# Credits:
* Tony Mejia-Cuba
* Trang Phung
* ZhaoXiang Lan
* Tyler Bandura

**Thank you for using our program!**







