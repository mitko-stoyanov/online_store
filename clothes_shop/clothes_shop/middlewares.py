from clothes_shop.web.views.main_views import InternalError


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 400:
            return InternalError.as_view()(request)
        return response
    return middleware
