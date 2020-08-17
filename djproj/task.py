from __future__ import absolute_import, unicode_literals

from cel import app
import requests
import hashlib

@app.task(name='get_md5')
def get_md5(url):
    try:
        r = requests.get(url, timeout=(5, 600))
        if r.status_code != 200:
            return (r.status_code, Exception(f"bad status code: {r.status_code}"))
        return (r.status_code, hashlib.md5(r.content).hexdigest())
    except Exception as e:
        return ("Unknown", str(e))
