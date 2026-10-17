# BookShelf — Gerenciador de Leituras

O BookShelf é uma aplicação de linha de comando (CLI) em Python para organizar livros, acompanhar o progresso de leitura e registrar avaliações.

## Funcionalidades

- Cadastrar livros com título, autor, total de páginas e status.
- Visualizar a estante virtual e o percentual de leitura.
- Atualizar a quantidade de páginas lidas.
- Alterar automaticamente o status para `Lido` quando todas as páginas forem concluídas.
- Avaliar livros concluídos com notas de 1 a 5 estrelas.
- Editar título e autor.
- Excluir livros cadastrados.
- Validar campos obrigatórios, números inteiros, páginas e status.

## Tecnologias

- Python 3
- Git
- GitHub

## Estrutura

```text
bookshelf-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Como executar

1. Instale o Python 3.
2. Abra o terminal na pasta `bookshelf-projeto`.
3. Execute:

```bash
py src/main.py
```

Se `py` não funcionar, tente `python src/main.py`.

## Regras de negócio

- Título e autor são obrigatórios.
- O total de páginas deve ser um inteiro maior que zero.
- As páginas lidas devem ficar entre zero e o total de páginas.
- O status aceita `Quero Ler`, `Lendo` ou `Lido`.
- Ao completar 100% da leitura, o status muda para `Lido`.
- A nota deve ser um inteiro entre 1 e 5 e é solicitada para livros concluídos.

## Limitação da versão

Os dados são mantidos em memória durante a execução e não são gravados em arquivo ou banco de dados. Ao fechar o programa, a estante volta a ficar vazia.
