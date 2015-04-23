import redis
import numpy.random as npr
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def trim_to_highest(key,n):
	""" Trim sorted set to n elements, removing elements 
		with lowest scores. Returns number of elements removed."""
	return r.zremrangebyrank(key,0,-(n+1))

def add_trip(user_id, trip_data, trip_start_timestamp, size_limit = 10):
	""" Add trip data to sorted set and remove older data 
		if set length exceeds size_limit."""
	r.zadd(user_id, trip_start_timestamp, trip_data)
	trim_to_highest(user_id, size_limit)

def get_trips(user_id):
	"""Return trip_data for user."""
	return r.zrange(user_id,0,-1)

