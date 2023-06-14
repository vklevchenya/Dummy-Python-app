import unittest
from app import app

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        response = self.app.post('/todos', json={'title': 'Sample todo'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()

# test commit