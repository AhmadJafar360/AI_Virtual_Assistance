import os
import speech_recognition as srec
import sounddevice as sd

from gtts import gTTS
from scipy.io.wavfile import write

def input_suara():
    print("Merekam...")
    fs = 44100  # Sample rate
    duration = 5  # seconds
    try:
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
        sd.wait()  # Tunggu hingga selesai
        filename = "input.wav"
        write(filename, fs, recording)  # Simpan sebagai file WAV
        print("Rekaman selesai")
        return filename
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None

def output_suara(teks):
    language = 'id'
    filename = "Voice.mp3"
    try:
        suara = gTTS(text=teks, lang=language, slow=False)
        suara.save(filename)
        if os.name == 'nt': #Windows
            os.startfile(filename)
        else: #Linux/MacOS
            os.system(f"mpg123 {filename}")
    except Exception as e:
        print(f"Terjadi kesalahan saat memproses suara: {e}")

def talk():
    file_input = input_suara()
    if file_input:
        print("File suara tersimpan.")
        output_suara("Ini adalah contoh output suara")

talk()