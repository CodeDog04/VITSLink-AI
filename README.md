# OpenAI English to Japanese/Chinese with VITS #
This project utilizes ChatGPT API and whisper to provide English text to Japanese translation while also providing VITS text to speech. You speak, it speaks.

## How it works
English Voice input -> English Text (whisper) -> Japanese text translation (OpenAI API) -> Japanese Voice (VITS)  

## Install
setup.bat
paste the OpenAI API key into the config.py file

## How to run
Just run "run.bat" file
or run vits "python app.py --api" and the Language Link "english_to_japanese_vits.py" 



## Requirements
run setup.bat to auto clone all repos listed below except for voicemeeter

- whisper - https://github.com/openai/whisper
    - Allows for voice to text transcription 
    
    
- OpenAI API - https://openai.com/ 
    - Allows you to turn text from whisper to Japanese or Chinese


- vits-models (VITS) - https://huggingface.co/spaces/sayashi/vits-models 
    - Allows for Japanese or Chinese text to turn to Speech through the use of the gradio API


- Voicemeeter - https://vb-audio.com/Voicemeeter/
    - Allows you to play audio generated from the translator app through your mic in games or elsewhere 
