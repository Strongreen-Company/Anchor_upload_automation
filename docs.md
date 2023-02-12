# tecnologia utilizadas

-   python
-   selenium
-   aws SES
-   VPS OCi
-   Crontab

# bibliotecas

-   demoji
-   boto3
-   pythube
-   selenium
-   black & flake8
-   requsets

# resumo da aplicação

esse repositorio é de um sistema para monitorar o canal do YouTube em busca de novos episódios da live "Falando com Maker". Quando um vídeo é detectado, ele é imediatamente baixado, convertido em formato de áudio e publicado na plataforma de podcasts Anchor através duma automação.

Utilizei a API do YouTube para monitorar, o Pytube para baixar vídeos, o Selenium para automatizar a publicação de episódios e o demoji para remover emojis não permitidos pelo drive do selenium. Além disso, escolhi o AWS SES para enviar notificações de e-mail e a VPS da Oracle Cloud IaaS como plataforma de hospedagem.

# nescessário para rodar o projeto

é nescessario ter o python na versão 3.9.1 e o pip instalado.

é nesscessario uma conta na aws para enviar emails e uma conta na oracle cloud para hospedar a aplicação.

o usuário deve criar um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:

o usuario deverá ser administrador do canal do youtube e ter uma conta na plataforma de podcast anchor.

o usuario devera rodar o comando `pip install -r requirements.txt` para instalar as dependencias do projeto.

o usuario deverar esta no grupo root para poder rodar o projeto.

o usuario devera rodar o comando `sudo ./init.sh` para rodar o projeto.

devera instalar o chrome no servidor.

deverá ter o crontab instalado e configurado.

`EMAIL= email da plataforma de podcast (anchor)`
`PASSWORD=senha da plataforma de podcast (anchor)`
`AUTOMACAO_EMAIL=email da automação que irá enviar os emails confirmando a publicação do episódio`
`MAIN_EMAIL=email principal do usuário que irá receber os emails`
`API_KEY_YOUTUBE=api key do youtube `
`CHANNEL_ID= id do canal do youtube`
`AWS_SECRET_ACCESS_KEY=secret key da aws `
`AWS_ACCESS_KEY_ID=access key da aws`
