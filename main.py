# -*- coding: utf-8 -*-
import os

from flask import Flask

app = Flask(__name__)


@app.route('/docker/lakeeee')
def restart_lakeeee():
    os.system("docker restart lakeeee")
    return "success"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
