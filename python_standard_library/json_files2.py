import json
from pathlib import Path

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
first_movie = movies[0]["title"]
print(first_movie)
