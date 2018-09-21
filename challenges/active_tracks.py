"""
Given a list of track data, return the IDs of active tracks.
The list may contain duplicate tracks.

    [
        {
            'id': 1,
            'name': 'In Arms',
            'active': True,
        },
        {
            'id': 2,
            'name': 'Deep Dip',
            'active': False,
        },
        {
            'id': 3,
            'name': 'Panic Room',
            'active': True,
        },
        {
            'id': 1,
            'name': 'In Arms',
            'active': True,
        },
    ]  # should return [1, 3]

"""

def active_tracks(tracks):
    """Given a list of track data as dictionaries, return the IDs of active tracks as list."""
    track_id = set()
    for song in tracks:
        if song['active']:
            track_id.add(song['id'])
    return list(track_id)