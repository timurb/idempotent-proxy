from flask import Flask
from flask import request

import object_storage
from proxy import ApiProxy

app = Flask(__name__)


@app.route("/api", methods=['GET'])
def api_get():
    return proxy.get


@app.route("/api", methods=['POST'])
def api_post():
    data = request.get_json(force=True)
    if not storage.is_valid(data):
        return 400, 'Malformed request'

    if storage.check(data):
        return 200, 'NO CHANGE'
    else:
        resp = proxy.get()
        storage.put(data)
        return resp


if __name__ == "__main__":
    storage = object_storage.ObjectStorage()
    proxy = ApiProxy('https://www.google.com/?q=foobar')
    app.run()
