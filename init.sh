#!/bin/bash
#shellcheck source=/dev/null

echo "Criando ambiente virtual..."
python3 -m venv venv

echo "criando pasta para logs caso não exista em /var/log/anchor"
echo "Ativando ambiente virtual..."
source venv/bin/activate
echo "Ambiente virtual ativado!"

echo "Instalando dependencias..."
pip install -r "${PWD}"/requirements.txt

echo "Executando arquivo Python..."
python3 "${PWD}"/verifyLastVideoInYoutube.py
