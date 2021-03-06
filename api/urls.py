from django.conf.urls import url

from .views import (CharacterHistoryView, CharactersView, CharacterView,
                    ClansView, ClanView, ServersView, ServerView,
                    SyncCharactersView, ClanCharactersView)

urlpatterns = [
    url(r'^$', ServersView.as_view()),
    url(r'^(?P<server_id>\d+)$', ServerView.as_view()),
    url(r'^(?P<server_id>\d+)/sync/characters$', SyncCharactersView.as_view()),
    url(r'^(?P<server_id>\d+)/clans$', ClansView.as_view()),
    url(r'^(?P<server_id>\d+)/clans/(?P<clan_id>\d+)$', ClanView.as_view()),
    url(r'^(?P<server_id>\d+)/clans/(?P<clan_id>\d+)/characters$', ClanCharactersView.as_view()),
    url(r'^(?P<server_id>\d+)/characters$', CharactersView.as_view()),
    url(r'^(?P<server_id>\d+)/characters/(?P<character_id>\d+)$', CharacterView.as_view()),
    url(r'^(?P<server_id>\d+)/characters/(?P<character_id>\d+)/history$', CharacterHistoryView.as_view())
]
