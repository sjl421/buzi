import redis

conn = None

def get_connection():
    global conn
    if not conn:
        conn = redis.StrictRedis()
    return conn