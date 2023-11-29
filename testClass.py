from datetime import datetime

class TestClass:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = TestClass(email='leila@example.com', content='foo bar')