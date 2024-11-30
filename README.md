<h1 align="center"> Gerenciador de Países, Cidades e Rios 🌍 </h1>
Este é um projeto de aplicação web desenvolvido com Flask e MongoDB para gerenciar coleções de países, cidades e rios. A aplicação permite cadastrar, listar, filtrar, atualizar, detalhar e excluir itens dessas coleções, proporcionando uma interface simples e intuitiva.

## Descrição do Projeto
Funcionalidades 🛠️
Países
Adicionar país: Nome, continente, população, PIB e expectativa de vida.

Listar países: Filtros por nome, continente, população, PIB e expectativa de vida.

Detalhar país: Exibe informações detalhadas de um país específico.

Atualizar país: Permite editar as informações de um país.

Deletar país: Remove um país do banco de dados.
![Captura de tela 2024-11-30 093840](https://github.com/user-attachments/assets/896f1ec0-7626-4786-afd3-93390f3772c6)


## Cidades
Adicionar cidade: Nome, país, população e se é capital.

Listar cidades: Filtros por nome, país, população e status de capital.

Detalhar cidade: Exibe informações detalhadas de uma cidade específica.

Atualizar cidade: Permite editar as informações de uma cidade.

Deletar cidade: Remove uma cidade do banco de dados.
![Captura de tela 2024-11-30 094103](https://github.com/user-attachments/assets/57558fd2-b09c-4d3c-a352-2e129c6b825b)


## Rios
Adicionar rio: Nome, nascente, país e comprimento.

Listar rios: Filtros por nome, nascente, país e comprimento.

Detalhar rio: Exibe informações detalhadas de um rio específico.

Atualizar rio: Permite editar as informações de um rio.

Deletar rio: Remove um rio do banco de dados.

![Captura de tela 2024-11-30 094213](https://github.com/user-attachments/assets/d2cdbcc7-d766-48fb-b4b2-fbbdba0aa690)

## Tecnologias Utilizadas
 💻
Back-end: Flask

Banco de Dados: MongoDB

Driver MongoDB para Python: PyMongo

Template Engine: Jinja2 (integrada ao Flask)

HTML e CSS: Para interface do usuário.

## Configuração e Execução 🚀
Pré-requisitos
Python 3.8+: Certifique-se de ter o Python instalado.

MongoDB: Um servidor MongoDB rodando localmente na porta padrão (localhost:27017).

Passo a passo

Clone o repositório:

bash
Copiar código

git clone https://github.com/seu-usuario/seu-repositorio.git

cd seu-repositorio

Instale as dependências:

bash

Copiar código

pip install flask pymongo

Configure o MongoDB:

Certifique-se de que o banco de dados mundo está criado.
As coleções paises, cidades e rios serão criadas automaticamente na primeira inserção.
Inicie o servidor:

bash
Copiar código
python app.py
Acesse no navegador:

Copiar código
http://localhost:5000
