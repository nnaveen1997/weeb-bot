import redis
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def getConnection():
    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    return redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)



