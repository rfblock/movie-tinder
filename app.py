from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'Root', 200

@app.route('/api_3')
def api_3():
    return "Bad request", 500

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)