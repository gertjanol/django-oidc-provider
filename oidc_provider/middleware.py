from django.utils.deprecation import MiddlewareMixin

from oidc_provider.lib.utils.common import get_browser_state_or_default


class SessionManagementMiddleware(MiddlewareMixin):
    """
    Maintain a `op_browser_state` cookie along with the `sessionid` cookie that
    represents the End-User's login state at the OP. If the user is not logged
    in no cookie is set, because there is no session state to maintain.
    """

    def process_response(self, request, response):
        response.set_cookie('op_browser_state', get_browser_state_or_default(request))
        return response
