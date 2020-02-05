import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/movies', methods=['GET'])
def list_movies():
    return "this is a list of movies"

@app.route('/movie/<int:id>', methods=['GET'])
def show_movie(id):
    return f"this is movie {id}"

@app.route('/movies', methods=['POST'])
def create_movie():
    return "this is a new movie"

@app.route('/movie/<int:id>', methods=['PUT', 'PATCH'])
def update_movie(id):
    return f"movie {id} was updated"

@app.route('/movie/<int:id>', methods=['DELETE'])
def delete_movie(id):
    return f"movie {id} was deleted"

if __name__ == "__main__":
  app.run()