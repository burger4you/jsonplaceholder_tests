import allure
from framework.check import check_get_all_posts_response, check_get_post_response, check_not_found_posts, \
    check_post_is_created, check_post_is_not_created

check_post_is_created, check_post_is_not_created
from framework.jsonplaceholder_client import Client


@allure.suite('POST /posts')
class TestCreatePosts:

    @allure.title('Positive. Create  post')
    def test_create_post(self):
        response = Client().create_post()
        check_post_is_created(response)

    @allure.title('Negative. Create  post')
    def test_create_invalid_post(self):
        response = Client().create_invalid_post()
        check_post_is_not_created(response)
