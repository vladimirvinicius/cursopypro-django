import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains
from model_bakery import baker
from pypro.aperitivos.models import Video


@pytest.fixture
def videos(db):
    return baker.make(Video, 2)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_status_code_indice(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_titulo_link_indice(resp, videos):
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
