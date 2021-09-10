from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Initializing playlist app
app = Flask(__name__)
app.config.from_object("project.config.Config")
#Database SQLalchemy
db = SQLAlchemy(app) #object relation mapper
ma = Marshmallow(app) #convert object from python datatype

class Playlist(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  author = db.Column(db.String(100))
  length = db.Column(db.Float)
  genre = db.Column(db.String(100))

  def __init__(self, name, author, length, genre):
    self.name = name
    self.author = author
    self.length = length
    self.genre = genre

#Playlist Schema
class PlaylistSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'author', 'length', 'genre')

#Init Schema
playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)

#Testing route
@app.route("/")
def hello_world():
  return jsonify(hello="world")

#Add Song
@app.route('/playlist', methods=['POST'])
def add_song():
  name = request.json['name']
  author = request.json['author']
  length = request.json['length']
  genre = request.json['genre']
  new_song = Playlist(name, author, length, genre)
  #to add song and save to db
  db.session.add(new_song)
  db.session.commit()

  return playlist_schema.jsonify(new_song)


#Get Song
@app.route('/playlist', methods=['GET'])
def get_song():
  songs = Playlist.query.all()
  output = playlists_schema.dump(songs)

  return jsonify(output)


#Update Song
@app.route('/playlist/<id>', methods=['PUT'])
def update_song():
  playlist = Playlist.query.get(id)
  name = request.json['name']
  author = request.json['author']
  length = request.json['length']
  genre = request.json['genre']

  playlist.name = name
  playlist.author = author
  playlist.length = length
  playlist.genre = genre

  db.session.commit()

  return playlist_schema.jsonify(playlist)


#Delete Song
@app.route('/playlist/<id>', methods=['DELETE'])
def delete_song(id):
  playlist = Playlist.query.get(id)
  db.session.delete(playlist)
  db.session.commit()

  return playlist_schema.jsonify(playlist)
