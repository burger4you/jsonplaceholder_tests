import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, path: str):
        return r.post(url=JSONPLACEHOLDER_HOST + path)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def get_all_posts_by_user_id(self, user_id: int):
        return self._get(path=f'/posts?user_id={user_id}')

    @allure.step
    def create_post(self):
        return self._post(path=f'/posts')

    @allure.step
    def create_invalid_post(self):
        return self._post(path=f'/posts/1')
