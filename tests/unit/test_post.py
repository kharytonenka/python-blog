from unittest import TestCase
from post import Post


class PostTest(TestCase):
    POST_TEST_TITLE = "Post Test Title"
    POST_TEST_CONTENT = "Post Test Content"

    def test_create_post(self):
        post = Post(PostTest.POST_TEST_TITLE, PostTest.POST_TEST_CONTENT)

        self.assertEqual(PostTest.POST_TEST_TITLE, post.title)
        self.assertEqual(PostTest.POST_TEST_CONTENT, post.content)

    def test_json_1(self):
        post = Post(PostTest.POST_TEST_TITLE, PostTest.POST_TEST_CONTENT)

        self.assertEqual(PostTest.POST_TEST_TITLE, post.json()["title"])
        self.assertEqual(PostTest.POST_TEST_CONTENT, post.json()["content"])

    def test_json_2(self):
        post = Post(PostTest.POST_TEST_TITLE, PostTest.POST_TEST_CONTENT)
        json_post_expected = {"title": PostTest.POST_TEST_TITLE, "content": PostTest.POST_TEST_CONTENT}

        self.assertDictEqual(json_post_expected, post.json())

    def test_str(self):
        post = Post(PostTest.POST_TEST_TITLE, PostTest.POST_TEST_CONTENT)
        str_expected = f"{{'title': '{PostTest.POST_TEST_TITLE}', 'content': '{PostTest.POST_TEST_CONTENT}'}}"

        self.assertEqual(str_expected, str(post))

    def test_repr(self):
        post = Post(PostTest.POST_TEST_TITLE, PostTest.POST_TEST_CONTENT)
        repr_expected = "{'title': '%s', 'content': '%s'}" % (PostTest.POST_TEST_TITLE, PostTest.POST_TEST_CONTENT)

        self.assertEqual(repr_expected, post.__repr__())
