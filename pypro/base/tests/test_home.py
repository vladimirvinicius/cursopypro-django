from django.test import Client


def test_status_code(client: Client):
    resp = client.get('/')
    resp.status_code == 200
