@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Cloning whisper repository...
pip install git+https://github.com/openai/whisper.git 
cd whisper
pip install -r requirements.txt
python setup.py


echo Cloning VITS models repository...
git clone https://huggingface.co/spaces/sayashi/vits-models.git
cd vits-models
pip install -r requirements.txt


echo Setup complete.
pause
