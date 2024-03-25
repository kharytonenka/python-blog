from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    BLOG_TEST_TITLE_1 = "Blog Test Title 1"
    BLOG_TEST_AUTHOR_1 = "Blog Test Author 1"

    BLOG_TEST_TITLE_2 = "Blog Test Title 2"
    BLOG_TEST_AUTHOR_2 = "Blog Test Author 2"

    POST_TEST_TITLE = "Post Test Title"
    POST_TEST_CONTENT = "Post Test Content"

    def test_create_post(self):
        blog = Blog(BlogTest.BLOG_TEST_TITLE_1, BlogTest.BLOG_TEST_AUTHOR_1)
        blog.create_post(BlogTest.POST_TEST_TITLE, BlogTest.POST_TEST_CONTENT)

        self.assertEqual(1, len(blog.posts))
        self.assertEqual(blog.posts[0].title, BlogTest.POST_TEST_TITLE)
        self.assertEqual(blog.posts[0].content, BlogTest.POST_TEST_CONTENT)

    def test_repr_one_post(self):
        blog = Blog(BlogTest.BLOG_TEST_TITLE_1, BlogTest.BLOG_TEST_AUTHOR_1)
        post = Post(BlogTest.POST_TEST_TITLE, BlogTest.POST_TEST_CONTENT)
        blog.posts.append(post)

        repr_expected = f"{BlogTest.BLOG_TEST_TITLE_1} by {BlogTest.BLOG_TEST_AUTHOR_1} (1 post)"

        self.assertEqual(repr_expected, blog.__repr__())

    def test_repr_two_post(self):
        blog = Blog(BlogTest.BLOG_TEST_TITLE_1, BlogTest.BLOG_TEST_AUTHOR_1)
        post = Post(BlogTest.POST_TEST_TITLE, BlogTest.POST_TEST_CONTENT)
        blog.posts.append(post)
        blog.posts.append(post)

        repr_expected = f"{BlogTest.BLOG_TEST_TITLE_1} by {BlogTest.BLOG_TEST_AUTHOR_1} (2 posts)"

        self.assertEqual(repr_expected, blog.__repr__())

    def test_json_string(self):
        blog = Blog(BlogTest.BLOG_TEST_TITLE_1, BlogTest.BLOG_TEST_AUTHOR_1)
        blog.create_post(BlogTest.POST_TEST_TITLE, BlogTest.POST_TEST_CONTENT)

        json_blog_expected = ("{{'title': '{0}', 'author': '{1}', 'posts': [{{'title': '{2}', 'content': '{3}'}}]}}".
                              format(BlogTest.BLOG_TEST_TITLE_1,
                                     BlogTest.BLOG_TEST_AUTHOR_1,
                                     BlogTest.POST_TEST_TITLE,
                                     BlogTest.POST_TEST_CONTENT
                                     ))

        self.assertEqual(json_blog_expected, str(blog.json()))

    def test_json_dictionary(self):
        blog = Blog(BlogTest.BLOG_TEST_TITLE_1, BlogTest.BLOG_TEST_AUTHOR_1)
        blog.create_post(BlogTest.POST_TEST_TITLE, BlogTest.POST_TEST_CONTENT)

        json_blog_expected = {"title": BlogTest.BLOG_TEST_TITLE_1,
                              "author": BlogTest.BLOG_TEST_AUTHOR_1,
                              "posts": [{"title": BlogTest.POST_TEST_TITLE,
                                         "content": BlogTest.POST_TEST_CONTENT}]}

        self.assertEqual(json_blog_expected, blog.json())
