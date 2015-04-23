import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# def add_trip(user_id, trip_data, trip_start_timestamp, size_limit = 10):
# 	""" Add trip data to sorted set and remove older data 
# 		if set length exceeds size_limit."""
# 	

from numpy.random import random,shuffle
key = str(random())

def p(): 
	print r.zrange(key,0,-1)

nums = range(1,16)
shuffle(nums)
x = [(n,str(n)) for n in nums]

for score,val in x: 
	r.zadd(key,score,val)	
	p()


def trim_to_highest(key,n):
	""" Trim sorted set to n elements, removing elements 
		with lowest scores. """
	r.zremrangebyrank(key,0,-(n+1))

trim_to_highest(key,10)
p()
print r.zcard(key)