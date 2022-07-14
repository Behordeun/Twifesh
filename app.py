from twifesh.api import Stream, Profile, Profiler
from keys import bearer_token, access_token, access_token_secret, consumer_key, consumer_secret

twifesh = Stream(bearer_token, keywords=[], write_file=True)

twifesh.stream_now()