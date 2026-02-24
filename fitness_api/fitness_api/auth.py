"""
Custom authentication for the API: session auth without CSRF enforcement
so that API clients (Postman, curl, frontends) can use session cookies without a CSRF token.
"""
from rest_framework.authentication import SessionAuthentication


class SessionAuthenticationNoCSRF(SessionAuthentication):
    """Session auth that does not enforce CSRF (for API-only usage)."""

    def enforce_csrf(self, request):
        pass  # Skip CSRF check
