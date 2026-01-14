📊 Controle de Infectados – Região Sudeste

Este projeto foi desenvolvido em Python com o objetivo de registrar, armazenar e consultar dados de pessoas infectadas na Região Sudeste do Brasil, separando os casos entre profissionais da saúde e população em geral.

O sistema é voltado para fins educacionais, aplicando conceitos básicos de programação e manipulação de arquivos.
<p></p>

---
🚀 Funcionalidades

📌 Cadastro de infectados por estado:

São Paulo

Rio de Janeiro

Espírito Santo

Minas Gerais

🏥 Separação entre profissionais da saúde e população geral

💾 Armazenamento dos dados em arquivo texto

📈 Consulta da situação atual com totais consolidados

❌ Encerramento seguro do programa
<p></p>

---
📄 Descrição dos Arquivos

app_contagio.py<p></p>
Arquivo principal. Controla o menu, a interação com o usuário e chama as funções de cadastro e consulta.
<p></p>
cabecalho_exercicio.py<p></p>
Contém funções responsáveis pela interface textual do sistema, como menus, cabeçalhos e validação de entrada de dados.
<p></p>
arquivo_app.py<p></p>
Responsável pela manipulação de arquivos, incluindo:
<p></p>
verificação da existência do arquivo

criação do arquivo

gravação de registros

leitura e consolidação dos dados

arquivo.txt
Arquivo onde os dados cadastrados são armazenados.
<p></p>

---
🧠 Como o Programa Funciona

- Ao iniciar, o sistema verifica se o arquivo de dados existe.

- Caso não exista, ele é criado automaticamente.

- O usuário escolhe uma opção no menu principal.

- Para cadastro, o sistema solicita os valores de infectados.

- Os dados são gravados no arquivo de texto.

- Na opção de consulta, o sistema lê o arquivo e apresenta:

Dados por estado, total de profissionais da saúde infectados e total da população geral infectada.
