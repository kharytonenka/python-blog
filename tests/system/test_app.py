from unittest import TestCase
from unittest.mock import patch
from blog import Blog
from post import Post
import app


class AppTest(TestCase):
    BLOG_TEST_TITLE_1 = "Blog Test Title 1"
    BLOG_TEST_AUTHOR_1 = "Blog Test Author 1"

    POST_TEST_TITLE = "Post Test Title"
    POST_TEST_CONTENT = "Post Test Content"

    def test_menu_calls_create_blog_1(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("c", AppTest.BLOG_TEST_TITLE_1, AppTest.BLOG_TEST_AUTHOR_1, "q")
            app.menu()
            self.assertIsNotNone(app.blogs[AppTest.BLOG_TEST_TITLE_1])

    def test_menu_calls_create_blog_2(self):
        with patch("builtins.input") as mocked_input:
            # "ask_create_blog" is not executed, as it's being mocked, but we can check that it is called
            with patch("app.ask_create_blog") as mocked_ask_create_blog:
                mocked_input.side_effect = ("c", "q")
                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_menu_prints_prompt(self):
        with patch("builtins.input", return_value="q") as mocked_print:
            app.menu()
            mocked_print.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch('builtins.input', return_value="q"):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog(AppTest.BLOG_TEST_TITLE_1, AppTest.BLOG_TEST_AUTHOR_1)
        app.blogs[AppTest.BLOG_TEST_TITLE_1] = blog

        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(f"-{AppTest.BLOG_TEST_TITLE_1} by {AppTest.BLOG_TEST_AUTHOR_1} (0 posts)")

    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = (AppTest.BLOG_TEST_TITLE_1, AppTest.BLOG_TEST_AUTHOR_1)
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get(AppTest.BLOG_TEST_TITLE_1))

    def test_ask_read_blog(self):
        blog = Blog(AppTest.BLOG_TEST_TITLE_1, AppTest.BLOG_TEST_AUTHOR_1)
        app.blogs[AppTest.BLOG_TEST_TITLE_1] = blog

        with patch("builtins.input", return_value=AppTest.BLOG_TEST_TITLE_1):
            with patch("app.print_posts") as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog(AppTest.BLOG_TEST_TITLE_1, AppTest.BLOG_TEST_AUTHOR_1)
        blog.create_post(AppTest.POST_TEST_TITLE, AppTest.POST_TEST_CONTENT)
        app.blogs[AppTest.BLOG_TEST_TITLE_1] = blog

        with patch("app.print_post") as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post(AppTest.POST_TEST_TITLE, AppTest.POST_TEST_CONTENT)

        with patch("builtins.print") as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(
                app.POST_TEMPLATE.format(AppTest.POST_TEST_TITLE, AppTest.POST_TEST_CONTENT))

    def test_ask_create_post(self):
        blog = Blog(AppTest.BLOG_TEST_TITLE_1, AppTest.BLOG_TEST_AUTHOR_1)
        app.blogs[AppTest.BLOG_TEST_TITLE_1] = blog

        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = (AppTest.BLOG_TEST_TITLE_1, AppTest.POST_TEST_TITLE, AppTest.POST_TEST_CONTENT)
            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, AppTest.POST_TEST_TITLE)
            self.assertEqual(blog.posts[0].content, AppTest.POST_TEST_CONTENT)
