from flask import Flask
import imdb_api as imdb

app = Flask(__name__)

@app.route('/')
def root():
    return 'Root', 200

@app.route('/test')
def test():
    mov_id = imdb.top_250_movies()[1]['id']
    return vars(imdb.movie_from_id(mov_id))

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)