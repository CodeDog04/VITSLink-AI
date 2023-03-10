@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Cloning whisper repository...
git clone https://github.com/openai/whisper.git
cd whisper
pip install -e .

echo Cloning VITS models repository...
git clone https://huggingface.co/spaces/sayashi/vits-models.git
cd ..

echo Setup complete.
pause
