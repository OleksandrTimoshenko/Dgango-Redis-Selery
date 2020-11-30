from django.test import TestCase, Client


class TestGetSomething(TestCase):
    def test_root_url(self):
        path = "/"
        client = Client()
        response = client.get(path=path)
        self.assertEqual(response.status_code, 302)

    def test_movies_url(self):
        path = "/movies"
        client = Client()
        response = client.get(path=path)
        self.assertEqual(response.status_code, 301)
