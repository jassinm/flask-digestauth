install
-------
    pip install git+https://github.com/locojay/flask-digestauth.git

usage
-----
    digest_auth = DigestAuth(<realm>)

    digest_auth.init_app(app)
    digest_auth.add_user(<username> , <password>)


use digest_auth.requires_auth decorator on entry points, or set DIGEST_AUTH_FORCE to
True to enforce it for all entry points

see "http://flask.pocoo.org/snippets/31/"
