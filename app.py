from flask import Flask
import imdb_api as imdb

app = Flask(__name__)

@app.route('/')
def root():
    return 'Root', 200

@app.route('/api_3')
def api_3():
    return imdb.search_movie('Inception'), 200

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)