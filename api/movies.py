import json

from flask import Flask, request, Response
from api.models.movie import Movie

app = Flask(__name__)
if not Movie.exists():
  Movie.create_table(
    read_capacity_units=Movie.Meta.read_capacity_units,
    write_capacity_units=Movie.Meta.write_capacity_units,
    wait=True
  )

@app.route('/movies', methods=['GET'])
def list_movies():
  sort = request.args.get("sort")
  desc = request.args.get("desc")
  asc = request.args.get("asc")
  movies = Movie.scan()
  result = {}
  result['movies'] = [dict(movie) for movie in movies]
  if sort:
    if desc:
      result['movies'].sort(reverse=True, key=lambda i: (i[sort]))
    elif asc:
      result['movies'].sort(key=lambda i: (i[sort]))
    else:
      result['movies'].sort(key=lambda i: (i[sort]))
  result['count'] = movies._count
  return Response(json.dumps(result), mimetype='application/json')

@app.route('/movie/<int:id>', methods=['GET'])
def show_movie(id):
    return f"this is movie {id}"

@app.route('/movies', methods=['POST'])
def create_movie():
  print(request)
  args = request.get_json()
  movie = Movie(
    title=args['title'],
    format=args['format'],
    length=args['length'],
    release_year=args['release_year'],
    rating=args['rating']
  ).save()
  return movie

@app.route('/movie/<int:id>', methods=['PUT', 'PATCH'])
def update_movie(id):
    return f"movie {id} was updated"

@app.route('/movie/<int:id>', methods=['DELETE'])
def delete_movie(id):
    return f"movie {id} was deleted"

if __name__ == "__main__":
  app.run(debug=True)