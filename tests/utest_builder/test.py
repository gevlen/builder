from __future__ import annotations

from unittest import TestCase

from fastapi.testclient import TestClient

from src.asgi import create_app

from tests.utest_builder.data import forward_interest
from tests.utest_builder.data import not_found


class BuilderTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app=create_app())  # type: ignore

    def test_get_tasks_positive(self):
        response = self.client.post(
            url="/builder/get_tasks", json={"build": "forward_interest"}
        )
        self.assertEqual(
            first=(response.status_code, response.json()),
            second=(200, forward_interest),
            msg=(
                f"response code: {response.status_code}, must be: 200 OK"
                f"content: {response.content} must be b'{forward_interest}'"
            ),
        )

    def test_get_tasks_negative(self):
        response = self.client.post(
            url="/builder/get_tasks", json={"build": "no_such_build_name"}
        )
        self.assertEqual(
            first=(response.status_code, response.json()),
            second=(404, not_found),
            msg=(
                f"response code: {response.status_code}, must be: 404 NOT FOUND"
                f"content: {response.content} must be b'{not_found}'"
            ),
        )
        response = self.client.post(
            url="/builder/get_tasks", json={"task": "forward_interest"}
        )
        self.assertEqual(
            first=response.status_code,
            second=422,
            msg=(
                f"response code: {response.status_code}, must be: 422 Validation ERROR"
            ),
        )
