@echo off
echo Starting English to Japanese Text to Speech Translator
echo Starting VITS...
cd vits-models
start cmd /k python app.py --api

cd ..
start cmd /k python japanese_to_english.py
