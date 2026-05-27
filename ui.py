from __future__ import annotations

from rich.align import Align
from rich.console import Group
from rich.text import Text

from battery import BatteryInfo, format_time_left, get_battery_color
from config import BATTERY_WIDTH


def build_battery_body(percent: int, color: str) -> Text:
    filled_size = round((percent / 100) * BATTERY_WIDTH)
    empty_size = BATTERY_WIDTH - filled_size

    battery = Text()

    battery.append("╭", style="bold white")
    battery.append("─" * BATTERY_WIDTH, style="bold white")
    battery.append("╮", style="bold white")
    battery.append("╭╮\n", style="bold white")

    battery.append("│", style="bold white")
    battery.append("█" * filled_size, style=f"bold {color}")
    battery.append("░" * empty_size, style="dim white")
    battery.append("│", style="bold white")
    battery.append("││\n", style="bold white")

    battery.append("╰", style="bold white")
    battery.append("─" * BATTERY_WIDTH, style="bold white")
    battery.append("╯", style="bold white")
    battery.append("╰╯", style="bold white")

    return battery


def build_screen(
    battery_info: BatteryInfo,
    loading_frame: str,
    terminal_height: int,
) -> Align:
    color = get_battery_color(battery_info.percent)

    title = Text("VoltUI", style="bold white")
    battery_body = build_battery_body(battery_info.percent, color)
    percentage = Text(f"\n{battery_info.percent}%\n", style=f"bold {color}")

    if battery_info.is_charging:
        status = Text(f"{loading_frame} Charging...", style=f"bold {color}")
        time_left = Text("")
    else:
        status = Text("On battery", style="bold white")
        time_left = Text(
            format_time_left(battery_info.seconds_left),
            style=f"bold {color}",
        )

    content = Group(
        Align.center(title),
        Text(""),
        Align.center(battery_body),
        Align.center(percentage),
        Align.center(status),
        Align.center(time_left),
    )

    return Align.center(
        content,
        vertical="middle",
        height=terminal_height,
    )


def build_error_screen(terminal_height: int) -> Align:
    return Align.center(
        Text("Battery not detected.", style="bold red"),
        vertical="middle",
        height=terminal_height,
    )