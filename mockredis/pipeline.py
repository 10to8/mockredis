from mockredis.redis import MockRedis


class MockRedisPipeline(MockRedis):
    """
    Imitate a redis-python pipeline object
    so unit tests can run without needing a
    real Redis server.
    """

    def __init__(self, redis, timeouts, client):
        """Initialize the object."""
        self.redis = redis
        self.timeouts = timeouts
        self.client = client
        self.results = []

    @property
    def shas(self):
        return self.client.shas

    def execute(self):
        """
        Emulate the execute method. All piped
        commands are executed immediately
        in this mock, so this is a no-op.

        We're still interested in the results though.

        """
        results = self.results
        self.results = []
        return results

    def __exit__(self, *argv, **kwargs):
        pass

    def __enter__(self, *argv, **kwargs):
        return self
