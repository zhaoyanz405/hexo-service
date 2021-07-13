# -*- coding: utf-8 -*-
import os

from flask import Flask

app = Flask(__name__)


@app.route('/hexo-service/docker/lakeeee')
def restart_lakeeee():
    os.system("docker restart lakeeee")
    return "restart lakeeee success"


@app.route('/hexo-service/docker/nginx')
def restart_nginx():
    os.system("docker restart nginx")
    return "restart nginx success"


@app.route('/hexo-service/git/pull')
def git_pull():
    os.system("cd /home/zhaoy/hexo-box/lakeeee && git pull origin master")
    return "git pull success"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
