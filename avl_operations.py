from utils import create_node, get_height, calculate_balance, rotate_left, rotate_right

# Função para inserir um novo produto na Árvore AVL
def insert(node, id, name, quantity, price):
    if node is None:  # Se a árvore estiver vazia, cria um novo nó
        return create_node(id, name, quantity, price)

    if id < node["id"]:  # ID menor vai para a subárvore esquerda
        node["left"] = insert(node["left"], id, name, quantity, price)
    elif id > node["id"]:  # ID maior vai para a subárvore direita
        node["right"] = insert(node["right"], id, name, quantity, price)
    else:
        return node  # IDs duplicados não são inseridos

    # Atualiza a altura e balanceia a árvore após a inserção
    node["height"] = 1 + max(get_height(node["left"]), get_height(node["right"]))
    balance_factor = calculate_balance(node)

    # Corrige desbalanceamento

    #Esquerda-esquerda
    if balance_factor > 1 and id < node["left"]["id"]:
        return rotate_right(node)
    #Direita-direita
    if balance_factor < -1 and id > node["right"]["id"]:
        return rotate_left(node)
    #Esquerda-direita
    if balance_factor > 1 and id > node["left"]["id"]:
        node["left"] = rotate_left(node["left"])
        return rotate_right(node)
    #Direita-esquerda
    if balance_factor < -1 and id < node["right"]["id"]:
        node["right"] = rotate_right(node["right"])
        return rotate_left(node)

    return node

# Função para buscar um produto pelo ID
def search(node, id):
    if node is None:  # Caso base: produto não encontrado
        return None

    if id == node["id"]:  # ID encontrado
        return node
    elif id < node["id"]:  # Busca na subárvore esquerda
        return search(node["left"], id)
    else:  # Busca na subárvore direita
        return search(node["right"], id)

# Função para exibir os produtos em ordem crescente de ID
def inorder_traversal(node):
    if node is None:  # Caso base: árvore vazia
        return []

    # Combina os resultados da subárvore esquerda, nó atual e subárvore direita
    return inorder_traversal(node["left"]) + [node] + inorder_traversal(node["right"])
