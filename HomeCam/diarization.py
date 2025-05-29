import whisper
from pyannote.audio import Pipeline

def run_stt(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path, language="ko")
    return result.get("segments", [])

def run_diarization(audio_path, token):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=token)
    diarization = pipeline(audio_path, num_speakers=2)
    return diarization

def map_speaker_segments(segments, diarization):
    speaker_turns = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        matched_segments = [
            s["text"] for s in segments if not (s["end"] < turn.start or turn.end < s["start"])
        ]
        if matched_segments:
            text = "".join(matched_segments).strip()
            speaker_turns.append((speaker, text))
    return speaker_turns
