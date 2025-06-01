from pyannote.audio import Pipeline

def run_diarization(audio_path, token):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=token)
    diarization = pipeline(audio_path, num_speakers=2)
    return diarization
