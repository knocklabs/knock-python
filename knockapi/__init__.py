__version__ = '0.6.0'

from knockapi.async_client import Knock as AsyncKnock

try:
    from knockapi.sync_client import Knock
except ImportError:
    Knock = None

__all__ = [
    "AsyncKnock",
    "Knock",
    "__version__"
]
