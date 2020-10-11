import os

# 'http://localhost:8501/v1/models/bert:predict'
API_URI = os.environ['API_URI']

INDICES_GENRE_MAPPING_LOCATION = './cog/bert/2/indices_genre.json'
MAX_LENGTH = 200
PADDING = 'max_length'
TRUNCATION = True