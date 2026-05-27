from __future__ import annotations

import time

from rich.console import Console
from rich.live import Live

from battery import get_battery_info
from config import LOADING_FRAMES, REFRESH_SECONDS
from ui import build_error_screen, build_screen


def main() -> None:
    battery_info = get_battery_info()

    if battery_info is None:
        print("Could not detect a battery on this computer.")
        print("This can happen on desktops, virtual machines, or unsupported systems.")
        return

    console = Console()
    frame_index = 0

    with Live(refresh_per_second=10, screen=True, console=console) as live:
        while True:
            battery_info = get_battery_info()
            terminal_height = console.size.height

            if battery_info is None:
                live.update(build_error_screen(terminal_height))
                time.sleep(REFRESH_SECONDS)
                continue

            loading_frame = LOADING_FRAMES[frame_index % len(LOADING_FRAMES)]

            live.update(
                build_screen(
                    battery_info=battery_info,
                    loading_frame=loading_frame,
                    terminal_height=terminal_height,
                )
            )

            frame_index += 1
            time.sleep(REFRESH_SECONDS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nVoltUI closed.")