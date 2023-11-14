import time
import redis
#import os
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
def get_hit_count():
	retries = 5
	while True:
		try:
			return cache.incr('hits')
		except redis.exceptions.ConnectionError as exc:
			if retries == 0:
				raise exc
			retries -= 1
			time.sleep(0.5)
@app.route('/')
def hello():
	#os._exit(0)
	count = get_hit_count()
	return 'Hola que tal! Este siitio se ha visitado {} veces.\n'.format(count)
