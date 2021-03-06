import calendar

import serpy


class EnumField(serpy.Field):

    def to_value(self, v):
        return v.name


class DatetimeToUnixField(serpy.Field):

    def to_value(self, v):
        if v is None:
            return None
        return calendar.timegm(v.utctimetuple())

class CharacterLocationField(serpy.Field):

    getter_takes_serializer = True

    def as_getter(self, serializer_field_name, serializer_cls):
        return lambda self, v: {'x': v.x, 'y': v.y, 'z': v.z}


class ClanSerializer(serpy.Serializer):
    id              = serpy.Field()
    server_id       = serpy.Field()
    name            = serpy.Field()
    motd            = serpy.Field()
    owner_id        = serpy.Field()
    owner_name      = serpy.MethodField()
    character_count = serpy.Field()
    created         = DatetimeToUnixField()

    def get_owner_name(self, item):
        return item.owner.name if item.owner is not None else None


class CharacterSerializer(serpy.Serializer):
    id             = serpy.Field()
    server_id      = serpy.Field()
    steam_id       = serpy.Field()
    clan_id        = serpy.Field()
    name           = serpy.Field()
    level          = serpy.Field()
    is_online      = serpy.Field()
    location       = CharacterLocationField()
    clan_name      = serpy.MethodField()
    created        = DatetimeToUnixField()
    last_online    = DatetimeToUnixField()
    last_killed_by = serpy.Field()

    def get_clan_name(self, item):
        return item.clan.name if item.clan is not None else None


class CharacterHistorySerializer(serpy.Serializer):
    character_id   = serpy.Field()
    created        = DatetimeToUnixField()
    location       = CharacterLocationField()


class ServerAdminSerializer(serpy.Serializer):
    id              = serpy.Field()
    name            = serpy.Field()
    character_count = serpy.Field()
    online_count    = serpy.Field()
    private_secret  = serpy.Field()
    ip_address      = serpy.Field()
    last_sync       = DatetimeToUnixField()


class ServerSerializer(serpy.Serializer):
    id              = serpy.Field()
    name            = serpy.Field()
    character_count = serpy.Field()
    online_count    = serpy.Field()
    ip_address      = serpy.Field()
    last_sync       = DatetimeToUnixField()
