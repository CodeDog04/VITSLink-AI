# OpenAI English to Japanese/Chinese VITS tts #
This project utilizes ChatGPT API and whisper to provide English text to Japanese translation while also providing VITS text to speech. You speak, it speaks.

## Future Plan
- program which runs in seperate cli which allows you to translate speech heard from your systems audio 
- Implement tortoise-tts for English-to-English near real time voice changer
- different python programs for English to all langauges (require tortoise-tts model good enough to do this, otherwise you're forced to use Elevenlabs API, will make new repo for this) 

## How it works
English Input -> English Text (whisper) -> Japanese Text translation (OpenAI API) -> Japanese Voice (VITS)  

## Install
setup.bat
paste the OpenAI API key into the config.py file

## How to run
Just run "run_en-to-ja.bat" file
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
