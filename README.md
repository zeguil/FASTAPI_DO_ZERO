# Gerenciador de Tarefas

## Descrição do Projeto

O projeto central deste curso é a construção de um gerenciador de tarefas (uma lista de tarefas), começando do zero. Este projeto inclui a implementação da autenticação do usuário e das operações CRUD completas.

## Ferramentas Utilizadas

Para a construção do projeto, foram utilizadas as versões mais recentes das ferramentas disponíveis em 2024:

- **FastAPI**: versão 0.100
- **Pydantic**: versão 2.0
- **SQLAlchemy ORM**: versão 2.0
- **Python**: versão 3.11
- **Alembic**: para gerenciamento de migrações

## Funcionalidades do Projeto

- **Autenticação de Usuário**: Implementação completa de autenticação para garantir a segurança e integridade dos dados.
- **Operações CRUD**: Criação, leitura, atualização e exclusão de tarefas.
- **Gerenciamento de Migrações**: Utilização do Alembic para gerenciar mudanças no banco de dados de forma eficiente.

## Testes

A construção do projeto incluirá a prática de testes, utilizando o pytest. Essa abordagem planeja garantir que a API desenvolvida seja não apenas funcional, mas também robusta e confiável.

## Como Baixar e Executar o Projeto

### Pré-requisitos

Certifique-se de ter o **Poetry** instalado. Você pode instalá-lo seguindo as instruções na [documentação oficial do Poetry](https://python-poetry.org/docs/#installation).

### Passos para Baixar e Executar

1. **Clone o Repositório**

   ```sh
   https://github.com/zeguil/FASTAPI_DO_ZERO.git

   cd FASTAPI_DO_ZERO
   ```

2. **Instale as Dependências**

   No diretório do projeto, execute:

   ```sh
   poetry install
   ```
3. **Ative o Ambiente Virtual do Poetry**

   ```
   poetry shell
   ```

4. **Execute o Projeto**
   ```
   fastapi dev fast_zero/app.py
   ```




