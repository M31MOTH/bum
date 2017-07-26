"""
Musicbrainz related functions.
"""
import musicbrainzngs as mus


def init():
    """Initialize musicbrainz."""
    mus.set_useragent("python-bum: A cover art daemon.",
                      "0.0.1",
                      "https://github.com/dylanaraps/bum")


def get_cover(song_data):
    """Download the cover art."""
    try:
        data = mus.search_releases(artist=song_data[0],
                                   release=song_data[2], limit=1)
        release_id = data["release-list"][0]["release-group"]["id"]
        return mus.get_release_group_image_front(release_id, size=250)

    except mus.NetworkError:
        get_cover(song_data)

    except mus.ResponseError:
        print("error: Couldn't find album art for",
              f"{song_data[0]} - {song_data[1]}")
