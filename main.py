from avl_operations import insert, search, inorder_traversal

def menu():
    root = None  # Inicializa a árvore AVL

    while True:
        print("\n1. Adicionar item")
        print("2. Buscar item")
        print("3. Mostrar estoque ordenado")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            id = int(input("ID: "))
            name = input("Nome: ")
            quantity = int(input("Quantidade: "))
            price = float(input("Preço: "))
            root = insert(root, id, name, quantity, price)
            print(f"Produto {name} inserido com sucesso!")
        elif choice == "2":
            id = int(input("ID do item a buscar: "))
            result = search(root, id)
            if result:
                print(f"Produto encontrado: ID={result['id']}, Nome={result['name']}, "
                      f"Quantidade={result['quantity']}, Preço={result['price']:.2f}")
            else:
                print(f"Produto com ID={id} não encontrado.")
        elif choice == "3":
            print("\nEstoque ordenado por ID:")
            products = inorder_traversal(root)  # Obtém os produtos ordenados
            if products:
                for product in products:
                    print(f"ID: {product['id']}, Nome: {product['name']}, "
                          f"Quantidade: {product['quantity']}, Preço: {product['price']:.2f}")
            else:
                print("O estoque está vazio.")
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
