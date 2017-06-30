from .base import BaseAdminView
from api.models import Character, Server
from datetime import datetime
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.utils import timezone
import json
import pytz


class SyncCharactersView(BaseAdminView):

	def post(self, request, server_id):
		now = timezone.now()

		if 'private_secret' not in request.GET:
			return HttpResponse('missing required param private_secret', status=400)

		data = json.loads(request.body)

		if 'characters' not in data:
			return HttpResponse('missing required param characters', status=400)

		server = (Server.objects
			.filter(id=server_id, private_secret=request.GET['private_secret'])
			.first())

		if server is None:
			return HttpResponse('server does not exist', status=404)

		with transaction.atomic():
			# Delete removed characters
			synced_ids = [c['conan_id'] for c in data['characters']]

			(Character.objects
				.filter(server=server)
				.filter(~Q(conan_id__in=synced_ids))
				.delete())

			for sync_data in data['characters']:
				character = (Character.objects
					.filter(conan_id=sync_data['conan_id'])
					.first())

				if character is None:
					character = Character()

				is_different = (
					sync_data['x'] != character.x or
					sync_data['y'] != character.y or
					sync_data['z'] != character.y)

				last_online = (datetime
					.utcfromtimestamp(sync_data['last_online'])
					.replace(tzinfo=pytz.utc))

				character.server         = server
				character.conan_id       = sync_data['conan_id']
				character.name           = sync_data['name']
				character.level          = sync_data['level']
				character.is_online      = sync_data['is_online']
				character.steam_id       = sync_data['steam_id']
				character.last_killed_by = sync_data['last_killed_by']
				character.x              = sync_data['x']
				character.y              = sync_data['y']
				character.z              = sync_data['z']
				character.last_online    = last_online
				character.save()

				if is_different:
					CharacterHistory.objects.create(
						character=character,
						created=now,
						x=character.x,
						y=character.y,
						z=character.z)

		server.last_sync = now
		server.save()

		return HttpResponse(status=200)