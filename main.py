# -*- coding: utf-8 -*-
import os
import time

import requests
from flask import Flask

app = Flask(__name__)


@app.route('/hexo-service/docker/lakeeee')
def restart_lakeeee():
    os.system("docker restart lakeeee")

    url = "http://127.0.0.1:4000"
    while True:
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                break
        except:
            print('try to connect %s failed.' % url)
            time.sleep(1)

    return "restart lakeeee success"


@app.route('/hexo-service/docker/nginx')
def restart_nginx():
    os.system("docker restart nginx")

    url = "http://127.0.0.1:80"
    while True:
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                break
        except:
            print('try to connect %s failed.' % url)
            time.sleep(1)

    return "restart nginx success"


@app.route('/hexo-service/git/pull')
def git_pull():
    os.system("cd /home/zhaoy/hexo-box/lakeeee && git pull origin master")
    return "git pull success"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
