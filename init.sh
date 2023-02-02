#!/bin/bash
#shellcheck source=/dev/null

echo "Criando ambiente virtual..."
python3 -m venv venv

echo "criando pasta para logs caso não exista em /var/log/anchor"

FOLDER_NAME="/var/log/anchor"

if [ ! -d "$FOLDER_NAME" ]; then
    mkdir $FOLDER_NAME
    sudo chmod +777 /var/log/anchor
fi

echo "Ativando ambiente virtual..."
source venv/bin/activate
echo "Ambiente virtual ativado!"
sleep 5s

echo "Instalando dependencias..."
pip install -r "${PWD}"/requirements.txt

#echo "Executando arquivo Python..."
sudo python3 "${PWD}"/verifyLastVideoInYoutube.py
