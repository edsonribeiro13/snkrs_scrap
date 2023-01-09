# Sneakers scrap
O objetivo desse projeto é realizar um simples scrap em um outlet qualquer, armazenar o nome, o preço e a menor data do preço de determinado tênis. O `.env.example` inicialmente está configurado para uma das páginas da Puma. O projeto utiliza como base o framework Flask e armazena os dados no banco relacional MySQL.

# Dependências
Para utilizar o projeto como está é necessário possuir o organizador de pacotes [poetry](https://python-poetry.org/docs/) instalado, também é recomendável utilizar o gestor de envs [pyenv](https://github.com/pyenv/pyenv), além de possuir o banco de dados [MySQL](https://www.mysql.com/downloads/).

# Utilização
Para rodar o projeto é necessário incialmente criar uma cópia do arquivo `.env.example` e renomear esta cópia para `.env`, na sequência (possuindo o poetry) utilizar os comandos `make install` e `make shell`, por fim dentro do shell do ambiente `make run`. Uma página será servida com os dados relacionados aos tênis
