import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
import subprocess
import sys


def download_spacy_model(model_name="pt_core_news_sm"):
    """
    Download and load a SpaCy model programmatically.
    """
    try:
        # Load the SpaCy model if already installed
        return spacy.load(model_name)
    except OSError:
        # If not installed, download and install
        print(f"Downloading and installing {model_name}...", file=sys.stderr)
        subprocess.check_call([sys.executable, "-m", "spacy", "download", model_name])
        return spacy.load(model_name)
