import json

from api_service.base_api import BaseApi


class EventsApi:

    api_executor = BaseApi()
    base_url = "https://rmzq829cg3.execute-api.us-east-1.amazonaws.com/sbx/api"
    all_events_url = f"{base_url}/v3/customers/AppTest/events"
    create_events_url = f"{base_url}/v3/customers/AppTest/events-batch"

    token = {'Authorization': 'Bearer eyJraWQiOiJzXC83Q3lJTWhIRGFHZVFWaFM4QjhKZVhGdmJTSElVUWVieWdQOGVUaGltWT0iLCJhbGciOiJSUzI1NiJ9.eyJjdXN0b206dHlwZSI6ImFkbWluIiwic3ViIjoiZmRkMjU1MDUtMjUyYi00OTBmLWIxNTktOGQ4NTQ2Njc5OWJiIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX0NLZ0VYVmc2UyIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiJkc3ZpdGx5Y2huYS1sY2ciLCJjdXN0b206ZW50cnlfcG9pbnQiOiJodHRwczpcL1wvbXlldm9sdi5zYnguZXZvbHZkZXZlbG9wbWVudC5jb20iLCJhdWQiOiI2NTZmcDJtMDJwdnMzajRiMzFvc280cmNucCIsImN1c3RvbTppc19mZWRlcmF0ZWQiOiIwIiwiZXZlbnRfaWQiOiIzZGE2MzdiZS04ZDljLTQ3MzQtYjMxYy1iZTYwMGVhMDdjZmUiLCJ0b2tlbl91c2UiOiJpZCIsImN1c3RvbTp0YWJsZWF1X3VzZXIiOiJkc3ZpdGx5Y2huYS1sY2ciLCJhdXRoX3RpbWUiOjE3MTQ3NDYyNDYsImV4cCI6MTcxNDg1NzE2MywiaWF0IjoxNzE0ODU2ODY0LCJlbWFpbCI6ImRzdml0bHljaG5hQGV2b2x2dGVjaG5vbG9neS5jb20ifQ.mN9nuajzqFJtv_rVOkFBCxpV8-_V2ZfOv31FlCE9ZBrSsQ107ufXF4xHypSCk8KiGxid573apy9HkNUJI0OdsAbug-WwslzhQku_xQKPpzcO7s8TR27pfbKbrtteiNeThdom1iUJhmT0EkG4MEDxao0jScRonNPRTO8ajfxrcnbHAB9f-480Mc3UIXgTZ7KtKqRpTnqGsGQjjbd1wXf1WI4dPtmyoevGOk7adWBc5_mFyfjOgZFkXCTE81c1PhxddS92gQ8le4vaYCm-5qOL99a_WRzrVxkJYBWc6_sTLaQ6UVMIjZzjMqOYSvnzDtREzbSRtl8lKC_AluCE4t7zzA'}

    def get_all_events(self, headers=None, use_default_token=True):

        if headers and use_default_token:
            headers.update(self.token)

        return (self.api_executor.get(
            url=self.all_events_url,
            headers=headers or self.token
        ))

    def create_events(self, body, headers=None, use_default_token=True):

        if headers and use_default_token:
            headers.update(self.token)

        return self.api_executor.post(
            url=self.create_events_url,
            headers=headers or self.token,
            body=json.dumps(body)
        )
