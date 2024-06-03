import redis
import pytest

@pytest.fixture(scope="module")
def redis_client():
    client = redis.Redis(host='localhost', port=6379)
    yield client
    client.flushall()  # Clean up after tests

def test_redis_connection(redis_client):
    assert redis_client.ping() == True

def test_set_get(redis_client):
    redis_client.set('mykey', 'Hello, Redis!')
    value = redis_client.get('mykey').decode('utf-8')
    assert value == 'Hello, Redis!'

def test_appendonly(redis_client):
    config_value = redis_client.config_get('appendonly')['appendonly']
    assert config_value == 'yes'