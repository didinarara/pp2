def is_high_score(movie):
    return movie["imdb"] > 5.5

sample_movie = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}

result = is_high_score(sample_movie)
print(result)  # True
