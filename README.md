#WORK IN PROGRESSS

# OpenAI_English-to-Japanese-or-Chinese_VITS-tts #
This project utilizes ChatGPT API and whisper to provide English text to Japanese translation while also providing VITS text to speech. You speak, it speaks.

## Future Plan
- program which allows you to translate speech heard in Games or Media. 
- Implement tortoise-tts for English-to-English near real time voice changer
- different python programs for English to all langauges (require tortoise-tts model good enough to do this, otherwise you're forced to use Elevenlabs API) 

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
