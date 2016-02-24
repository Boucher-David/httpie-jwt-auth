# -*- coding: utf-8 -*-

"""
JWTAuth auth plugin for HTTPie.
"""
import os

from httpie.plugins import AuthPlugin

__version__ = '0.3.0-dev0'
__author__ = 'hoatle'
__license__ = 'BSD'


class JWTAuth(object):
    """JWTAuth to set the right Authorization header format of JWT"""

    def __init__(self, token, auth_prefix):
        self.token = token
        self.auth_prefix = auth_prefix

    def __call__(self, request):
        request.headers['Authorization'] = '{0} {1}'.format(self.auth_prefix, self.token)
        return request


class JWTAuthPlugin(AuthPlugin):
    """Plugin registration"""

    name = 'JWT auth'
    auth_type = 'jwt'
    description = 'Set the right format for JWT auth request'

    def get_auth(self, username, password):
        auth_prefix = os.environ.get('JWT_AUTH_PREFIX', 'Bearer')
        return JWTAuth(username, auth_prefix)
