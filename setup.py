import nltk
import ssl
import os

# Handle SSL certificate issues
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Ensure NLTK data directory exists
nltk_data_dir = os.path.expanduser('~/nltk_data')
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

# Download required NLTK data
required_data = [
    'stopwords',
    'punkt', 
    'averaged_perceptron_tagger',
    'maxent_ne_chunker',
    'words'
]

for data in required_data:
    try:
        nltk.data.find(f'tokenizers/{data}' if data == 'punkt' else 
                      f'taggers/{data}' if 'tagger' in data else
                      f'chunkers/{data}' if 'chunker' in data else
                      f'corpora/{data}')
    except LookupError:
        print(f"Downloading {data}...")
        nltk.download(data, quiet=True)

print("NLTK setup complete!")