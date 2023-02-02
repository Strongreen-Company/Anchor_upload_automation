#!/bin/bash
#shellcheck source=/dev/null

echo "Criando ambiente virtual..."
python3 -m venv venv

echo "Criando pasta para armazenamento de logs em /log/anchor"

FOLDER_NAME="log/anchor"

if [ ! -d "$FOLDER_NAME" ]; then
    sudo mkdir "$FOLDER_NAME"
    sudo chmod +755 "${FOLDER_NAME}"
    echo "Pasta criada com sucesso em ${FOLDER_NAME} e permissões definidas."
else
    echo "Pasta já existente em ${FOLDER_NAME}."
fi

echo "Ativando ambiente virtual..."
source venv/bin/activate
echo "Ambiente virtual ativado com sucesso!"

echo "Instalando dependências listadas no arquivo requirements.txt..."
pip install -r "${PWD}"/requirements.txt

echo "Executando arquivo Python verifyLastVideoInYoutube.py..."
python3 "${PWD}"/verifyLastVideoInYoutube.py
echo "Execução do script concluída."
