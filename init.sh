#!/bin/bash

echo "Criando ambiente virtual..."
python3 -m venv env

echo "Ativando ambiente virtual..."
source env/bin/activate
echo "Ambiente virtual ativado!"

echo "Instalando dependencias..."
pip install -r /home/flaco/workspace/downloads_youtube/requirements.txt

echo "Executando arquivo Python..."
python3 /home/flaco/workspace/downloads_youtube/t.py
