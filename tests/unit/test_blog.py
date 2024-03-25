from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    BLOG_TEST_TITLE_1 = "Blog Test Title 1"
    BLOG_TEST_AUTHOR_1 = "Blog Test Author 1"

    BLOG_TEST_TITLE_2 = "Blog Test Title 2"
    BLOG_TEST_AUTHOR_2 = "Blog Test Author 2"

    def test_create_blog(self):
        blog = Blog(BlogTest.BLOG_TEST_TITLE_1, BlogTest.BLOG_TEST_AUTHOR_1)

        self.assertEqual(BlogTest.BLOG_TEST_TITLE_1, blog.title)
        self.assertEqual(BlogTest.BLOG_TEST_AUTHOR_1, blog.author)
        self.assertListEqual([], blog.posts)
        self.assertEqual(0, len(blog.posts))
        self.assertEqual([], blog.posts)
        self.assertTrue([] == blog.posts)

    def test_repr_zero_posts(self):
        blog_1 = Blog(BlogTest.BLOG_TEST_TITLE_1, BlogTest.BLOG_TEST_AUTHOR_1)
        repr_1_expected = f"{BlogTest.BLOG_TEST_TITLE_1} by {BlogTest.BLOG_TEST_AUTHOR_1} (0 posts)"

        blog_2 = Blog(BlogTest.BLOG_TEST_TITLE_2, BlogTest.BLOG_TEST_AUTHOR_2)
        repr_2_expected = f"{BlogTest.BLOG_TEST_TITLE_2} by {BlogTest.BLOG_TEST_AUTHOR_2} (0 posts)"

        self.assertEqual(repr_1_expected, blog_1.__repr__())
        self.assertEqual(repr_2_expected, blog_2.__repr__())
