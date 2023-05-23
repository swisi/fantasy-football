class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = request.user if request.user.is_authenticated else None
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        response.context_data['user'] = request.user
        return response
