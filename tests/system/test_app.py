from unittest import TestCase
from unittest.mock import patch
from blog import Blog
import app


class AppTest(TestCase):
    BLOG_TEST_TITLE_1 = "Blog Test Title 1"
    BLOG_TEST_AUTHOR_1 = "Blog Test Author 1"

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_print:
            app.menu()
            mocked_print.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog(AppTest.BLOG_TEST_TITLE_1, AppTest.BLOG_TEST_AUTHOR_1)
        app.blogs[AppTest.BLOG_TEST_TITLE_1] = blog

        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(f"-{AppTest.BLOG_TEST_TITLE_1} by {AppTest.BLOG_TEST_AUTHOR_1} (0 posts)")
