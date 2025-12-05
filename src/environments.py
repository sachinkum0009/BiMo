"""
Environment class for managing different simulation environments in Isaac Sim.
"""

from pathlib import Path

from isaacsim.storage.native import get_assets_root_path

from my_utils import get_omniverse_content_url

ASSETS_ROOT = get_assets_root_path()
OMNIVERSE_CONTENT_URL = get_omniverse_content_url()


class IndoorEnvironment:
    """Enum for predefined indoor environment USD file paths."""

    HOSPITAL = Path(
        f"{OMNIVERSE_CONTENT_URL}/Assets/Isaac/5.0/Isaac/Environments/Hospital/hospital.usd"
    )


class OutdoorEnvironment:
    """Enum for predefined outdoor environment USD file paths."""

    RIVERMARK = Path(
        f"{OMNIVERSE_CONTENT_URL}/Assets/Isaac/5.0/Isaac/Environments/Outdoor/Rivermark/rivermark.usd"
    )


class Environment:
    """Enum for predefined environment USD file paths."""

    INDOOR = IndoorEnvironment
    OUTDOOR = OutdoorEnvironment
