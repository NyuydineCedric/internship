def average_rating_by_genre(movies):
    
    averages = {}

    action_total = 0
    action_count = 0

    comedy_total = 0
    comedy_count = 0

    drama_total = 0
    drama_count = 0

    for movie in movies:

        if movie["genre"] == "Action":
            action_total = action_total + movie["rating"]
            action_count = action_count + 1

        elif movie["genre"] == "Comedy":
            comedy_total = comedy_total + movie["rating"]
            comedy_count = comedy_count + 1

        elif movie["genre"] == "Drama":
            drama_total = drama_total + movie["rating"]
            drama_count = drama_count + 1

    if action_count > 0:
        averages["Action"] = action_total / action_count

    if comedy_count > 0:
        averages["Comedy"] = comedy_total / comedy_count

    if drama_count > 0:
        averages["Drama"] = drama_total / drama_count

    return averages


def movies_above(movies, min_rating):

    titles = []

    for movie in movies:

        if movie["rating"] >= min_rating:
            titles.append(movie["title"])

    return titles


movies = [
    {"title": "Movie A", "genre": "Action", "rating": 7.5},
    {"title": "Movie B", "genre": "Comedy", "rating": 6.0},
    {"title": "Movie C", "genre": "Action", "rating": 8.8},
    {"title": "Movie D", "genre": "Drama", "rating": 9.1}
]

print(average_rating_by_genre(movies))
print(movies_above(movies, 7.5))