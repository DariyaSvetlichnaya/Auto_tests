import json

from api_service.base_api import BaseApi
from utils.api_config_manager import ConfigManager


class EventsApi:

    api_executor = BaseApi()

    token = {'Authorization': 'Bearer xfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX0NLZ0VYVmc2UyIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiJkc3ZpdGx5Y2huYS1sY2ciLCJjdXN0b206ZW50cnlfcG9pbnQiOiJodHRwczpcL1wvbXlldm9sdi5zYnguZXZvbHZkZXZlbG9wbWVudC5jb20iLCJhdWQiOiI2NTZmcDJtMDJwdnMzajRiMzFvc280cmNucCIsImN1c3RvbTppc19mZWRlcmF0ZWQiOiIwIiwiZXZlbnRfaWQiOiIzZGE2MzdiZS04ZDljLTQ3MzQtYjMxYy1iZTYwMGVhMDdjZmUiLCJ0b2tlbl91c2UiOiJpZCIsImN1c3RvbTp0YWJsZWF1X3VzZXIiOiJkc3ZpdGx5Y2huYS1sY2ciLCJhdXRoX3RpbWUiOjE3MTQ3NDYyNDYsImV4cCI6MTcxNDg1NzE2MywiaWF0IjoxNzE0ODU2ODY0LCJlbWFpbCI6ImRzdml0bHljaG5hQGV2b2x2dGVjaG5vbG9neS5jb20ifQ.mN9nuajzqFJtv_rVOkFBCxpV8-_V2ZfOv31FlCE9ZBrSsQ107ufXF4xHypSCk8KiGxid573apy9HkNUJI0OdsAbug-WwslzhQku_xQKPpzcO7s8TR27pfbKbrtteiNeThdom1iUJhmT0EkG4MEDxao0jScRonNPRTO8ajfxrcnbHAB9f-480Mc3UIXgTZ7KtKqRpTnqGsGQjjbd1wXf1WI4dPtmyoevGOk7adWBc5_mFyfjOgZFkXCTE81c1PhxddS92gQ8le4vaYCm-5qOL99a_WRzrVxkJYBWc6_sTLaQ6UVMIjZzjMqOYSvnzDtREzbSRtl8lKC_AluCE4t7zzA'}

    def get_all_events(self, headers=None, use_default_token=True):

        if headers and use_default_token:
            headers.update(self.token)

        return (self.api_executor.get(
            url=ConfigManager.all_events_url,
            headers=headers or self.token
        ))

    def create_events(self, body, headers=None, use_default_token=True):

        if headers and use_default_token:
            headers.update(self.token)

        return self.api_executor.post(
            url=ConfigManager.create_events_url,
            headers=headers or self.token,
            body=json.dumps(body)
        )

    def get_event_by_id(self, headers=None, use_default_token=True):

        if headers and use_default_token:
            headers.update(self.token)

        return (self.api_executor.get(
            url=ConfigManager.event_by_id_url,
            headers=headers or self.token
        ))

    def delete_event(self, headers=None, use_default_token=True):
        if headers and use_default_token:
            headers.update(self.token)

        return (self.api_executor.get(
            url=ConfigManager.delete_event_url,
            headers=headers or self.token
        ))

    def delete_wrong_event(self, headers=None, use_default_token=True):
        if headers and use_default_token:
            headers.update(self.token)

        return (self.api_executor.get(
            url=ConfigManager.delete_wrong_event_url,
            headers=headers or self.token
        ))

    def get_events_sample_file(self, headers=None, use_default_token=True):

        if headers and use_default_token:
            headers.update(self.token)

        return (self.api_executor.get(
            url=ConfigManager.events_sample_file_url,
            headers=headers or self.token
        ))
