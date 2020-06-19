
from .package import Package


class BaseClient(object):

    def __init__(self):
        self.album = Album(self)
        self.artist = Artist(self)
        self.auth = Auth(self)
        self.chart = Chart(self)
        self.event = Event(self)
        self.geo = Geo(self)
        self.group = Group(self)
        self.library = Library(self)
        self.playlist = Playlist(self)
        self.radio = Radio(self)
        self.tag = Tag(self)
        self.tasteometer = Tasteometer(self)
        self.track = Track(self)
        self.user = User(self)
        self.venue = Venue(self)


class Album(Package):

    def add_tags(self, album, artist, tags):
        """
        Tag an album using a list of user supplied tags.

        Authorization required.

        http://www.last.fm/api/show/album.addTags

        :param album: required
            (Required) : The album name
        :param artist: required
            (Required) : The artist name
        :param tags: required
            (Required) : A comma delimited list of user supplied tags to apply to
            this album. Accepts a maximum of 10 tags.

        """
        return self._call('POST', 'addTags', auth=True, album=album, artist=artist, tags=tags)

    def get_buylinks(self, album, artist, country, autocorrect=None, mbid=None):
        """
        Get a list of Buy Links for a particular Album. It is required that
        you supply either the artist and track params or the mbid param.

        Authorization not required.

        http://www.last.fm/api/show/album.getBuylinks

        :param album: required
            (Required (unless mbid)] : The album
        :param artist: required
            (Required (unless mbid)] : The artist name
        :param country: required
            (Required) : A country name or two character country code, as defined
            by the ISO 3166-1 country names standard.
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the album

        """
        return self._call('GET', 'getBuylinks', auth=False, album=album, artist=artist, country=country,
                          autocorrect=autocorrect, mbid=mbid)

    def get_info(self, album, artist, lang=None, autocorrect=None, username=None, mbid=None):
        """
        Get the metadata and tracklist for an album on Last.fm using the album
        name or a musicbrainz id.

        Authorization not required.

        http://www.last.fm/api/show/album.getInfo

        :param album: required
            (Required (unless mbid)] : The album name
        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param lang: optional
            (Optional) : The language to return the biography in, expressed as an
            ISO 639 alpha-2 code.
        :param mbid: optional
            (Optional) : The musicbrainz id for the album
        :param username: optional
            (Optional) : The username for the context of the request. If supplied,
            the user's playcount for this album is included in the response.

        """
        return self._call('GET', 'getInfo', auth=False, album=album, artist=artist, autocorrect=autocorrect, lang=lang,
                          mbid=mbid, username=username)

    def get_shouts(self, artist, autocorrect=None, page=None, limit=None, mbid=None):
        """
        Get shouts for this album. Also available as an rss feed.

        Authorization not required.

        http://www.last.fm/api/show/album.getShouts

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getShouts', auth=False, artist=artist, autocorrect=autocorrect, limit=limit,
                          mbid=mbid, page=page)

    def get_tags(self, album, artist, autocorrect=None, user=None, mbid=None):
        """
        Get the tags applied by an individual user to an album on Last.fm. To
        retrieve the list of top tags applied to an album by all users use
        album.getTopTags.

        Authorization not required.

        http://www.last.fm/api/show/album.getTags

        :param album: required
            (Required (unless mbid)] : The album name
        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the album
        :param user: optional
            (Optional) : If called in non-authenticated mode you must specify the
            user to look up

        """
        return self._call('GET', 'getTags', auth=False, album=album, artist=artist, autocorrect=autocorrect, mbid=mbid,
                          user=user)

    def get_top_tags(self, album, artist, autocorrect=None, mbid=None):
        """
        Get the top tags for an album on Last.fm, ordered by popularity.

        Authorization not required.

        http://www.last.fm/api/show/album.getTopTags

        :param album: required
            (Required (unless mbid)] : The album name
        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the album

        """
        return self._call('GET', 'getTopTags', auth=False, album=album, artist=artist, autocorrect=autocorrect,
                          mbid=mbid)

    def remove_tag(self, album, artist, tag):
        """
        Remove a user's tag from an album.

        Authorization required.

        http://www.last.fm/api/show/album.removeTag

        :param album: required
            (Required) : The album name
        :param artist: required
            (Required) : The artist name
        :param tag: required
            (Required) : A single user tag to remove from this album.

        """
        return self._call('POST', 'removeTag', auth=True, album=album, artist=artist, tag=tag)

    def search(self, album, limit=None, page=None):
        """
        Search for an album by name. Returns album matches sorted by
        relevance.

        Authorization not required.

        http://www.last.fm/api/show/album.search

        :param album: required
            (Required) : The album name
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 30.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'search', auth=False, album=album, limit=limit, page=page)

    def share(self, album, artist, recipient, message=None, public=None):
        """
        Share an album with one or more Last.fm users or other friends.

        Authorization required.

        http://www.last.fm/api/show/album.share

        :param album: required
            (Required) : An album name.
        :param artist: required
            (Required) : An artist name.
        :param recipient: required
            (Required): Email Address | Last.fm Username - A comma delimited list
            of email addresses or Last.fm usernames. Maximum is 10.
        :param message: optional
            (Optional): An optional message to send with the recommendation. If
            not supplied a default message will be used.
        :param public: optional
            (Optional): Optionally show in the sharing users activity feed.
            Defaults to 0 (false).

        """
        return self._call('POST', 'share', auth=True, album=album, artist=artist, recipient=recipient, message=message,
                          public=public)


class Artist(Package):

    def add_tags(self, artist, tags):
        """
        Tag an artist with one or more user supplied tags.

        Authorization required.

        http://www.last.fm/api/show/artist.addTags

        :param artist: required
            (Required) : The artist name
        :param tags: required
            (Required) : A comma delimited list of user supplied tags to apply to
            this artist. Accepts a maximum of 10 tags.

        """
        return self._call('POST', 'addTags', auth=True, artist=artist, tags=tags)

    def get_correction(self, artist):
        """
        Use the last.fm corrections data to check whether the supplied artist
        has a correction to a canonical artist

        Authorization not required.

        http://www.last.fm/api/show/artist.getCorrection

        :param artist: required
            (Required) : The artist name to correct.

        """
        return self._call('GET', 'getCorrection', auth=False, artist=artist)

    def get_events(self, artist, autocorrect=None, festivalsonly=None, mbid=None, limit=None, page=None):
        """
        Get a list of upcoming events for this artist. Easily integratable
        into calendars, using the ical standard (see feeds section below).

        Authorization not required.

        http://www.last.fm/api/show/artist.getEvents

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param festivalsonly: optional, boolean
            [0|1] (Optional) : Whether only festivals should be returned, or all
            events.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist
        :param page: optional
            (Optiona) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getEvents', auth=False, artist=artist, autocorrect=autocorrect,
                          festivalsonly=festivalsonly, limit=limit, mbid=mbid, page=page)

    def get_info(self, artist, lang=None, username=None, autocorrect=None, mbid=None):
        """
        Get the metadata for an artist. Includes biography, truncated at 300
        characters.

        Authorization not required.

        http://www.last.fm/api/show/artist.getInfo

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param lang: optional
            (Optional) : The language to return the biography in, expressed as an
            ISO 639 alpha-2 code.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist
        :param username: optional
            (Optional) : The username for the context of the request. If supplied,
            the user's playcount for this artist is included in the response.

        """
        return self._call('GET', 'getInfo', auth=False, artist=artist, autocorrect=autocorrect, lang=lang, mbid=mbid,
                          username=username)

    def get_past_events(self, artist, autocorrect=None, page=None, limit=None, mbid=None):
        """
        Get a paginated list of all the events this artist has played at in
        the past.

        Authorization not required.

        http://www.last.fm/api/show/artist.getPastEvents

        :param artist: required
            (Required (unless mbid)] :The name of the artist you would like to
            fetch event listings for.
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist
        :param page: optional
            (Optional) :The page of results to return.

        """
        return self._call('GET', 'getPastEvents', auth=False, artist=artist, autocorrect=autocorrect, limit=limit,
                          mbid=mbid, page=page)

    def get_podcast(self, artist, autocorrect=None, mbid=None):
        """
        Get a podcast of free mp3s based on an artist

        Authorization not required.

        http://www.last.fm/api/show/artist.getPodcast

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist

        """
        return self._call('GET', 'getPodcast', auth=False, artist=artist, autocorrect=autocorrect, mbid=mbid)

    def get_shouts(self, artist, autocorrect=None, page=None, limit=None, mbid=None):
        """
        Get shouts for this artist. Also available as an rss feed.

        Authorization not required.

        http://www.last.fm/api/show/artist.getShouts

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getShouts', auth=False, artist=artist, autocorrect=autocorrect, limit=limit,
                          mbid=mbid, page=page)

    def get_similar(self, artist, autocorrect=None, limit=None, mbid=None):
        """
        Get all the artists similar to this artist

        Authorization not required.

        http://www.last.fm/api/show/artist.getSimilar

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param limit: optional
            (Optional) : Limit the number of similar artists returned
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist

        """
        return self._call('GET', 'getSimilar', auth=False, artist=artist, autocorrect=autocorrect, limit=limit,
                          mbid=mbid)

    def get_tags(self, artist, user=None, autocorrect=None, mbid=None):
        """
        Get the tags applied by an individual user to an artist on Last.fm. If
        accessed as an authenticated service /and/ you don't supply a user
        parameter then this service will return tags for the authenticated
        user. To retrieve the list of top tags applied to an artist by all
        users use artist.getTopTags.

        Authorization not required.

        http://www.last.fm/api/show/artist.getTags

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist
        :param user: optional
            (Optional) : If called in non-authenticated mode you must specify the
            user to look up

        """
        return self._call('GET', 'getTags', auth=False, artist=artist, autocorrect=autocorrect, mbid=mbid, user=user)

    def get_top_albums(self, artist, autocorrect=None, page=None, limit=None, mbid=None):
        """
        Get the top albums for an artist on Last.fm, ordered by popularity.

        Authorization not required.

        http://www.last.fm/api/show/artist.getTopAlbums

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopAlbums', auth=False, artist=artist, autocorrect=autocorrect, limit=limit,
                          mbid=mbid, page=page)

    def get_top_fans(self, artist, autocorrect=None, mbid=None):
        """
        Get the top fans for an artist on Last.fm, based on listening data.

        Authorization not required.

        http://www.last.fm/api/show/artist.getTopFans

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist

        """
        return self._call('GET', 'getTopFans', auth=False, artist=artist, autocorrect=autocorrect, mbid=mbid)

    def get_top_tags(self, artist, autocorrect=None, mbid=None):
        """
        Get the top tags for an artist on Last.fm, ordered by popularity.

        Authorization not required.

        http://www.last.fm/api/show/artist.getTopTags

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist

        """
        return self._call('GET', 'getTopTags', auth=False, artist=artist, autocorrect=autocorrect, mbid=mbid)

    def get_top_tracks(self, artist, autocorrect=None, page=None, limit=None, mbid=None):
        """
        Get the top tracks by an artist on Last.fm, ordered by popularity

        Authorization not required.

        http://www.last.fm/api/show/artist.getTopTracks

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist names into correct
            artist names, returning the correct version instead. The corrected
            artist name will be returned in the response.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param mbid: optional
            (Optional) : The musicbrainz id for the artist
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopTracks', auth=False, artist=artist, autocorrect=autocorrect, limit=limit,
                          mbid=mbid, page=page)

    def remove_tag(self, artist, tag):
        """
        Remove a user's tag from an artist.

        Authorization required.

        http://www.last.fm/api/show/artist.removeTag

        :param artist: required
            (Required) : The artist name
        :param tag: required
            (Required) : A single user tag to remove from this artist.

        """
        return self._call('POST', 'removeTag', auth=True, artist=artist, tag=tag)

    def search(self, artist, limit=None, page=None):
        """
        Search for an artist by name. Returns artist matches sorted by
        relevance.

        Authorization not required.

        http://www.last.fm/api/show/artist.search

        :param artist: required
            (Required) : The artist name
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 30.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'search', auth=False, artist=artist, limit=limit, page=page)

    def share(self, artist, recipient, message=None, public=None):
        """
        Share an artist with Last.fm users or other friends.

        Authorization required.

        http://www.last.fm/api/show/artist.share

        :param artist: required
            (Required) : The artist to share.
        :param recipient: required
            (Required): Email Address | Last.fm Username - A comma delimited list
            of email addresses or Last.fm usernames. Maximum is 10.
        :param message: optional
            (Optional): An optional message to send with the recommendation. If
            not supplied a default message will be used.
        :param public: optional
            (Optional): Optionally show in the sharing users activity feed.
            Defaults to 0 (false).

        """
        return self._call('POST', 'share', auth=True, artist=artist, recipient=recipient, message=message,
                          public=public)

    def shout(self, artist, message):
        """
        Shout in this artist's shoutbox

        Authorization required.

        http://www.last.fm/api/show/artist.shout

        :param artist: required
            (Required) : The name of the artist to shout on.
        :param message: required
            (Required) : The message to post to the shoutbox.

        """
        return self._call('POST', 'shout', auth=True, artist=artist, message=message)


class Auth(Package):

    def get_mobile_session(self, password, username):
        """
        Create a web service session for a user. Used for authenticating a
        user when the password can be inputted by the user. Accepts email
        address as well, so please use the username supplied in the output.
        Only suitable for standalone mobile devices. See the authentication
        how-to for more. You must use HTTPS and POST in order to use this
        method.

        Authorization not required.

        http://www.last.fm/api/show/auth.getMobileSession

        :param password: required
            (Required) : The password in plain text.
        :param username: required
            (Required) : The last.fm username or email address.

        """
        return self._call('GET', 'getMobileSession', auth=False, password=password, username=username)

    def get_session(self, token):
        """
        Fetch a session key for a user. The third step in the authentication
        process. See the authentication how-to for more information.

        Authorization not required.

        http://www.last.fm/api/show/auth.getSession

        :param token: required
            (Required) : A 32-character ASCII hexadecimal MD5 hash returned by
            step 1 of the authentication process (following the granting of
            permissions to the application by the user)

        """
        return self._call('GET', 'getSession', auth=False, token=token)

    def get_token(self):
        """
        Fetch an unathorized request token for an API account. This is step 2
        of the authentication process for desktop applications. Web
        applications do not need to use this service.

        Authorization not required.

        http://www.last.fm/api/show/auth.getToken


        """
        return self._call('GET', 'getToken', auth=False)


class Chart(Package):

    def get_hyped_artists(self, limit=None, page=None):
        """
        Get the hyped artists chart

        Authorization not required.

        http://www.last.fm/api/show/chart.getHypedArtists

        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getHypedArtists', auth=False, limit=limit, page=page)

    def get_hyped_tracks(self, limit=None, page=None):
        """
        Get the top artists chart

        Authorization not required.

        http://www.last.fm/api/show/chart.getHypedTracks

        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getHypedTracks', auth=False, limit=limit, page=page)

    def get_loved_tracks(self, limit=None, page=None):
        """
        Get the most loved tracks chart

        Authorization not required.

        http://www.last.fm/api/show/chart.getLovedTracks

        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getLovedTracks', auth=False, limit=limit, page=page)

    def get_top_artists(self, limit=None, page=None):
        """
        Get the top artists chart

        Authorization not required.

        http://www.last.fm/api/show/chart.getTopArtists

        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopArtists', auth=False, limit=limit, page=page)

    def get_top_tags(self, limit=None, page=None):
        """
        Get the top artists chart

        Authorization not required.

        http://www.last.fm/api/show/chart.getTopTags

        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopTags', auth=False, limit=limit, page=page)

    def get_top_tracks(self, limit=None, page=None):
        """
        Get the top tracks chart

        Authorization not required.

        http://www.last.fm/api/show/chart.getTopTracks

        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopTracks', auth=False, limit=limit, page=page)


class Event(Package):

    def attend(self, event, status):
        """
        Set a user's attendance status for an event.

        Authorization required.

        http://www.last.fm/api/show/event.attend

        :param event: required
            (Required) : The numeric last.fm event id
        :param status: required
            (Required) : The attendance status (0=Attending, 1=Maybe attending,
            2=Not attending)

        """
        return self._call('POST', 'attend', auth=True, event=event, status=status)

    def get_attendees(self, event, limit=None, page=None):
        """
        Get a list of attendees for an event.

        Authorization not required.

        http://www.last.fm/api/show/event.getAttendees

        :param event: required
            (Required) : The numeric last.fm event id
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optiona) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getAttendees', auth=False, event=event, limit=limit, page=page)

    def get_info(self, event):
        """
        Get the metadata for an event on Last.fm. Includes attendance and
        lineup information.

        Authorization not required.

        http://www.last.fm/api/show/event.getInfo

        :param event: required
            (Required) : The numeric last.fm event id

        """
        return self._call('GET', 'getInfo', auth=False, event=event)

    def get_shouts(self, event, limit=None, page=None):
        """
        Get shouts for this event. Also available as an rss feed.

        Authorization not required.

        http://www.last.fm/api/show/event.getShouts

        :param event: required
            (Required) : The numeric last.fm event id
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getShouts', auth=False, event=event, limit=limit, page=page)

    def share(self, event, recipient, message=None, public=None):
        """
        Share an event with one or more Last.fm users or other friends.

        Authorization required.

        http://www.last.fm/api/show/event.share

        :param event: required
            (Required) : An event ID
        :param recipient: required
            (Required): Email Address | Last.fm Username - A comma delimited list
            of email addresses or Last.fm usernames. Maximum is 10.
        :param message: optional
            (Optional): An optional message to send with the recommendation. If
            not supplied a default message will be used.
        :param public: optional
            (Optional): Optionally show the share in the sharing users recent
            activity. Defaults to 0 (false).

        """
        return self._call('POST', 'share', auth=True, event=event, recipient=recipient, message=message, public=public)

    def shout(self, event, message):
        """
        Shout in this event's shoutbox

        Authorization required.

        http://www.last.fm/api/show/event.shout

        :param event: required
            (Required) : The id of the event to shout on
        :param message: required
            (Required) : The message to post to the shoutbox

        """
        return self._call('POST', 'shout', auth=True, event=event, message=message)


class Geo(Package):

    def get_events(self, distance=None, festivalsonly=None, long=None, tag=None, limit=None, location=None, lat=None,
                   page=None):
        """
        Get all events in a specific location by country or city name.

        Authorization not required.

        http://www.last.fm/api/show/geo.getEvents

        :param distance: optional
            (Optional) : Find events within a specified radius (in kilometres)
        :param festivalsonly: optional, boolean
            [0|1] (Optional) : Whether only festivals should be returned, or all
            events.
        :param lat: optional
            (Optional) : Specifies a latitude value to retrieve events for
            (service returns nearby events by default)
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 10.
        :param location: optional
            (Optional) : Specifies a location to retrieve events for (service
            returns nearby events by default)
        :param long: optional
            (Optional) : Specifies a longitude value to retrieve events for
            (service returns nearby events by default)
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param tag: optional
            (Optional) : Specifies a tag to filter by.

        """
        return self._call('GET', 'getEvents', auth=False, distance=distance, festivalsonly=festivalsonly, lat=lat,
                          limit=limit, location=location, long=long, page=page, tag=tag)

    def get_metro_artist_chart(self, country, metro, end=None, start=None, limit=None, page=None):
        """
        Get a chart of artists for a metro

        Authorization not required.

        http://www.last.fm/api/show/geo.getMetroArtistChart

        :param country: required
            (Required) : A country name, as defined by the ISO 3166-1 country
            names standard
        :param metro: required
            (Required) : The metro's name
        :param end: optional
            (Optional) : Ending timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param start: optional
            (Optional) : Beginning timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)

        """
        return self._call('GET', 'getMetroArtistChart', auth=False, country=country, metro=metro, end=end, limit=limit,
                          page=page, start=start)

    def get_metro_hype_artist_chart(self, country, metro, end=None, start=None, limit=None, page=None):
        """
        Get a chart of hyped (up and coming) artists for a metro

        Authorization not required.

        http://www.last.fm/api/show/geo.getMetroHypeArtistChart

        :param country: required
            (Required) : A country name, as defined by the ISO 3166-1 country
            names standard
        :param metro: required
            (Required) : The metro's name
        :param end: optional
            (Optional) : Ending timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param start: optional
            (Optional) : Beginning timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)

        """
        return self._call('GET', 'getMetroHypeArtistChart', auth=False, country=country, metro=metro, end=end,
                          limit=limit, page=page, start=start)

    def get_metro_hype_track_chart(self, country, metro, end=None, start=None, limit=None, page=None):
        """
        Get a chart of tracks for a metro

        Authorization not required.

        http://www.last.fm/api/show/geo.getMetroHypeTrackChart

        :param country: required
            (Required) : A country name, as defined by the ISO 3166-1 country
            names standard
        :param metro: required
            (Required) : The metro's name
        :param end: optional
            (Optional) : Ending timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param start: optional
            (Optional) : Beginning timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)

        """
        return self._call('GET', 'getMetroHypeTrackChart', auth=False, country=country, metro=metro, end=end,
                          limit=limit, page=page, start=start)

    def get_metro_track_chart(self, country, metro, end=None, start=None, limit=None, page=None):
        """
        Get a chart of tracks for a metro

        Authorization not required.

        http://www.last.fm/api/show/geo.getMetroTrackChart

        :param country: required
            (Required) : A country name, as defined by the ISO 3166-1 country
            names standard
        :param metro: required
            (Required) : The metro's name
        :param end: optional
            (Optional) : Ending timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param start: optional
            (Optional) : Beginning timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)

        """
        return self._call('GET', 'getMetroTrackChart', auth=False, country=country, metro=metro, end=end, limit=limit,
                          page=page, start=start)

    def get_metro_unique_artist_chart(self, country, metro, end=None, start=None, limit=None, page=None):
        """
        Get a chart of the artists which make that metro unique

        Authorization not required.

        http://www.last.fm/api/show/geo.getMetroUniqueArtistChart

        :param country: required
            (Required) : A country name, as defined by the ISO 3166-1 country
            names standard
        :param metro: required
            (Required) : The metro's name
        :param end: optional
            (Optional) : Ending timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param start: optional
            (Optional) : Beginning timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)

        """
        return self._call('GET', 'getMetroUniqueArtistChart', auth=False, country=country, metro=metro, end=end,
                          limit=limit, page=page, start=start)

    def get_metro_unique_track_chart(self, country, metro, end=None, start=None, limit=None, page=None):
        """
        Get a chart of tracks for a metro

        Authorization not required.

        http://www.last.fm/api/show/geo.getMetroUniqueTrackChart

        :param country: required
            (Required) : A country name, as defined by the ISO 3166-1 country
            names standard
        :param metro: required
            (Required) : The metro's name
        :param end: optional
            (Optional) : Ending timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param start: optional
            (Optional) : Beginning timestamp of the weekly range requested (c.f.
            geo.getWeeklyChartlist)

        """
        return self._call('GET', 'getMetroUniqueTrackChart', auth=False, country=country, metro=metro, end=end,
                          limit=limit, page=page, start=start)

    def get_metro_weekly_chartlist(self, metro=None):
        """
        Get a list of available chart periods for this metro, expressed as
        date ranges which can be sent to the chart services.

        Authorization not required.

        http://www.last.fm/api/show/geo.getMetroWeeklyChartlist

        :param metro: optional
            : The metro name to fetch the charts list for.

        """
        return self._call('GET', 'getMetroWeeklyChartlist', auth=False, metro=metro)

    def get_metros(self, country=None):
        """
        Get a list of valid countries and metros for use in the other
        webservices

        Authorization not required.

        http://www.last.fm/api/show/geo.getMetros

        :param country: optional
            (Optional) : Optionally restrict the results to those Metros from a
            particular country, as defined by the ISO 3166-1 country names
            standard

        """
        return self._call('GET', 'getMetros', auth=False, country=country)

    def get_top_artists(self, country, limit=None, page=None):
        """
        Get the most popular artists on Last.fm by country

        Authorization not required.

        http://www.last.fm/api/show/geo.getTopArtists

        :param country: required
            (Required) : A country name, as defined by the ISO 3166-1 country
            names standard
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopArtists', auth=False, country=country, limit=limit, page=page)

    def get_top_tracks(self, country, limit=None, location=None, page=None):
        """
        Get the most popular tracks on Last.fm last week by country

        Authorization not required.

        http://www.last.fm/api/show/geo.getTopTracks

        :param country: required
            (Required) : A country name, as defined by the ISO 3166-1 country
            names standard
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param location: optional
            (Optional) : A metro name, to fetch the charts for (must be within the
            country specified)
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopTracks', auth=False, country=country, limit=limit, location=location, page=page)


class Group(Package):

    def get_hype(self, Group):
        """
        Get the hype list for a group

        Authorization not required.

        http://www.last.fm/api/show/group.getHype

        :param Group: required
            (Required) : The last.fm group name

        """
        return self._call('GET', 'getHype', auth=False, Group=Group)

    def get_members(self, group, limit=None, page=None):
        """
        Get a list of members for this group.

        Authorization not required.

        http://www.last.fm/api/show/group.getMembers

        :param group: required
            (Required) : The group name to fetch the members of.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The results page you would like to fetch

        """
        return self._call('GET', 'getMembers', auth=False, group=group, limit=limit, page=page)

    def get_weekly_album_chart(self, group, from_=None, to=None):
        """
        Get an album chart for a group, for a given date range. If no date
        range is supplied, it will return the most recent album chart for this
        group.

        Authorization not required.

        http://www.last.fm/api/show/group.getWeeklyAlbumChart

        :param group: required
            (Required) : The last.fm group name to fetch the charts of.
        :param from_: optional
            (Optional) : The date at which the chart should start from. See
            Group.getWeeklyChartList for more.
        :param to: optional
            (Optional) : The date at which the chart should end on. See
            Group.getWeeklyChartList for more.

        """
        return self._call('GET', 'getWeeklyAlbumChart', auth=False, group=group, from_=from_, to=to)

    def get_weekly_artist_chart(self, group, from_=None, to=None):
        """
        Get an artist chart for a group, for a given date range. If no date
        range is supplied, it will return the most recent album chart for this
        group.

        Authorization not required.

        http://www.last.fm/api/show/group.getWeeklyArtistChart

        :param group: required
            (Required) : The last.fm group name to fetch the charts of.
        :param from_: optional
            (Optional) : The date at which the chart should start from. See
            Group.getWeeklyChartList for more.
        :param to: optional
            (Optional) : The date at which the chart should end on. See
            Group.getWeeklyChartList for more.

        """
        return self._call('GET', 'getWeeklyArtistChart', auth=False, group=group, from_=from_, to=to)

    def get_weekly_chart_list(self, group):
        """
        Get a list of available charts for this group, expressed as date
        ranges which can be sent to the chart services.

        Authorization not required.

        http://www.last.fm/api/show/group.getWeeklyChartList

        :param group: required
            (Required) : The last.fm group name to fetch the charts list for.

        """
        return self._call('GET', 'getWeeklyChartList', auth=False, group=group)

    def get_weekly_track_chart(self, group, from_=None, to=None):
        """
        Get a track chart for a group, for a given date range. If no date
        range is supplied, it will return the most recent album chart for this
        group.

        Authorization not required.

        http://www.last.fm/api/show/group.getWeeklyTrackChart

        :param group: required
            (Required) : The last.fm group name to fetch the charts of.
        :param from_: optional
            (Optional) : The date at which the chart should start from. See
            Group.getWeeklyChartList for more.
        :param to: optional
            (Optional) : The date at which the chart should end on. See
            Group.getWeeklyChartList for more.

        """
        return self._call('GET', 'getWeeklyTrackChart', auth=False, group=group, from_=from_, to=to)


class Library(Package):

    def add_album(self, album, artist):
        """
        Add an album or collection of albums to a user's Last.fm library

        Authorization required.

        http://www.last.fm/api/show/library.addAlbum

        :param album: required, multiple
            [i] (Required) : The album or collection of albums that you wish to
            add. The indices of the albums that you pass MUST correspond to those
            of the artists.
        :param artist: required, multiple
            [i] (Required) : The artist or collection of artists that you wish to
            add.

        """
        return self._call('POST', 'addAlbum', auth=True, album=album, artist=artist)

    def add_artist(self, artist):
        """
        Add an artist to a user's Last.fm library

        Authorization required.

        http://www.last.fm/api/show/library.addArtist

        :param artist: required, multiple
            [i] (Required) : The artist or collection of artists you wish to add.

        """
        return self._call('POST', 'addArtist', auth=True, artist=artist)

    def add_track(self, artist, track):
        """
        Add a track to a user's Last.fm library

        Authorization required.

        http://www.last.fm/api/show/library.addTrack

        :param artist: required
            (Required) : The artist that composed the track
        :param track: required
            (Required) : The track name you wish to add

        """
        return self._call('POST', 'addTrack', auth=True, artist=artist, track=track)

    def get_albums(self, user, limit=None, page=None, artist=None):
        """
        A paginated list of all the albums in a user's library, with play
        counts and tag counts.

        Authorization not required.

        http://www.last.fm/api/show/library.getAlbums

        :param user: required
            (Required) : The user whose library you want to fetch.
        :param artist: optional
            (Optional) : An artist by which to filter tracks
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number you wish to scan to.

        """
        return self._call('GET', 'getAlbums', auth=False, user=user, artist=artist, limit=limit, page=page)

    def get_artists(self, user, limit=None, page=None):
        """
        A paginated list of all the artists in a user's library, with play
        counts and tag counts.

        Authorization not required.

        http://www.last.fm/api/show/library.getArtists

        :param user: required
            (Required) : The user whose library you want to fetch.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number you wish to scan to.

        """
        return self._call('GET', 'getArtists', auth=False, user=user, limit=limit, page=page)

    def get_tracks(self, user, album=None, limit=None, page=None, artist=None):
        """
        A paginated list of all the tracks in a user's library, with play
        counts and tag counts.

        Authorization not required.

        http://www.last.fm/api/show/library.getTracks

        :param user: required
            (Required) : The user whose library you want to fetch.
        :param album: optional
            (Optional) : An album by which to filter tracks (needs an artist)
        :param artist: optional
            (Optional) : An artist by which to filter tracks
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number you wish to scan to.

        """
        return self._call('GET', 'getTracks', auth=False, user=user, album=album, artist=artist, limit=limit, page=page)

    def remove_album(self, album, artist):
        """
        Remove an album from a user's Last.fm library

        Authorization required.

        http://www.last.fm/api/show/library.removeAlbum

        :param album: required
            (Required) : The name of the album you wish to remove
        :param artist: required
            (Required) : The artist that composed the album

        """
        return self._call('POST', 'removeAlbum', auth=True, album=album, artist=artist)

    def remove_artist(self, artist):
        """
        Remove an artist from a user's Last.fm library

        Authorization required.

        http://www.last.fm/api/show/library.removeArtist

        :param artist: required
            (Required) : The artist name you wish to remove

        """
        return self._call('POST', 'removeArtist', auth=True, artist=artist)

    def remove_scrobble(self, artist, timestamp, track):
        """
        Remove a scrobble from a user's Last.fm library

        Authorization required.

        http://www.last.fm/api/show/library.removeScrobble

        :param artist: required
            (Required) : The artist that composed the track
        :param timestamp: required
            (Required) : The unix timestamp of the scrobble that you wish to
            remove
        :param track: required
            (Required) : The name of the track

        """
        return self._call('POST', 'removeScrobble', auth=True, artist=artist, timestamp=timestamp, track=track)

    def remove_track(self, artist, track):
        """
        Remove a track from a user's Last.fm library

        Authorization required.

        http://www.last.fm/api/show/library.removeTrack

        :param artist: required
            (Required) : The artist that composed the track
        :param track: required
            (Required) : The name of the track that you wish to remove

        """
        return self._call('POST', 'removeTrack', auth=True, artist=artist, track=track)


class Playlist(Package):

    def add_track(self, artist, playlistID, track):
        """
        Add a track to a Last.fm user's playlist

        Authorization required.

        http://www.last.fm/api/show/playlist.addTrack

        :param artist: required
            (Required) : The artist name that corresponds to the track to be
            added.
        :param playlistID: required
            (Required) : The ID of the playlist - this is available in
            user.getPlaylists.
        :param track: required
            (Required) : The track name to add to the playlist.

        """
        return self._call('POST', 'addTrack', auth=True, artist=artist, playlistID=playlistID, track=track)

    def create(self, description=None, title=None):
        """
        Create a Last.fm playlist on behalf of a user

        Authorization required.

        http://www.last.fm/api/show/playlist.create

        :param description: optional
            (Optional) : Description for the playlist
        :param title: optional
            (Optional) : Title for the playlist

        """
        return self._call('POST', 'create', auth=True, description=description, title=title)


class Radio(Package):

    def get_playlist(self, speed_multiplier=None, buylinks=None, bitrate=None, rtp=None, discovery=None):
        """
        Fetch new radio content periodically in an XSPF format.

        Authorization not required.

        http://www.last.fm/api/show/radio.getPlaylist

        :param bitrate: optional
            (Optional) : What bitrate to stream content at, in kbps (supported
            bitrates are 64 and 128)
        :param buylinks: optional
            (Optional) : Whether the response should contain links for
            purchase/download, if available (default false)
        :param discovery: optional
            (Optional) : Whether to request last.fm content with discovery mode
            switched on.
        :param rtp: optional
            (Optional) : Whether the user is scrobbling or not during this radio
            session (helps content generation)
        :param speed_multiplier: optional
            (Optional) : The rate at which to provide the stream (supported
            multipliers are 1.0 and 2.0)

        """
        return self._call('GET', 'getPlaylist', auth=False, bitrate=bitrate, buylinks=buylinks, discovery=discovery,
                          rtp=rtp, speed_multiplier=speed_multiplier)

    def search(self, name):
        """
        Resolve the name of a resource into a station depending on which
        resource it is most likely to represent

        Authorization not required.

        http://www.last.fm/api/show/radio.search

        :param name: required
            (Required) : The tag or artist to resolve

        """
        return self._call('GET', 'search', auth=False, name=name)

    def tune(self, station, lang=None):
        """
        Tune in to a Last.fm radio station.

        Authorization not required.

        http://www.last.fm/api/show/radio.tune

        :param station: required
            (Required) : A lastfm:// radio URL
        :param lang: optional
            (Optional) : An ISO language code to determine the language to return
            the station name in, expressed as an ISO 639 alpha-2 code.

        """
        return self._call('GET', 'tune', auth=False, station=station, lang=lang)


class Tag(Package):

    def get_info(self, artist, lang=None):
        """
        Get the metadata for a tag

        Authorization not required.

        http://www.last.fm/api/show/tag.getInfo

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param lang: optional
            (Optional) : The language to return the biography in, expressed as an
            ISO 639 alpha-2 code.

        """
        return self._call('GET', 'getInfo', auth=False, artist=artist, lang=lang)

    def get_similar(self, tag):
        """
        Search for tags similar to this one. Returns tags ranked by
        similarity, based on listening data.

        Authorization not required.

        http://www.last.fm/api/show/tag.getSimilar

        :param tag: required
            (Required) : The tag name

        """
        return self._call('GET', 'getSimilar', auth=False, tag=tag)

    def get_top_albums(self, tag, limit=None, page=None):
        """
        Get the top albums tagged by this tag, ordered by tag count.

        Authorization not required.

        http://www.last.fm/api/show/tag.getTopAlbums

        :param tag: required
            (Required) : The tag name
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopAlbums', auth=False, tag=tag, limit=limit, page=page)

    def get_top_artists(self, tag, limit=None, page=None):
        """
        Get the top artists tagged by this tag, ordered by tag count.

        Authorization not required.

        http://www.last.fm/api/show/tag.getTopArtists

        :param tag: required
            (Required) : The tag name
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopArtists', auth=False, tag=tag, limit=limit, page=page)

    def get_top_tags(self):
        """
        Fetches the top global tags on Last.fm, sorted by popularity (number
        of times used)

        Authorization not required.

        http://www.last.fm/api/show/tag.getTopTags


        """
        return self._call('GET', 'getTopTags', auth=False)

    def get_top_tracks(self, tag, limit=None, page=None):
        """
        Get the top tracks tagged by this tag, ordered by tag count.

        Authorization not required.

        http://www.last.fm/api/show/tag.getTopTracks

        :param tag: required
            (Required) : The tag name
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getTopTracks', auth=False, tag=tag, limit=limit, page=page)

    def get_weekly_artist_chart(self, tag, limit=None, from_=None, to=None):
        """
        Get an artist chart for a tag, for a given date range. If no date
        range is supplied, it will return the most recent artist chart for
        this tag.

        Authorization not required.

        http://www.last.fm/api/show/tag.getWeeklyArtistChart

        :param tag: required
            (Required) : The tag name
        :param from_: optional
            (Optional) : The date at which the chart should start from. See
            Tag.getWeeklyChartList for more.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param to: optional
            (Optional) : The date at which the chart should end on. See
            Tag.getWeeklyChartList for more.

        """
        return self._call('GET', 'getWeeklyArtistChart', auth=False, tag=tag, from_=from_, limit=limit, to=to)

    def get_weekly_chart_list(self, tag):
        """
        Get a list of available charts for this tag, expressed as date ranges
        which can be sent to the chart services.

        Authorization not required.

        http://www.last.fm/api/show/tag.getWeeklyChartList

        :param tag: required
            (Required) : The tag name

        """
        return self._call('GET', 'getWeeklyChartList', auth=False, tag=tag)

    def search(self, tag, limit=None, page=None):
        """
        Search for a tag by name. Returns matches sorted by relevance.

        Authorization not required.

        http://www.last.fm/api/show/tag.search

        :param tag: required
            (Required) : The tag name
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 30.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'search', auth=False, tag=tag, limit=limit, page=page)


class Tasteometer(Package):

    def compare(self, type, value, limit=None):
        """
        Get a Tasteometer score from two inputs, along with a list of shared
        artists. If the input is a User some additional information is
        returned.

        Authorization not required.

        http://www.last.fm/api/show/tasteometer.compare

        :param type: required, multiple
            [1|2] (Required x 2) : 'user' | 'artists'
        :param value: required, multiple
            [1|2] (Required x 2) : [Last.fm username] | [Comma-separated artist
            names (max. 100)]
        :param limit: optional
            (Optional, default = 5) : How many shared artists to display

        """
        return self._call('GET', 'compare', auth=False, type=type, value=value, limit=limit)

    def compare_group(self):
        """
        This service has been deprecated and is no longer available.

        Authorization not required.

        http://www.last.fm/api/show/tasteometer.compareGroup


        """
        return self._call('GET', 'compareGroup', auth=False)


class Track(Package):

    def add_tags(self, artist, tags, track):
        """
        Tag an album using a list of user supplied tags.

        Authorization required.

        http://www.last.fm/api/show/track.addTags

        :param artist: required
            (Required) : The artist name
        :param tags: required
            (Required) : A comma delimited list of user supplied tags to apply to
            this track. Accepts a maximum of 10 tags.
        :param track: required
            (Required) : The track name

        """
        return self._call('POST', 'addTags', auth=True, artist=artist, tags=tags, track=track)

    def ban(self, artist, track):
        """
        Ban a track for a given user profile.

        Authorization required.

        http://www.last.fm/api/show/track.ban

        :param artist: required
            (Required) : An artist name (utf8 encoded)
        :param track: required
            (Required) : A track name (utf8 encoded)

        """
        return self._call('POST', 'ban', auth=True, artist=artist, track=track)

    def get_buylinks(self, artist, country, track, autocorrect=None, mbid=None):
        """
        Get a list of Buy Links for a particular Track. It is required that
        you supply either the artist and track params or the mbid param.

        Authorization not required.

        http://www.last.fm/api/show/track.getBuylinks

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param country: required
            (Required) : A country name or two character country code, as defined
            by the ISO 3166-1 country names standard.
        :param track: required
            (Required (unless mbid)] : The track name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist and track names into
            correct artist and track names, returning the correct version instead.
            The corrected artist and track name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the track

        """
        return self._call('GET', 'getBuylinks', auth=False, artist=artist, country=country, track=track,
                          autocorrect=autocorrect, mbid=mbid)

    def get_correction(self, artist, track):
        """
        Use the last.fm corrections data to check whether the supplied track
        has a correction to a canonical track

        Authorization not required.

        http://www.last.fm/api/show/track.getCorrection

        :param artist: required
            (Required) : The artist name to correct.
        :param track: required
            (Required) : The track name to correct.

        """
        return self._call('GET', 'getCorrection', auth=False, artist=artist, track=track)

    def get_fingerprint_metadata(self, fingerprintid):
        """
        Retrieve track metadata associated with a fingerprint id generated by
        the Last.fm Fingerprinter. Returns track elements, along with a 'rank'
        value between 0 and 1 reflecting the confidence for each match. See
        this blog post for more info.

        Authorization not required.

        http://www.last.fm/api/show/track.getFingerprintMetadata

        :param fingerprintid: required
            (Required) : The fingerprint id to look up

        """
        return self._call('GET', 'getFingerprintMetadata', auth=False, fingerprintid=fingerprintid)

    def get_info(self, artist, track, username=None, autocorrect=None, mbid=None):
        """
        Get the metadata for a track on Last.fm using the artist/track name or
        a musicbrainz id.

        Authorization not required.

        http://www.last.fm/api/show/track.getInfo

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param track: required
            (Required (unless mbid)] : The track name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist and track names into
            correct artist and track names, returning the correct version instead.
            The corrected artist and track name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the track
        :param username: optional
            (Optional) : The username for the context of the request. If supplied,
            the user's playcount for this track and whether they have loved the
            track is included in the response.

        """
        return self._call('GET', 'getInfo', auth=False, artist=artist, track=track, autocorrect=autocorrect, mbid=mbid,
                          username=username)

    def get_shouts(self, artist, track, autocorrect=None, mbid=None, limit=None, page=None):
        """
        Get shouts for this track. Also available as an rss feed.

        Authorization not required.

        http://www.last.fm/api/show/track.getShouts

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param track: required
            (Required (unless mbid)] : The track name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist and track names into
            correct artist and track names, returning the correct version instead.
            The corrected artist and track name will be returned in the response.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param mbid: optional
            (Optional) : The musicbrainz id for the track
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getShouts', auth=False, artist=artist, track=track, autocorrect=autocorrect,
                          limit=limit, mbid=mbid, page=page)

    def get_similar(self, artist, track, autocorrect=None, limit=None, mbid=None):
        """
        Get the similar tracks for this track on Last.fm, based on listening
        data.

        Authorization not required.

        http://www.last.fm/api/show/track.getSimilar

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param track: required
            (Required (unless mbid)] : The track name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist and track names into
            correct artist and track names, returning the correct version instead.
            The corrected artist and track name will be returned in the response.
        :param limit: optional
            (Optional) : Maximum number of similar tracks to return
        :param mbid: optional
            (Optional) : The musicbrainz id for the track

        """
        return self._call('GET', 'getSimilar', auth=False, artist=artist, track=track, autocorrect=autocorrect,
                          limit=limit, mbid=mbid)

    def get_tags(self, artist, track, autocorrect=None, user=None, mbid=None):
        """
        Get the tags applied by an individual user to a track on Last.fm. To
        retrieve the list of top tags applied to a track by all users use
        track.getTopTags.

        Authorization not required.

        http://www.last.fm/api/show/track.getTags

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param track: required
            (Required (unless mbid)] : The track name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist and track names into
            correct artist and track names, returning the correct version instead.
            The corrected artist and track name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the track
        :param user: optional
            (Optional) : If called in non-authenticated mode you must specify the
            user to look up

        """
        return self._call('GET', 'getTags', auth=False, artist=artist, track=track, autocorrect=autocorrect, mbid=mbid,
                          user=user)

    def get_top_fans(self, artist, track, autocorrect=None, mbid=None):
        """
        Get the top fans for this track on Last.fm, based on listening data.
        Supply either track & artist name or musicbrainz id.

        Authorization not required.

        http://www.last.fm/api/show/track.getTopFans

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param track: required
            (Required (unless mbid)] : The track name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist and track names into
            correct artist and track names, returning the correct version instead.
            The corrected artist and track name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the track

        """
        return self._call('GET', 'getTopFans', auth=False, artist=artist, track=track, autocorrect=autocorrect,
                          mbid=mbid)

    def get_top_tags(self, artist, track, autocorrect=None, mbid=None):
        """
        Get the top tags for this track on Last.fm, ordered by tag count.
        Supply either track & artist name or mbid.

        Authorization not required.

        http://www.last.fm/api/show/track.getTopTags

        :param artist: required
            (Required (unless mbid)] : The artist name
        :param track: required
            (Required (unless mbid)] : The track name
        :param autocorrect: optional, boolean
            [0|1] (Optional) : Transform misspelled artist and track names into
            correct artist and track names, returning the correct version instead.
            The corrected artist and track name will be returned in the response.
        :param mbid: optional
            (Optional) : The musicbrainz id for the track

        """
        return self._call('GET', 'getTopTags', auth=False, artist=artist, track=track, autocorrect=autocorrect,
                          mbid=mbid)

    def love(self, artist, track):
        """
        Love a track for a user profile.

        Authorization required.

        http://www.last.fm/api/show/track.love

        :param artist: required
            (Required) : An artist name (utf8 encoded)
        :param track: required
            (Required) : A track name (utf8 encoded)

        """
        return self._call('POST', 'love', auth=True, artist=artist, track=track)

    def remove_tag(self, artist, tag, track):
        """
        Remove a user's tag from a track.

        Authorization required.

        http://www.last.fm/api/show/track.removeTag

        :param artist: required
            (Required) : The artist name
        :param tag: required
            (Required) : A single user tag to remove from this track.
        :param track: required
            (Required) : The track name

        """
        return self._call('POST', 'removeTag', auth=True, artist=artist, tag=tag, track=track)

    def scrobble(self, artist, timestamp, track, album=None, mbid=None, albumArtist=None, context=None, streamId=None,
                 duration=None, trackNumber=None, chosenByUser=None):
        """
        Used to add a track-play to a user's profile. Scrobble a track, or a
        batch of tracks. Tracks are passed to the service using array notation
        for each of the below params, up to a maximum of 50 scrobbles per
        batch [0<=i<=49]. If you are only sending a single scrobble the array
        notation may be ommited. Note: Extra care should be taken while
        calculating the signature when using array notation as the parameter
        names MUST be sorted according to the ASCII table (i.e., artist[10]
        comes before artist[1]). It is important to not use the corrections
        returned by the now playing service as input for the scrobble request,
        unless they have been explicitly approved by the user. Parameter names
        are case sensitive.

        Authorization required.

        http://www.last.fm/api/show/track.scrobble

        :param artist: required, multiple
            [i] (Required) : The artist name.
        :param timestamp: required, multiple
            [i] (Required) : The time the track started playing, in UNIX timestamp
            format (integer number of seconds since 00:00:00, January 1st 1970
            UTC). This must be in the UTC time zone.
        :param track: required, multiple
            [i] (Required) : The track name.
        :param album: optional, multiple
            [i] (Optional) : The album name.
        :param albumArtist: optional, multiple
            [i] (Optional) : The album artist - if this differs from the track
            artist.
        :param chosenByUser: optional, multiple
            [i] (Optional) : Set to 1 if the user chose this song, or 0 if the
            song was chosen by someone else (such as a radio station or
            recommendation service). Assumes 1 if not specified
        :param context: optional, multiple
            [i] (Optional) : Sub-client version (not public, only enabled for
            certain API keys)
        :param duration: optional, multiple
            [i] (Optional) : The length of the track in seconds.
        :param mbid: optional, multiple
            [i] (Optional) : The MusicBrainz Track ID.
        :param streamId: optional, multiple
            [i] (Optional) : The stream id for this track received from the
            radio.getPlaylist service, if scrobbling Last.fm radio
        :param trackNumber: optional, multiple
            [i] (Optional) : The track number of the track on the album.

        """
        return self._call('POST', 'scrobble', auth=True, artist=artist, timestamp=timestamp, track=track, album=album,
                          albumArtist=albumArtist, chosenByUser=chosenByUser, context=context, duration=duration,
                          mbid=mbid, streamId=streamId, trackNumber=trackNumber)

    def search(self, track, limit=None, page=None, artist=None):
        """
        Search for a track by track name. Returns track matches sorted by
        relevance.

        Authorization not required.

        http://www.last.fm/api/show/track.search

        :param track: required
            (Required) : The track name
        :param artist: optional
            (Optional) : Narrow your search by specifying an artist.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 30.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'search', auth=False, track=track, artist=artist, limit=limit, page=page)

    def share(self, artist, recipient, track, message=None, public=None):
        """
        Share a track twith one or more Last.fm users or other friends.

        Authorization required.

        http://www.last.fm/api/show/track.share

        :param artist: required
            (Required) : An artist name.
        :param recipient: required
            (Required): Email Address | Last.fm Username - A comma delimited list
            of email addresses or Last.fm usernames. Maximum is 10.
        :param track: required
            (Required) : A track name.
        :param message: optional
            (Optional): An optional message to send with the recommendation. If
            not supplied a default message will be used.
        :param public: optional
            (Optional): Optionally show in the sharing users activity feed.
            Defaults to 0 (false).

        """
        return self._call('POST', 'share', auth=True, artist=artist, recipient=recipient, track=track, message=message,
                          public=public)

    def unban(self, artist, track):
        """
        UnBan a track for a user profile.

        Authorization required.

        http://www.last.fm/api/show/track.unban

        :param artist: required
            (Required) : An artist name (utf8 encoded)
        :param track: required
            (Required) : A track name (utf8 encoded)

        """
        return self._call('POST', 'unban', auth=True, artist=artist, track=track)

    def unlove(self, artist, track):
        """
        UnLove a track for a user profile.

        Authorization required.

        http://www.last.fm/api/show/track.unlove

        :param artist: required
            (Required) : An artist name (utf8 encoded)
        :param track: required
            (Required) : A track name (utf8 encoded)

        """
        return self._call('POST', 'unlove', auth=True, artist=artist, track=track)

    def update_now_playing(self, artist, track, album=None, mbid=None, albumArtist=None, context=None, duration=None,
                           trackNumber=None):
        """
        Used to notify Last.fm that a user has started listening to a track.
        Parameter names are case sensitive.

        Authorization required.

        http://www.last.fm/api/show/track.updateNowPlaying

        :param artist: required
            (Required) : The artist name.
        :param track: required
            (Required) : The track name.
        :param album: optional
            (Optional) : The album name.
        :param albumArtist: optional
            (Optional) : The album artist - if this differs from the track artist.
        :param context: optional
            (Optional) : Sub-client version (not public, only enabled for certain
            API keys)
        :param duration: optional
            (Optional) : The length of the track in seconds.
        :param mbid: optional
            (Optional) : The MusicBrainz Track ID.
        :param trackNumber: optional
            (Optional) : The track number of the track on the album.

        """
        return self._call('POST', 'updateNowPlaying', auth=True, artist=artist, track=track, album=album,
                          albumArtist=albumArtist, context=context, duration=duration, mbid=mbid,
                          trackNumber=trackNumber)


class User(Package):

    def get_artist_tracks(self, artist, user, startTimestamp=None, page=None, endTimestamp=None):
        """
        Get a list of tracks by a given artist scrobbled by this user,
        including scrobble time. Can be limited to specific timeranges,
        defaults to all time.

        Authorization not required.

        http://www.last.fm/api/show/user.getArtistTracks

        :param artist: required
            (Required) : The artist name you are interested in
        :param user: required
            (Required) : The last.fm username to fetch the recent tracks of.
        :param endTimestamp: optional
            (Optional) : An unix timestamp to end at.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param startTimestamp: optional
            (Optional) : An unix timestamp to start at.

        """
        return self._call('GET', 'getArtistTracks', auth=False, artist=artist, user=user, endTimestamp=endTimestamp,
                          page=page, startTimestamp=startTimestamp)

    def get_banned_tracks(self, user, limit=None, page=None):
        """
        Returns the tracks banned by the user

        Authorization not required.

        http://www.last.fm/api/show/user.getBannedTracks

        :param user: required
            (Required) : The user name
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getBannedTracks', auth=False, user=user, limit=limit, page=page)

    def get_events(self, user, limit=None, festivalsonly=None, page=None):
        """
        Get a list of upcoming events that this user is attending. Easily
        integratable into calendars, using the ical standard (see 'more
        formats' section below).

        Authorization not required.

        http://www.last.fm/api/show/user.getEvents

        :param user: required
            (Required) : The user to fetch the events for.
        :param festivalsonly: optional, boolean
            [0|1] (Optional) : Whether only festivals should be returned, or all
            events.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getEvents', auth=False, user=user, festivalsonly=festivalsonly, limit=limit,
                          page=page)

    def get_friends(self, user, limit=None, page=None, recenttracks=None):
        """
        Get a list of the user's friends on Last.fm.

        Authorization not required.

        http://www.last.fm/api/show/user.getFriends

        :param user: required
            (Required) : The last.fm username to fetch the friends of.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param recenttracks: optional
            (Optional) : Whether or not to include information about friends'
            recent listening in the response.

        """
        return self._call('GET', 'getFriends', auth=False, user=user, limit=limit, page=page, recenttracks=recenttracks)

    def get_info(self, user=None):
        """
        Get information about a user profile.

        Authorization not required.

        http://www.last.fm/api/show/user.getInfo

        :param user: optional
            (Optional) : The user to fetch info for. Defaults to the authenticated
            user.

        """
        return self._call('GET', 'getInfo', auth=False, user=user)

    def get_loved_tracks(self, user, limit=None, page=None):
        """
        Get the last 50 tracks loved by a user.

        Authorization not required.

        http://www.last.fm/api/show/user.getLovedTracks

        :param user: required
            (Required) : The user name to fetch the loved tracks for.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getLovedTracks', auth=False, user=user, limit=limit, page=page)

    def get_neighbours(self, user, limit=None):
        """
        Get a list of a user's neighbours on Last.fm.

        Authorization not required.

        http://www.last.fm/api/show/user.getNeighbours

        :param user: required
            (Required) : The last.fm username to fetch the neighbours of.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.

        """
        return self._call('GET', 'getNeighbours', auth=False, user=user, limit=limit)

    def get_new_releases(self, user, userecs=None):
        """
        Gets a list of forthcoming releases based on a user's musical taste.

        Authorization not required.

        http://www.last.fm/api/show/user.getNewReleases

        :param user: required
            (Required) : The Last.fm username.
        :param userecs: optional
            (Optional) : 0 or 1. If 1, the feed contains new releases based on
            Last.fm's artist recommendations for this user. Otherwise, it is based
            on their library (the default).

        """
        return self._call('GET', 'getNewReleases', auth=False, user=user, userecs=userecs)

    def get_past_events(self, user, limit=None, page=None):
        """
        Get a paginated list of all events a user has attended in the past.

        Authorization not required.

        http://www.last.fm/api/show/user.getPastEvents

        :param user: required
            (Required) : The username to fetch the events for.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to scan to.

        """
        return self._call('GET', 'getPastEvents', auth=False, user=user, limit=limit, page=page)

    def get_personal_tags(self, tag, taggingtype, user, limit=None, page=None):
        """
        Get the user's personal tags

        Authorization not required.

        http://www.last.fm/api/show/user.getPersonalTags

        :param tag: required
            (Required) : The tag you're interested in.
        :param taggingtype: required
            [artist|album|track] (Required) : The type of items which have been
            tagged
        :param user: required
            (Required) : The user who performed the taggings.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getPersonalTags', auth=False, tag=tag, taggingtype=taggingtype, user=user,
                          limit=limit, page=page)

    def get_playlists(self, user):
        """
        Get a list of a user's playlists on Last.fm.

        Authorization not required.

        http://www.last.fm/api/show/user.getPlaylists

        :param user: required
            (Required) : The last.fm username to fetch the playlists of.

        """
        return self._call('GET', 'getPlaylists', auth=False, user=user)

    def get_recent_stations(self, user, limit=None, page=None):
        """
        Get a list of the recent Stations listened to by this user.

        Authorization required.

        http://www.last.fm/api/show/user.getRecentStations

        :param user: required
            (Required) : The last.fm username to fetch the recent Stations of.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 10.
            Maximum is 25.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getRecentStations', auth=True, user=user, limit=limit, page=page)

    def get_recent_tracks(self, user, extended=None, from_=None, to=None, limit=None, page=None):
        """
        Get a list of the recent tracks listened to by this user. Also
        includes the currently playing track with the nowplaying="true"
        attribute if the user is currently listening.

        Authorization not required.

        http://www.last.fm/api/show/user.getRecentTracks

        :param user: required
            (Required) : The last.fm username to fetch the recent tracks of.
        :param extended: optional
            (0|1) (Optional) : Includes extended data in each artist, and whether
            or not the user has loved each track
        :param from_: optional
            (Optional) : Beginning timestamp of a range - only display scrobbles
            after this time, in UNIX timestamp format (integer number of seconds
            since 00:00:00, January 1st 1970 UTC). This must be in the UTC time
            zone.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
            Maximum is 200.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param to: optional
            (Optional) : End timestamp of a range - only display scrobbles before
            this time, in UNIX timestamp format (integer number of seconds since
            00:00:00, January 1st 1970 UTC). This must be in the UTC time zone.

        """
        return self._call('GET', 'getRecentTracks', auth=False, user=user, extended=extended, from_=from_, limit=limit,
                          page=page, to=to)

    def get_recommended_artists(self, limit=None, page=None):
        """
        Get Last.fm artist recommendations for a user

        Authorization required.

        http://www.last.fm/api/show/user.getRecommendedArtists

        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getRecommendedArtists', auth=True, limit=limit, page=page)

    def get_recommended_events(self, country=None, festivalsonly=None, longitude=None, limit=None, latitude=None,
                               page=None):
        """
        Get a paginated list of all events recommended to a user by Last.fm,
        based on their listening profile.

        Authorization required.

        http://www.last.fm/api/show/user.getRecommendedEvents

        :param country: optional
            (Optional) : Optionally find events in a particular country (use
            EITHER lat/long or country)
        :param festivalsonly: optional, boolean
            [0|1] (Optional) : Whether only festivals should be returned, or all
            events.
        :param latitude: optional
            (Optional) : Optionally find events at a particular location (must be
            paired with a valid longitude)
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 20.
        :param longitude: optional
            (Optional) : Optionally find events at a particular location (must be
            paired with a valid latitude)
        :param page: optional
            (Optional) : The page number to scan to.

        """
        return self._call('GET', 'getRecommendedEvents', auth=True, country=country, festivalsonly=festivalsonly,
                          latitude=latitude, limit=limit, longitude=longitude, page=page)

    def get_shouts(self, user, limit=None, page=None):
        """
        Get shouts for this user. Also available as an rss feed.

        Authorization not required.

        http://www.last.fm/api/show/user.getShouts

        :param user: required
            (Required) : The username to fetch shouts for
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.

        """
        return self._call('GET', 'getShouts', auth=False, user=user, limit=limit, page=page)

    def get_top_albums(self, user, limit=None, page=None, period=None):
        """
        Get the top albums listened to by a user. You can stipulate a time
        period. Sends the overall chart by default.

        Authorization not required.

        http://www.last.fm/api/show/user.getTopAlbums

        :param user: required
            (Required) : The user name to fetch top albums for.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param period: optional
            (Optional) : overall | 7day | 1month | 3month | 6month | 12month - The
            time period over which to retrieve top albums for.

        """
        return self._call('GET', 'getTopAlbums', auth=False, user=user, limit=limit, page=page, period=period)

    def get_top_artists(self, user, limit=None, page=None, period=None):
        """
        Get the top artists listened to by a user. You can stipulate a time
        period. Sends the overall chart by default.

        Authorization not required.

        http://www.last.fm/api/show/user.getTopArtists

        :param user: required
            (Required) : The user name to fetch top artists for.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param period: optional
            (Optional) : overall | 7day | 1month | 3month | 6month | 12month - The
            time period over which to retrieve top artists for.

        """
        return self._call('GET', 'getTopArtists', auth=False, user=user, limit=limit, page=page, period=period)

    def get_top_tags(self, user, limit=None):
        """
        Get the top tags used by this user.

        Authorization not required.

        http://www.last.fm/api/show/user.getTopTags

        :param user: required
            (Required) : The user name
        :param limit: optional
            (Optional) : Limit the number of tags returned

        """
        return self._call('GET', 'getTopTags', auth=False, user=user, limit=limit)

    def get_top_tracks(self, user, limit=None, page=None, period=None):
        """
        Get the top tracks listened to by a user. You can stipulate a time
        period. Sends the overall chart by default.

        Authorization not required.

        http://www.last.fm/api/show/user.getTopTracks

        :param user: required
            (Required) : The user name to fetch top tracks for.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The page number to fetch. Defaults to first page.
        :param period: optional
            (Optional) : overall | 7day | 1month | 3month | 6month | 12month - The
            time period over which to retrieve top tracks for.

        """
        return self._call('GET', 'getTopTracks', auth=False, user=user, limit=limit, page=page, period=period)

    def get_weekly_album_chart(self, user, to=None, from_=None):
        """
        Get an album chart for a user profile, for a given date range. If no
        date range is supplied, it will return the most recent album chart for
        this user.

        Authorization not required.

        http://www.last.fm/api/show/user.getWeeklyAlbumChart

        :param user: required
            (Required) : The last.fm username to fetch the charts of.
        :param from_: optional
            (Optional) : The date at which the chart should start from. See
            User.getChartsList for more.
        :param to: optional
            (Optional) : The date at which the chart should end on. See
            User.getChartsList for more.

        """
        return self._call('GET', 'getWeeklyAlbumChart', auth=False, user=user, from_=from_, to=to)

    def get_weekly_artist_chart(self, user, to=None, from_=None):
        """
        Get an artist chart for a user profile, for a given date range. If no
        date range is supplied, it will return the most recent artist chart
        for this user.

        Authorization not required.

        http://www.last.fm/api/show/user.getWeeklyArtistChart

        :param user: required
            (Required) : The last.fm username to fetch the charts of.
        :param from_: optional
            (Optional) : The date at which the chart should start from. See
            User.getWeeklyChartList for more.
        :param to: optional
            (Optional) : The date at which the chart should end on. See
            User.getWeeklyChartList for more.

        """
        return self._call('GET', 'getWeeklyArtistChart', auth=False, user=user, from_=from_, to=to)

    def get_weekly_chart_list(self, user):
        """
        Get a list of available charts for this user, expressed as date ranges
        which can be sent to the chart services.

        Authorization not required.

        http://www.last.fm/api/show/user.getWeeklyChartList

        :param user: required
            (Required) : The last.fm username to fetch the charts list for.

        """
        return self._call('GET', 'getWeeklyChartList', auth=False, user=user)

    def get_weekly_track_chart(self, user, to=None, from_=None):
        """
        Get a track chart for a user profile, for a given date range. If no
        date range is supplied, it will return the most recent track chart for
        this user.

        Authorization not required.

        http://www.last.fm/api/show/user.getWeeklyTrackChart

        :param user: required
            (Required) : The last.fm username to fetch the charts of.
        :param from_: optional
            (Optional) : The date at which the chart should start from. See
            User.getWeeklyChartList for more.
        :param to: optional
            (Optional) : The date at which the chart should end on. See
            User.getWeeklyChartList for more.

        """
        return self._call('GET', 'getWeeklyTrackChart', auth=False, user=user, from_=from_, to=to)

    def shout(self, message, user):
        """
        Shout on this user's shoutbox

        Authorization required.

        http://www.last.fm/api/show/user.shout

        :param message: required
            (Required) : The message to post to the shoutbox.
        :param user: required
            (Required) : The name of the user to shout on.

        """
        return self._call('POST', 'shout', auth=True, message=message, user=user)

    def sign_up(self):
        """

        Authorization required.

        http://www.last.fm/api/show/user.signUp


        """
        return self._call('GET', 'signUp', auth=True)

    def terms(self):
        """

        Authorization required.

        http://www.last.fm/api/show/user.terms


        """
        return self._call('GET', 'terms', auth=True)


class Venue(Package):

    def get_events(self, venue, festivalsonly=None):
        """
        Get a list of upcoming events at this venue.

        Authorization not required.

        http://www.last.fm/api/show/venue.getEvents

        :param venue: required
            (Required) :The id for the venue you would like to fetch event
            listings for.
        :param festivalsonly: optional, boolean
            [0|1] (Optional) : Whether only festivals should be returned, or all
            events.

        """
        return self._call('GET', 'getEvents', auth=False, venue=venue, festivalsonly=festivalsonly)

    def get_past_events(self, venue, limit=None, festivalsonly=None, page=None):
        """
        Get a paginated list of all the events held at this venue in the past.

        Authorization not required.

        http://www.last.fm/api/show/venue.getPastEvents

        :param venue: required
            (Required) :The id for the venue you would like to fetch event
            listings for.
        :param festivalsonly: optional, boolean
            [0|1] (Optional) : Whether only festivals should be returned, or all
            events.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) :The page of results to return.

        """
        return self._call('GET', 'getPastEvents', auth=False, venue=venue, festivalsonly=festivalsonly, limit=limit,
                          page=page)

    def search(self, venue, country=None, limit=None, page=None):
        """
        Search for a venue by venue name

        Authorization not required.

        http://www.last.fm/api/show/venue.search

        :param venue: required
            (Required) : The venue name you would like to search for.
        :param country: optional
            (Optional) : Filter your results by country. Expressed as an ISO
            3166-2 code.
        :param limit: optional
            (Optional) : The number of results to fetch per page. Defaults to 50.
        :param page: optional
            (Optional) : The results page you would like to fetch

        """
        return self._call('GET', 'search', auth=False, venue=venue, country=country, limit=limit, page=page)