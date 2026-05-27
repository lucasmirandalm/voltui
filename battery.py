from __future__ import annotations

from dataclasses import dataclass

import psutil


@dataclass
class BatteryInfo:
    percent: int
    is_charging: bool
    seconds_left: int


def get_battery_info() -> BatteryInfo | None:
    battery = psutil.sensors_battery()

    if battery is None:
        return None

    return BatteryInfo(
        percent=round(battery.percent),
        is_charging=bool(battery.power_plugged),
        seconds_left=battery.secsleft,
    )


def get_battery_color(percent: int) -> str:
    if percent >= 51:
        return "green"

    if percent >= 26:
        return "yellow"

    return "red"


def format_time_left(seconds: int) -> str:
    if seconds == psutil.POWER_TIME_UNKNOWN:
        return ""

    if seconds == psutil.POWER_TIME_UNLIMITED:
        return ""

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    if hours > 0:
        return f"{hours}h {minutes}min remaining"

    return f"{minutes}min remaining"