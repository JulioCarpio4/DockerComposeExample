# flask_web/app.py
from flask import Flask
from redis import Redis
#from flask import render_template

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')