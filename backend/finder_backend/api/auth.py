from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from jose import JWTError, jwt
import requests
import os

class Auth0Authentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return None
        token = auth_header.split(' ')[1]
        try:
            jwks_url = f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/jwks.json'
            response = requests.get(jwks_url)
            jwks = response.json()
            unverified_header = jwt.get_unverified_header(token)
            kid = unverified_header['kid']
            key = next(key for key in jwks['keys'] if key['kid'] == kid)
            public_key = f"-----BEGIN PUBLIC KEY-----\n{key['x5c'][0]}\n-----END PUBLIC KEY-----"
            claims = jwt.decode(
                token,
                public_key,
                algorithms=['RS256'],
                audience=os.getenv('AUTH0_AUDIENCE'),
                issuer=f'https://{os.getenv("AUTH0_DOMAIN")}/'
            )
            userinfo_url = f'https://{os.getenv("AUTH0_DOMAIN")}/userinfo'
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(userinfo_url, headers=headers)
            userinfo = response.json()
            user, created = User.objects.get_or_create(
                auth0_id=userinfo['sub'],
                defaults={'email': userinfo['email'], 'name': userinfo['name']}
            )
            return (user, token)
        except JWTError as e:
            raise AuthenticationFailed('Invalid token')