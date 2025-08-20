from .models import Visit

class SaveVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Не сохраняем для админки
        if not request.path.startswith("/admin/"):
            ip = request.META.get("REMOTE_ADDR")
            user_agent = request.META.get("HTTP_USER_AGENT", "")
            Visit.objects.create(
                ip_address=ip,
                user_agent=user_agent,
                path=request.path
            )

        return response
