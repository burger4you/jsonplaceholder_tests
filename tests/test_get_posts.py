import allure
from framework.check import check_get_all_posts_response, check_get_post_response, check_not_found_posts
from framework.jsonplaceholder_client import Client


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self):
        response = Client().get_all_posts()
        check_get_all_posts_response(response)

    @allure.title('Positive. Get post by id')
    def test_get_post_by_id(self):
        response = Client().get_post_by_id(1)
        check_get_post_response(response)

    @allure.title('Negative. Get post by id')
    def test_get_post_by_id(self):
        response = Client().get_post_by_id(101)
        check_not_found_posts(response)

    @allure.title('Positive. Get post by user_id')
    def test_get_all_posts_by_user_id(self):
        response = Client().get_all_posts_by_user_id(1)
        check_get_post_response(response)
