from typing import Literal
from urllib.parse import urlencode
import json
import time

class Agent:
    def __init__(self):
        self._epoch_offset = 0

    def get_screen_properties(self) -> dict:
        # window.screen
        return {}
    
    def get_navigator_properties(self) -> dict:
        # window.navigator
        return {}

    def epoch(self, ms: bool = True):
        # Returns current timestamp, with offset added.
        t = time.time() * 1000
        t += self._epoch_offset
        if not ms: t /= 1000
        return int(t)

    def epoch_travel(self, delta: float, ms: bool = True):
        # Offsets the epoch.
        if not ms: delta *= 1000
        self._epoch_offset += delta

    def epoch_wait(self):
        # Waits out epoch offset and resets it to 0.
        if self._epoch_offset > 0:
            time.sleep(self._epoch_offset/1000)
        self._epoch_offset = 0

    def json_encode(self, data: Literal) -> str:
        # Browsers can have differing ways of performing JSON encoding.
        return json.dumps(data, separators=(",", ":"))

    def url_encode(self, data: dict) -> str:
        # Browsers can have differing ways of performing URL encoding.
        return urlencode(data)
    
    def format_headers(
        self,
        url: str,
        headers: dict = {},
        origin_url: str = None,
        sec_site: str = "cross-site",
        sec_mode: str = "cors",
        sec_dest: str = "empty"
    ) -> dict:
        # Formats headers in a browser-like way.
        return headers