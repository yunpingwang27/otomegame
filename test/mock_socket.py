from collections import deque

class MockSocket:
    def __init__(self, logger):
        self.logger = logger
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def is_connected(self):
        return self.connected

    def communicate(self, message):
        pass

class ResponseTestMockSocket(MockSocket):
    def __init__(self, logger):
        super().__init__(logger)
        self.responses = deque()

    def communicate(self, message):
        return self.responses.popleft()

    def add(self, responses):
        for response in responses:
            self.responses.append(response)
