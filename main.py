def ler_texto_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Erro: este campo é obrigatório.")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if minimo is not None and valor < minimo:
                print(f"Erro: informe um número maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Erro: informe um número menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def ler_status():
    status_validos = {
        "quero ler": "Quero Ler",
        "lendo": "Lendo",
        "lido": "Lido",
    }

    while True:
        status = input("Status (Quero Ler, Lendo ou Lido): ").strip().lower()
        if status in status_validos:
            return status_validos[status]
        print("Erro: escolha Quero Ler, Lendo ou Lido.")


def ler_nota():
    return ler_inteiro("Nota (1 a 5 estrelas): ", 1, 5)


def calcular_progresso(livro):
    return (livro["paginas_lidas"] / livro["total_paginas"]) * 100


def cadastrar_livro(estante):
    print("\n=== Cadastro de livro ===")
    titulo = ler_texto_obrigatorio("Título: ")
    autor = ler_texto_obrigatorio("Autor: ")
    total_paginas = ler_inteiro("Total de páginas: ", 1)
    status = ler_status()

    if status == "Quero Ler":
        paginas_lidas = 0
        nota = None
    elif status == "Lendo":
        paginas_lidas = ler_inteiro(
            f"Páginas lidas (0 a {total_paginas}): ", 0, total_paginas
        )
        nota = None
        if paginas_lidas == total_paginas:
            status = "Lido"
            nota = ler_nota()
    else:
        paginas_lidas = total_paginas
        nota = ler_nota()

    livro = {
        "titulo": titulo,
        "autor": autor,
        "total_paginas": total_paginas,
        "paginas_lidas": paginas_lidas,
        "status": status,
        "nota": nota,
    }

    estante.append(livro)
    print(f'Livro "{titulo}" cadastrado com sucesso!')


def listar_livros(estante):
    print("\n=== Minha estante BookShelf ===")
    if not estante:
        print("Sua estante está vazia no momento.")
        return

    for indice, livro in enumerate(estante, start=1):
        progresso = calcular_progresso(livro)
        nota = f'{livro["nota"]}/5 estrelas' if livro["nota"] is not None else "Não avaliado"
        print(f"\nLivro {indice}")
        print(f'Título: {livro["titulo"]}')
        print(f'Autor: {livro["autor"]}')
        print(f'Status: {livro["status"]}')
        print(f'Páginas: {livro["paginas_lidas"]}/{livro["total_paginas"]}')
        print(f"Progresso: {progresso:.1f}%")
        print(f"Nota: {nota}")


def selecionar_livro(estante):
    if not estante:
        print("Não há livros cadastrados.")
        return None

    listar_livros(estante)
    indice = ler_inteiro("Informe o número do livro: ", 1, len(estante))
    return estante[indice - 1]


def atualizar_progresso(estante):
    print("\n=== Atualizar progresso de leitura ===")
    livro = selecionar_livro(estante)
    if livro is None:
        return

    paginas = ler_inteiro(
        f'Nova quantidade de páginas lidas (0 a {livro["total_paginas"]}): ',
        0,
        livro["total_paginas"],
    )
    livro["paginas_lidas"] = paginas

    if paginas == livro["total_paginas"]:
        livro["status"] = "Lido"
        if livro["nota"] is None:
            livro["nota"] = ler_nota()
    elif paginas > 0:
        livro["status"] = "Lendo"
    else:
        livro["status"] = "Quero Ler"

    print("Progresso atualizado com sucesso!")


def avaliar_livro(estante):
    print("\n=== Avaliar livro concluído ===")
    livro = selecionar_livro(estante)
    if livro is None:
        return

    if livro["status"] != "Lido":
        print("Só é possível avaliar livros com status Lido.")
        return

    livro["nota"] = ler_nota()
    print("Avaliação registrada com sucesso!")


def editar_livro(estante):
    print("\n=== Editar livro ===")
    livro = selecionar_livro(estante)
    if livro is None:
        return

    print("Deixe o campo vazio para manter o valor atual.")
    titulo = input(f'Título [{livro["titulo"]}]: ').strip()
    autor = input(f'Autor [{livro["autor"]}]: ').strip()

    if titulo:
        livro["titulo"] = titulo
    if autor:
        livro["autor"] = autor

    print("Dados do livro atualizados com sucesso!")


def excluir_livro(estante):
    print("\n=== Excluir livro ===")
    livro = selecionar_livro(estante)
    if livro is None:
        return

    confirmacao = input(
        f'Deseja excluir "{livro["titulo"]}"? (s/n): '
    ).strip().lower()

    if confirmacao == "s":
        estante.remove(livro)
        print("Livro excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


def exibir_menu():
    print("\n========== BOOKSHELF ==========")
    print("1. Cadastrar livro")
    print("2. Visualizar estante")
    print("3. Atualizar progresso de leitura")
    print("4. Avaliar livro concluído")
    print("5. Editar livro")
    print("6. Excluir livro")
    print("7. Sair")


def main():
    estante = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_livro(estante)
        elif opcao == "2":
            listar_livros(estante)
        elif opcao == "3":
            atualizar_progresso(estante)
        elif opcao == "4":
            avaliar_livro(estante)
        elif opcao == "5":
            editar_livro(estante)
        elif opcao == "6":
            excluir_livro(estante)
        elif opcao == "7":
            print("Obrigado por usar o BookShelf. Até logo!")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 7.")


if __name__ == "__main__":
    main()
