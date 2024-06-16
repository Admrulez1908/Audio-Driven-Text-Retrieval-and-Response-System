import whisper
import pinecone
from sentence_transformers import SentenceTransformer
from transformers import LlamaForCausalLM, LlamaTokenizer
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import nltk
from nltk.tokenize import sent_tokenize
import os
from dotenv import load_dotenv
load_dotenv()

nltk.download('punkt')
