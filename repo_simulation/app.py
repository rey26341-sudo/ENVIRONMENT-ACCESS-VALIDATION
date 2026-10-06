"""
app.py
======

Simulated application entry point for the
ENVIRONMENT-ACCESS-VALIDATION project.
"""

import datetime
import logging
import os

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)

APP_NAME = "environment-access-validator"
VERSION = "1.0.0"
ENV = os.environ.get("APP_ENV", "development")


def get_status():
    """Return a health-check dictionary for the application."""
    return {
        "app": APP_NAME,
        "version": VERSION,
        "env": ENV,
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "status": "healthy",
    }


def start():
    """Simulate application startup."""
    logger.info("Starting %s v%s [%s]", APP_NAME, VERSION, ENV)

    status = get_status()

    logger.info("Health check: %s", status)

    print(f"[{APP_NAME}] Running in {ENV} mode — v{VERSION}")

    return status


if __name__ == "__main__":
    start()
