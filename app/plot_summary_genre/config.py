API_URI = 'http://localhost:8501/v1/models/bert:predict'
INDICES_GENRE_MAPPING_LOCATION = './cog/bert/2/indices_genre.json'
TOKENIZER = BertTokenizer.from_pretrained('bert-base-uncased')

MAX_LENGTH = 200
PADDING = 'max_length'
TRUNCATION = True