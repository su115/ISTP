import socket
from flask import Flask, render_template
from redis import Redis

#my add
import os

app = Flask(__name__)
redis = Redis(host='my_redis', port=6379)

# my function to debug problems!!!
def exists(path):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + os.sep + path
    if (os.path.exists(path)):
        return path
    else:
        pr='Path: not found or not exist!!!'+path
        pr+='\nCurrent path:'+dir_path
        pr += '\n List dir:'+str(os.listdir(dir_path))
        raise Exception(pr)

@app.route('/hits')
def hits():
    count = redis.incr('hits')
    message = 'I have been seen {t} times. My Hostname is: {h} \n'.format(
        t=count, h=socket.gethostname()
    )
    # call exists
    path = exists('logs/app.log')
    with open(path, 'a') as log:
        log.write(message)
    return str(count)


@app.route('/logs')
def logs():
    path = exists('logs/app.log')
    with open(path, 'r') as log:
        return ''.join(list(map(lambda l: '<p>{text}</p>'.format(text=l), log.readlines())))


@app.route('/')
def main():
    return render_template('index.html', parameter=str(redis.get('hits')))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
