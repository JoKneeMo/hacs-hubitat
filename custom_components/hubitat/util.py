from hashlib import sha256
from typing import Dict

from custom_components.hubitat.const import CONF_DEVICE_TYPE_OVERRIDES
from hubitatmaker import Hub

from homeassistant.config_entries import ConfigEntry

_token_hashes = {}


def get_token_hash(token: str) -> str:
    if token not in _token_hashes:
        hasher = sha256()
        hasher.update(token.encode("utf-8"))
        _token_hashes[token] = hasher.hexdigest()
    return _token_hashes[token]


def get_hub_short_id(hub: Hub) -> str:
    return hub.token[:8]


def get_device_overrides(config_entry: ConfigEntry) -> Dict[str, str]:
    return config_entry.options.get(CONF_DEVICE_TYPE_OVERRIDES, {})
