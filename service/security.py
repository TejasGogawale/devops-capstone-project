"""Security response policy helpers.

The Flask application installs Talisman and CORS response headers in
service/__init__.py. This module documents the headers expected by the API.
"""

SECURITY_HEADER_EXPECTATIONS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
}
