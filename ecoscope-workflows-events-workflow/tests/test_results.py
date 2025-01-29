# AUTOGENERATED BY ECOSCOPE-WORKFLOWS; see fingerprint in README.md for details

import asyncio
from typing import Any, Coroutine

import pytest
import pytest_check.context_manager
from syrupy import SnapshotAssertion
from syrupy.matchers import path_type


def test_failure_response(
    response_json_failure: dict, snapshot_json: SnapshotAssertion
):
    error = response_json_failure["error"]
    trace = response_json_failure["trace"]
    assert isinstance(error, str)
    assert isinstance(trace, str)

    assert trace.startswith("Traceback (most recent call last):\n ")
    assert trace.strip().endswith(error)

    exclude_trace = {"trace": (str,)}
    matcher = path_type(exclude_trace)
    assert response_json_failure == snapshot_json(matcher=matcher)


def test_dashboard_json(response_json_success: dict, snapshot_json: SnapshotAssertion):
    exclude_results_data = {
        f"result.views.{key}.{i}.data": (str,)
        for key in response_json_success["result"]["views"]
        for i, _ in enumerate(response_json_success["result"]["views"][key])
    }
    matcher = path_type(exclude_results_data)
    assert response_json_success == snapshot_json(matcher=matcher)


@pytest.mark.asyncio
async def test_iframes(
    snapshot_png: SnapshotAssertion,
    screenshot_coros: list[Coroutine[Any, Any, tuple[str, bytes]]],
    check: pytest_check.context_manager.CheckContextManager,
):
    screenshots = await asyncio.gather(*screenshot_coros)
    assert len(screenshots) >= 1, "No screenshots taken"
    for widget_title, actual_png in screenshots:
        with check:
            assert actual_png == snapshot_png(name=widget_title.replace(" ", "_"))
