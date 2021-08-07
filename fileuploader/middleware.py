class AuthenticationMiddleware(object):
    def process_exception(self, request, exception):
        print('okkkk')
        return None