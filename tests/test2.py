from MyMovieExplorer.query2 import FindByActor

def test_query2():
    q2 = FindByActor()
    q2.load_movies()
    q2.load_actors()

    q2.find_movies("Tom Hanks")
    q2.find_movies("Robin Williams")
    q2.find_movies("Don Rickles")
    q2.find_movies("Tom Hnaks")
    q2.find_movies("Bonnie Hunt")

if __name__ == "__main__":
    test_query2()
