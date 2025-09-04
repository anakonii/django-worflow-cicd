from django.test import TestCase
from posts.models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post", body="This is a test post.")
    
    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.body, "This is a test post.")

    def test_post_created_field(self):
        self.assertIsNotNone(self.post.created)