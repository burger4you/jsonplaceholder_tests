import allure
from hamcrest import assert_that, equal_to
from requests import codes


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


def _response_ok_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


def _response_not_found_check(response, expected_code=codes.not_found):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(100))


@allure.step
def check_get_post_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(1))


@allure.step
def check_not_found_posts(response):
    _response_not_found_check(response)


@allure.step
def check_post_is_created(response):
    _response_ok_check(response)


@allure.step
def check_post_is_not_created(response):
    _response_not_found_check(response)
