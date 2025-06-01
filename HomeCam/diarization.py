from pyannote.audio import Pipeline


def load_Huggingface_token_from_file(path="../keys/Huggingface_token.txt"):
    with open(path, "r") as f:
        return f.read().strip()


def run_diarization(audio_path):
    token = load_Huggingface_token_from_file()
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=token)
    diarization = pipeline(audio_path, num_speakers=2)
    return diarization
