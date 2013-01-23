# from werkzeug.contrib import authdigest
from authdigest import RealmDigestDB
from functools import wraps
from flask import current_app, request


class DigestAuth(RealmDigestDB):
    def __init__(self, realm, app=None):
        # super(DigestAuth, self).__init__(self, realm, algorithm='md5')
        RealmDigestDB.__init__(self, realm, 'md5')
        if app is not None:
            self.app = app
            self.init_app(app)
        else:
            self.app = None

    def init_app(self, app):
        app.config.setdefault('DIGEST_AUTH_FORCE', False)

        @app.before_request
        def require_basic_auth():
            if not current_app.config['DIGEST_AUTH_FORCE']:
                return
            if not self.isAuthenticated(request):
                return self.challenge()

    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not self.isAuthenticated(request):
                return self.challenge()

            return f(*args, **kwargs)

        return decorated
