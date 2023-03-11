import pyaudio
import wave
import keyboard
import threading
import whisper
import openai
import warnings
import config 
import json
import base64
import requests
import wave
import pyaudio

# openai ChatGPT API
openai.api_key = config.api_key

# whisper audio
model = whisper.load_model(config.wmodel)


# define audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# define file name
FILE_NAME = "recording.wav"

# create PyAudio object
audio = pyaudio.PyAudio()

# define push-to-talk button SEE CONFIG
PTT_BUTTON = config.PTT_BUTTON

#import tts model from config
tts_model = config.tts_model

# get list of available audio input devices
input_device_count = audio.get_device_count()
input_devices = {}
for i in range(input_device_count):
    device_info = audio.get_device_info_by_index(i)
    if device_info['maxInputChannels'] > 0:
        device_name = device_info['name']
        # Check if device name is already in input_devices dictionary
        if device_name not in input_devices.values():
            input_devices[i] = device_name
if not input_devices:
    raise Exception("No audio input devices found.")

# Print list of available input devices
print("Available input devices:")
for i, name in input_devices.items():
    print(f"{i}: {name}")
print()

# let user select input device by index
input_device_index = None
while input_device_index not in input_devices:
    try:
        input_device_index = int(input("Select input device by index: "))
    except ValueError:
        pass
if input_device_index is not None:
    print(f"Using input device: {input_devices[input_device_index]}")
else:
    print("No input device selected.")

# create a flag to indicate whether a recording is currently in progress
recording_in_progress = False

# start recording function
def start_recording():
    # set the flag to indicate that a recording is in progress
    global recording_in_progress
    recording_in_progress = True

    # create audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK, input_device_index=input_device_index)

    # create audio frames list
    frames = []

    # record audio while push-to-talk button is held down
    while keyboard.is_pressed(PTT_BUTTON):
        data = stream.read(CHUNK)
        frames.append(data)

    # stop audio stream
    stream.stop_stream()
    stream.close()

    # write audio frames to file
    wf = wave.open(FILE_NAME, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

    # set the flag to indicate that the recording is complete
    recording_in_progress = False

    # print message when recording stops
    print("Done...")
   
    # print recording whisper transcription
    result = model.transcribe("recording.wav", language="en")
    with open("output.txt", "w") as f:
            f.write(result['text'].strip() + '\n')
            f.close()
    print("English: " + result['text'].lstrip())
    
    
    translation = translate_to_japanese(result['text'])
    with open("output_translated.txt", "w") as f:
            f.write(result['text'].strip() + '\n')
            f.close()
    print(f"Japanese: {translation['choices'][0]['text'].strip()}")
    japanese_text = translation['choices'][0]['text'].strip()
    print("Playing Audio...")
    synthesize_and_play_audio(japanese_text)


def synthesize_and_play_audio(japanese_text):
    # Input Payload
    payload = {
        "data": [
            japanese_text,
            "Japanese",
            0.6,
            0.668,
            1,
            False
        ]
    }
    # Send request to server and receive response object
    url = f"http://127.0.0.1:7860/run/{tts_model}"
    response = requests.post(url, data=json.dumps(payload))
    response_obj = json.loads(response.text)
    # Remove prefix and suffix from base64 string
    audio_data = response_obj["data"][1].split(", 'is_generating'")[0]
    audio_data = audio_data.replace("data:audio/wav;base64,", "")
    # Decode base64 audio data
    audio_data = base64.b64decode(audio_data)
    # Save audio data as .wav file
    with wave.open("output.wav", "wb") as output_file:
        output_file.setnchannels(1)
        output_file.setsampwidth(2)
        output_file.setframerate(22050)
        output_file.writeframesraw(audio_data)

    # Play audio file
    with wave.open("output.wav", "rb") as input_file:
        audio = pyaudio.PyAudio()
        stream = audio.open(format=audio.get_format_from_width(input_file.getsampwidth()),
                            channels=input_file.getnchannels(),
                            rate=input_file.getframerate(),
                            output=True)
        data = input_file.readframes(1024)
        while data:
            stream.write(data)
            data = input_file.readframes(1024)
        stream.stop_stream()
        stream.close()
        audio.terminate()

# translates english text to japanese text utilizing OpenAI API
def translate_to_japanese(result):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Translate this text to Japanese: {result}\n\nTranslation:"),
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return(response) 

# create keyboard event handler function
def on_press(event):
    # start recording if the push-to-talk button is pressed and a recording is not already in progress
    global recording_in_progress
    if event.name == PTT_BUTTON and not recording_in_progress:
        print("\nRecording...")
        threading.Thread(target=start_recording).start()

def main():
    # print message to indicate program is running
    warnings.filterwarnings("ignore", category=UserWarning, message="FP16 is not supported on CPU; using FP32 instead")
    print(f"Press and hold {PTT_BUTTON} to start recording.")
    # listen for hotkey events
    keyboard.hook(on_press)
    try:
        # wait for any key to be pressed
        keyboard.wait()
    except KeyboardInterrupt:
        pass
    # wait for any key to be pressed
    keyboard.wait()
    # close the PyAudio object
    audio.terminate()

if __name__ == '__main__':
    main()
