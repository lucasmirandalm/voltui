from types import SimpleNamespace

import psutil

from battery import (
    BatteryInfo,
    format_time_left,
    get_battery_color,
    get_battery_info,
)


def test_battery_color_green() -> None:
    assert get_battery_color(100) == "green"
    assert get_battery_color(51) == "green"


def test_battery_color_yellow() -> None:
    assert get_battery_color(50) == "yellow"
    assert get_battery_color(26) == "yellow"


def test_battery_color_red() -> None:
    assert get_battery_color(25) == "red"
    assert get_battery_color(0) == "red"


def test_format_time_in_minutes() -> None:
    assert format_time_left(1800) == "30min remaining"


def test_format_time_in_hours_and_minutes() -> None:
    assert format_time_left(5400) == "1h 30min remaining"


def test_return_empty_string_on_loading_condition() -> None:
    assert format_time_left(psutil.POWER_TIME_UNKNOWN) == ""


def test_return_none_when_battery_is_undetected(monkeypatch) -> None:
    monkeypatch.setattr(psutil, "sensors_battery", lambda: None)

    assert get_battery_info() is None


def test_return_battery_info(monkeypatch) -> None:
    fake_battery = SimpleNamespace(
        percent=87.6,
        power_plugged=True,
        secsleft=3600,
    )

    monkeypatch.setattr(psutil, "sensors_battery", lambda: fake_battery)

    battery_info = get_battery_info()

    assert battery_info == BatteryInfo(
        percent=88,
        is_charging=True,
        seconds_left=3600,
    )