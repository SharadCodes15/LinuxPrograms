"""Live Linux network speed monitor for the terminal."""

from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Footer, Header, Static


NETWORK_ROOT = Path("/sys/class/net")


@dataclass(frozen=True)
class Counters:
	received: int = 0
	transmitted: int = 0


def read_counters() -> tuple[Counters, list[str]]:
	"""Read aggregate RX/TX counters for active non-loopback interfaces."""
	total = Counters()
	interfaces: list[str] = []

	for interface_path in sorted(NETWORK_ROOT.iterdir()):
		if interface_path.name == "lo":
			continue

		try:
			state = (interface_path / "operstate").read_text().strip()
			received = int((interface_path / "statistics/rx_bytes").read_text())
			transmitted = int((interface_path / "statistics/tx_bytes").read_text())
		except (OSError, ValueError):
			continue

		if state == "up":
			interfaces.append(interface_path.name)
			total = Counters(
				received=total.received + received,
				transmitted=total.transmitted + transmitted,
			)

	return total, interfaces


def format_rate(bytes_per_second: float) -> str:
	"""Format a byte rate using binary units."""
	units = ("B/s", "KiB/s", "MiB/s", "GiB/s")
	value = max(0.0, bytes_per_second)
	unit_index = 0
	while value >= 1024 and unit_index < len(units) - 1:
		value /= 1024
		unit_index += 1
	return f"{value:6.2f} {units[unit_index]}"


class NetSpeedApp(App[None]):
	"""Interactive Textual dashboard for Linux network throughput."""

	TITLE = "NETSPEED"
	SUB_TITLE = "Linux network monitor"

	CSS = """
	Screen {
		background: #10161b;
		color: #d7e2e8;
	}

	Header {
		background: #18252b;
		color: #8de0c2;
	}

	#dashboard {
		width: 100%;
		height: 1fr;
		padding: 1 2;
	}

	#rates {
		height: auto;
		min-height: 8;
	}

	.metric {
		width: 1fr;
		height: 8;
		margin: 0 1 1 0;
		padding: 1 2;
		border: round #31515a;
		background: #162126;
	}

	.metric-title {
		color: #90aab2;
		text-style: bold;
	}

	.metric-value {
		margin-top: 1;
		color: #8de0c2;
		text-style: bold;
	}

	#status {
		height: auto;
		margin-top: 1;
		padding: 1 2;
		border-left: thick #e3b86b;
		background: #162126;
		color: #b6c8cd;
	}

	Footer {
		background: #18252b;
	}
	"""

	BINDINGS = [
		("q", "quit", "Quit"),
		("r", "reset", "Reset"),
		("c", "clear", "Clear peak"),
	]

	def __init__(self) -> None:
		super().__init__()
		self._previous = Counters()
		self._previous_time = 0.0
		self._peak_download = 0.0
		self._peak_upload = 0.0

	def compose(self) -> ComposeResult:
		yield Header(show_clock=True)
		with Container(id="dashboard"):
			with Horizontal(id="rates"):
				with Vertical(classes="metric"):
					yield Static("DOWNLOAD", classes="metric-title")
					yield Static("Waiting...", id="download", classes="metric-value")
				with Vertical(classes="metric"):
					yield Static("UPLOAD", classes="metric-title")
					yield Static("Waiting...", id="upload", classes="metric-value")
			yield Static("Starting network monitor...", id="status")
		yield Footer()

	def on_mount(self) -> None:
		self._sample()
		self.set_interval(1.0, self._sample)

	def action_reset(self) -> None:
		self._previous = Counters()
		self._previous_time = 0.0
		self._sample()

	def action_clear(self) -> None:
		self._peak_download = 0.0
		self._peak_upload = 0.0
		self._sample()

	def _sample(self) -> None:
		try:
			counters, interfaces = read_counters()
		except OSError as error:
			self.query_one("#status", Static).update(f"Unable to read Linux network stats: {error}")
			return

		now = time.monotonic()
		elapsed = now - self._previous_time
		if self._previous_time and elapsed > 0:
			download = max(0, counters.received - self._previous.received) / elapsed
			upload = max(0, counters.transmitted - self._previous.transmitted) / elapsed
			self._peak_download = max(self._peak_download, download)
			self._peak_upload = max(self._peak_upload, upload)
			self.query_one("#download", Static).update(format_rate(download))
			self.query_one("#upload", Static).update(format_rate(upload))

		self._previous = counters
		self._previous_time = now
		interface_text = ", ".join(interfaces) if interfaces else "No active interface"
		self.query_one("#status", Static).update(
			f"Interfaces: {interface_text}  |  "
			f"Peak: {format_rate(self._peak_download)} down / "
			f"{format_rate(self._peak_upload)} up"
		)


if __name__ == "__main__":
	NetSpeedApp().run()
