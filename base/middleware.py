from django.http import HttpResponseForbidden

ALLOWED_IPS = ["172.18.0.1", "127.0.0.1", "::1", "77.75.146.202"] 
# 172.18.0.1 - Docker
# 127.0.0.1, ::1, localhost
# 77.75.146.202 public provider address

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

class AdminIPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/donttouchmethere/"):
            ip = get_client_ip(request)
            if ip not in ALLOWED_IPS:
                return HttpResponseForbidden("Access denied")
        return self.get_response(request)