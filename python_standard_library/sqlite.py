import sqlite3
import json
from pathlib import Path

# No longer need json database
# movies = json.loads(Path("movies.json").read_text())

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
    # conn.commit()
