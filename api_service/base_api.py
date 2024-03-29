import requests


class BaseApi:

    def __execute_request(self, method, url, params=None, body=None, headers=None):

        return requests.request(
            method=method,
            url=url,
            params=params or {},
            data=body,
            headers=headers or {}
        )

    def get(self, url, params=None, headers=None):
        return self.__execute_request('get', url=url, params=params, headers=headers)

    def post(self, url, body=None, headers=None):
        return self.__execute_request('post', url=url, body=body, headers=headers)

    def put(self, url, body=None, headers=None):
        return self.__execute_request('put', url=url, body=body, headers=headers)

    def delete(self, url=None, headers=None):
        return self.__execute_request('delete', url=url, headers=headers)
