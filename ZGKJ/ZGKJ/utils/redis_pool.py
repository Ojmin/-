import redis
from redis import StrictRedis
from goods.models import OrderInfo
# 抽取封装成模块，全局使用（单例模式，redis_pool.py）
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=1000, decode_responses=True)

