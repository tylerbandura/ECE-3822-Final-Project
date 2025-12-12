#!/usr/bin/env python
#
# file path: /home/tul34363/ece_3822LABWORK/ECE-3822-Final-Project/MyMovieExplorer/fav_list.py
#
#
# description: This script defines a UserProfile class that manages user's favorite and watch-later movie lists
#               we call on the array.py to make the list. this program will run concurrently with the main program.
#               the user can add, remove, clear, and display movies in their favorite and watch-later lists.
#               the program will also handle commands to add, remove, clear, and display movies in their favorite and watch-later lists.
#               the program will also handle commands to exit the program.
#
#               in the main program this should be in a while running loop
#               this is so the user can interact whenever they want to manage their movie lists
#
# import things
import os
import sys

# add project root to sys.path so Python can find DataStructures
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from DataStructures.array import array

class UserProfile:
    def __init__(self):
        # using your dynamic array, not Python list
        self.favorites = array()
        self.watch_later = array()

    # fuction to check if a movie is in the list
    def _contains(self, arr, movie_title):
        i = 0
        while i < arr.size():
            if arr.get(i) == movie_title:
                return True
            i += 1
        return False
    # fuction to remove a movie from the array and return the new array and a boolean indicating if the movie was removed
    def _remove_from_array(self, arr, movie_title):
        new_arr = array()
        removed = False

        i = 0
        # this while loop will iterate through the array and add 
        # all elements to the new array except the one to be removed
        while i < arr.size():
            value = arr.get(i)
            if value == movie_title and not removed:
                removed = True
            else:
                new_arr.append(value)
            i += 1

        return new_arr, removed

    # fuction to add a movie to the array
    def add_favorite(self, movie_title):
        # if the movie is already in the favorites list, return False
        if self._contains(self.favorites, movie_title):
            return False
        # add the movie to the favorites list
        self.favorites.append(movie_title)
        return True

    # fuction to add a movie to the watch-later list
    def add_watch_later(self, movie_title):
        # if the movie is already in the watch-later list, return False
        if self._contains(self.watch_later, movie_title):
            return False
        # add the movie to the watch-later list
        self.watch_later.append(movie_title)
        return True

    # fuctikon to remove a movie from the array
    def remove_favorite(self, movie_title):
        # remove the movie from the favorites list
        self.favorites, removed = self._remove_from_array(self.favorites, movie_title)
        return removed
    # fuction to remove a movie from the watch-later list
    def remove_watch_later(self, movie_title):
        # remove the movie from the watch-later list
        self.watch_later, removed = self._remove_from_array(self.watch_later, movie_title)
        return removed

    # fuction to clear the array
    def clear_favorites(self):
        self.favorites = array()

    # fuction to clear the watch-later list
    def clear_watch_later(self):
        self.watch_later = array()

    # fuction to show the array
    def show_favorites(self):
        if self.favorites.size() == 0:
            print("No favorites yet!\n")
            return

        print("\nYour Favorite Movies:")
        i = 0
        # while there are elements in the array, print them
        while i < self.favorites.size():
            print(" •", self.favorites.get(i))
            i += 1
        print()

    # fuction to show the watch-later list
    def show_watch_later(self):
        if self.watch_later.size() == 0:
            print("Nothing in watch later!\n")
            return

        print("\nYour Watch Later List:")
        i = 0
        while i < self.watch_later.size():
            print(" •", self.watch_later.get(i))
            i += 1
        print()

    # fuction to handle commands form the user in the main program.
    def handle_command(self, command):
        # if the command is add fav, add the movie to the favorites list
        if command.startswith("add fav "):
            title = command.replace("add fav ", "")
            if self.add_favorite(title):
                print(f"Added to favorites: {title}\n")
            else:
                print("Movie already in favorites!\n")
            return True

        # if the command is add watch, add the movie to the watch-later list
        if command.startswith("add watch "):
            title = command.replace("add watch ", "")
            if self.add_watch_later(title):
                print(f"Added to watch later: {title}\n")
            else:
                print("Movie already in watch later!\n")
            return True

        # if the command is remove fav, remove the movie from the favorites list
        if command.startswith("remove fav "):
            title = command.replace("remove fav ", "")
            if self.remove_favorite(title):
                print(f"Removed from favorites: {title}\n")
            else:
                print("Movie not found in favorites.\n")
            return True

        # if the command is remove watch, remove the movie from the watch later list
        if command.startswith("remove watch "):
            title = command.replace("remove watch ", "")
            if self.remove_watch_later(title):
                print(f"Removed from watch later: {title}\n")
            else:
                print("Movie not found in watch later.\n")
            return True

        # if the command is clear favs, clear the favorites list, propmt the user for confirmation
        if command == "clear favs":
            print("Are you sure you want to clear your favorites list? (y/n)")
            choice = input("> ").lower()

            if choice == "y":
                self.clear_favorites()
                print("Favorite list cleared.\n")
            else:
                print("Operation cancelled.\n")
            return True
    
        # if the command is clear watchlist, clear the watch later list, prompt the user for confirmation
        if command == "clear watchlist":
            print("Are you sure you want to clear your watch later list? (y/n)")
            choice = input("> ").lower()

            if choice == "y":
                self.clear_watch_later()
                print("Watch later list cleared.\n")
            else:
                print("Operation cancelled.\n")
            return True

        # if the command is show favs, show the favorites list
        if command == "show favs":
            self.show_favorites()
            return True

        # if the command is show watchlist, show the watch later list
        if command == "show watchlist":
            self.show_watch_later()
            return True

        # if the command is quit, exit the program
        if command == "quit":
            return False

        print("Unknown command.\n")
        return True
