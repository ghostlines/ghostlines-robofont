import requests

from ghostlines import env


class Ghostlines(object):

    def __init__(self, version, token=None):
        self.version = version
        self.token = token

    def send(self, otf=None, recipients=None, notes=None, designer_email_address=None, license=None):
        if not otf and not recipients:
            return

        url = self.path('send')

        files = {
            'otf': otf
        }

        data = {
            'recipients': recipients,
            'notes': notes,
            'designer_email_address': designer_email_address
        }

        if license is not None:
            files['license'] = license

        return requests.post(url, files=files, data=data)

    def enable_applicants(self, data):
        url = self.path('applicants/enable')
        return requests.post(url, data=data)

    def registry(self, token):
        url = self.path('applicants/{}'.format(token))
        return requests.get(url)

    def approve(self, token, email_address):
        data = {'email_address': email_address}
        url = self.path('applicants/{}/approve'.format(token))
        return requests.post(url, data=data)

    # V1

    def create_font_family(self, name, designer):
        data = {'name': name, 'designer_name': designer}
        headers = {'Authorization': 'Bearer {}'.format(self.token)}
        url = self.path('font_family')
        return requests.post(url, data=data, headers=headers)

    def path(self, endpoint):
        return '{}/{}/{}'.format(env.api_url, self.version, endpoint)
