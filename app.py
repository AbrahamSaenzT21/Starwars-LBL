import os
from flask import Flask, jsonify
from logic_file import sort_movies_by_id, get_movie_characters

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def list_movies():
    sorted_movies = sort_movies_by_id()
    return jsonify(sorted_movies)

@app.route("/movies/<int:movie_id>/characters", methods=['GET'])
def list_characters(movie_id):
    characters = get_movie_characters(movie_id)
    return jsonify(characters)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)

