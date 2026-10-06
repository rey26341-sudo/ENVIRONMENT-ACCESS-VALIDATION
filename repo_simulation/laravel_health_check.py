"""
laravel_health_check.py
=======================

Checks the health of the Laravel validation service
from the Python validation environment.
"""

import sys
import urllib.request
import json

LARAVEL_HEALTH_URL = "http://127.0.0.1:8001/api/health"


def check_laravel_health():
    """Call the Laravel health endpoint and validate the response."""

    try:
        with urllib.request.urlopen(LARAVEL_HEALTH_URL, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))

        if data.get("status") != "healthy":
            print("Laravel service is unhealthy.")
            return False

        print("Laravel service is healthy.")
        print(f"App: {data.get('app')}")
        print(f"Version: {data.get('version')}")
        print(f"Environment: {data.get('environment')}")

        return True

    except Exception as exc:
        print(f"Laravel health check failed: {exc}")
        return False


if __name__ == "__main__":
    sys.exit(0 if check_laravel_health() else 1)
