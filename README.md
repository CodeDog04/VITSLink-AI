# OpenAI_English-to-Japanese-or-Chinese_VITS-tts #
This project utilizes ChatGPT API and whisper to provide English text to Japanese translation while also providing VITS tts

## How it works
English Input -> English Text (whisper) -> Japanese Text translation (OpenAI API) -> Japanese Voice (VITS)  

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


## Documentation

## Bug Reporting
