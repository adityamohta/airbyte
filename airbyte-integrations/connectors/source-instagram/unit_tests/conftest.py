#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from typing import List

from facebook_business import FacebookAdsApi, FacebookSession
from pytest import fixture
from source_instagram.api import InstagramAPI as API


FB_API_VERSION = FacebookAdsApi.API_VERSION


@fixture(autouse=True)
def mock_sleep(mocker):
    mocker.patch("time.sleep")


@fixture(scope="session", name="account_id")
def account_id_fixture():
    return "unknown_account"


@fixture(name="config")
def config_fixture():
    config = {
        "access_token": "TOKEN",
        "start_date": "2022-03-20T00:00:00",
    }

    return config


@fixture(scope="session", name="some_config")
def some_config_fixture(account_id):
    return {"start_date": "2021-01-23T00:00:00Z", "access_token": "unknown_token"}


@fixture(scope="session", name="some_config_future_date")
def some_config_future_date_fixture(account_id):
    return {"start_date": "2030-01-23T00:00:00Z", "access_token": "unknown_token"}


@fixture(name="fb_account_response")
def fb_account_response_fixture(account_id, some_config, requests_mock):
    account = {"id": "test_id", "instagram_business_account": {"id": "test_id"}}
    requests_mock.register_uri(
        "GET",
        FacebookSession.GRAPH + f"/{FB_API_VERSION}/act_{account_id}/"
        f"?access_token={some_config['access_token']}&fields=instagram_business_account",
        json=account,
    )
    return {
        "json": {
            "data": [
                {
                    "access_token": "access_token",
                    "category": "Software company",
                    "id": f"act_{account_id}",
                    "paging": {"cursors": {"before": "cursor", "after": "cursor"}},
                    "summary": {"total_count": 1},
                    "status_code": 200,
                }
            ]
        }
    }


@fixture(name="api")
def api_fixture(some_config, requests_mock, fb_account_response):
    api = API(access_token=some_config["access_token"])

    requests_mock.register_uri(
        "GET",
        FacebookSession.GRAPH + f"/{FB_API_VERSION}/me/accounts?" f"access_token={some_config['access_token']}&summary=true",
        [fb_account_response],
    )

    return api


@fixture(name="user_insight_data")
def user_insight_data_fixture():
    return {
        "name": "reach",
        "period": "day",
        "values": [{"value": 4, "end_time": "2020-05-04T07:00:00+0000"}, {"value": 66, "end_time": "2020-05-05T07:00:00+0000"}],
        "title": "Reach",
        "description": "Total number of times this profile has been uniquely viewed",
        "id": "17841400008460056/insights/reach/day",
    }


@fixture(name="user_insights")
def user_insights():
    class UserInsightEntityMock:
        # reference Issue:
        # https://github.com/airbytehq/airbyte/issues/24697
        class UserInsight:
            def __init__(self, values: dict):
                self.data = {
                    "description": "test_insight",
                    "id": "123",
                    "name": "test_insight_metric",
                    "period": "day",
                    "title": "Test Insight",
                    "values": [values],
                }

            def __dict__(self):
                return self.data

            def export_all_data(self):
                return self.__dict__()

        def __new__(cls, values: dict):
            cls.insights = [cls.UserInsight(values)]

        @classmethod
        def get(cls, element):
            return cls.insights[0].__dict__()[element]

        @classmethod
        def get_insights(cls, **kwargs) -> List[dict]:
            return cls.insights

    return UserInsightEntityMock


@fixture(name="user_stories_data")
def user_stories_data_fixture():
    return {"id": "test_id"}
