from flask import Flask, render_template

import mongoengine
from mongoengine import Document,StringField
host = "ds011893.mlab.com"
port = 11893
db_name = "c4e_rss"
user_name = "c4e"
password = "codethechange"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)

# class Movie:
#     def __init__(self,title,img):
#         self.title = title
#         self.img = img
#
# movie1 = Movie('Zootopia','http://blogs-images.forbes.com/scottmendelson/files/2016/03/zootopiaposter1.jpg')
# movie2 = Movie('The girl next door','http://ecx.images-amazon.com/images/I/51izKX%2BywRL._SY300_.jpg')
# movie3 = Movie('Cloud Atlas','https://www.singularityweblog.com/wp-content/uploads/2013/07/Cloud-Atlas-2.jpg')
# m_list = [movie1,movie2,movie3]

class Movie(Document):
    title = StringField()
    img = StringField()

@app.route('/')
def hello_world():
    return 'Hello Khanh!'

@app.route('/c4e')
def hello_c4e():
    return 'Hello C4E !'

@app.route('/hi/<name>')
def hello(name):
    return('Hello ' + name)

@app.route('/movie')
def get_movie():
    return render_template('movie.html')

@app.route('/movie2')
def get_movie2():
    return render_template('movie2.html',title='Civil War', img = 'http://media.comicbook.com/2016/04/civil-war-cap-tony-179110.jpg')

@app.route('/movies')
def movies():
    return render_template('movies.html',movie_list = Movie.objects)

if __name__ == '__main__':
    app.run()
