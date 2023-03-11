@echo off

echo Select a translation option:
echo 1. English to Japanese
echo 2. English to Chinese

set /p option="Enter a selection number: "

if "%option%"=="1" (
  echo Starting English to Japanese Text to Speech Translator
  echo Starting VITS...
  cd vits-models
  start cmd /k python app.py --api
  cd ..
  start cmd /k python english_to_japanese.py
) else if "%option%"=="2" (
  echo Starting English to Chinese Text to Speech Translator
  echo Starting VITS...
  cd vits-models
  start cmd /k python app.py --api
  cd ..
  start cmd /k python english_to_chinese.py
) else (
  echo Invalid selection. Please try again.
)
