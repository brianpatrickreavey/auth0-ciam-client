"""Auth0 CIAM Client - Customer Identity and Access Management for Auth0"""

__version__ = "0.1.0"
__author__ = "Brian Reavey"
__email__ = "brian@reavey05.com"
__license__ = "GPL-3.0-only"

import logging

from .core import AuthenticationCore, AuthResult
from .session_store import SessionStore, InMemorySessionStore
from .exceptions import (
    AuthenticationError,
    AuthenticationRequiredError,
    SessionExpiredError,
    InvalidCredentialsError,
    NetworkError,
)
from .config import Auth0Config, create_angel_studios_config

def test_logging(level=None):
    """
    Test logging function for development/validation.
    If level is None, emits a message at each log level.
    If level is specified (e.g., 'info', 'error'), emits only at that level.
    """
    logger = logging.getLogger(__name__)
    
    if level is None:
        # Emit at all levels for comprehensive testing
        logger.debug("Auth0 CIAM Client test_logging: Debug message")
        logger.info("Auth0 CIAM Client test_logging: Info message")
        logger.warning("Auth0 CIAM Client test_logging: Warning message")
        logger.error("Auth0 CIAM Client test_logging: Error message")
        logger.critical("Auth0 CIAM Client test_logging: Critical message")
    else:
        # Emit at specific level
        level = level.lower()
        if level == 'debug':
            logger.debug("Auth0 CIAM Client test_logging: Debug message")
        elif level == 'info':
            logger.info("Auth0 CIAM Client test_logging: Info message")
        elif level == 'warning':
            logger.warning("Auth0 CIAM Client test_logging: Warning message")
        elif level == 'error':
            logger.error("Auth0 CIAM Client test_logging: Error message")
        elif level == 'critical':
            logger.critical("Auth0 CIAM Client test_logging: Critical message")
        else:
            logger.error(f"Auth0 CIAM Client test_logging: Invalid level '{level}'")

__all__ = [
    "AuthenticationCore",
    "AuthResult",
    "SessionStore",
    "InMemorySessionStore",
    "AuthenticationError",
    "AuthenticationRequiredError",
    "SessionExpiredError",
    "InvalidCredentialsError",
    "NetworkError",
    "Auth0Config",
    "create_angel_studios_config",
    "test_logging",
]
