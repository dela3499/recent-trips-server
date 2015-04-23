import redis
import numpy.random as npr
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def p(key): 
	print r.zrange(key,0,-1)

def trim_to_highest(key,n):
	""" Trim sorted set to n elements, removing elements 
		with lowest scores. Returns number of elements removed."""
	return r.zremrangebyrank(key,0,-(n+1))

def add_trip(user_id, trip_data, trip_start_timestamp, size_limit = 10):
	""" Add trip data to sorted set and remove older data 
		if set length exceeds size_limit."""
	r.zadd(user_id, trip_start_timestamp, trip_data)
	trim_to_highest(user_id, size_limit)

n_users = 100
n_trips = 1000

user_ids = [str(int(xi * 10000)) for xi in npr.random(n_users)]
#print user_ids
trip_user_ids = [npr.choice(user_ids) for _ in range(n_trips)]
trip_datas = [str(xi) for xi in npr.random(n_trips)]
trip_start_times = [int(xi) for xi in npr.random(n_trips)]

for user_id, trip_data, trip_start_time in zip(trip_user_ids, trip_datas, trip_start_times):
	add_trip(user_id, trip_data, trip_start_time)

for user_id in user_ids[:10]:
	#p(user_id)
	print r.zcard(user_id)