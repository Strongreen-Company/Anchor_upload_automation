#!/bin/bash

echo "Criando ambiente virtual..."
python3 -m venv venv

echo "Ativando ambiente virtual..."
source venv/bin/activate
echo "Ambiente virtual ativado!"

echo "Instalando dependencias..."
pip install -r /home/flaco/workspace/downloads_youtube/requirements.txt

echo "Executando arquivo Python..."
python3 /home/flaco/workspace/downloads_youtube/t.py
