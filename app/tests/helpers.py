import json

def register_user(self):
    """helper function for registering a user."""
    return self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='imireallan@gmail.com',
            username='imire',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
        )

def login_user(self):
    """helper function for login a user."""
    return self.client.post(
        'api/v2/auth/login',
        data=json.dumps(dict(
            username='imire',
            password='password'
        )),
        content_type='application/json'
    )

# def create_entry(self, access_token):
#     "helper function for creating an entry"
#     rv = self.client.post(
#     'api/v2/entries',
#     headers={
#         "x-access-token": access_token,
#         "content-type": "application/json"
#     },
#     data=self.entry
#     )

# def get_all(self, access_token):
#     "helper function for creating an entry"
#     rv = self.client.get(
#     'api/v2/entries',
#     headers={
#         "x-access-token": access_token,
#         "content-type": "application/json"
#     }
#     )