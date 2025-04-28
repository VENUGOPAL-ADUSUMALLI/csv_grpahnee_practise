import redis

# Connect to Redis (host='localhost' & default port 6379)
r = redis.Redis(host='localhost', port=6379, db=0)

# 1️⃣ Set a key-value pair in Redis
r.set('name', 'venu')

# 2️⃣ Get the value back from Redis
value = r.get('name')  # It returns bytes, so we decode
print(value.decode())  # Output: venu
