import json
import time

sair = True

# Carregar dados dos personagens
with open('personagens.json', 'r') as f:
    personagens = json.load(f)

class Node:
    def __init__(self, pergunta=None, personagem=None):
        self.pergunta = pergunta
        self.personagem = personagem
        self.sim = None
        self.nao = None

def criar_arvore():
    raiz = Node("O personagem é do universo Marvel?")
    raiz.sim = Node("O personagem é animado?")
    raiz.nao = Node("O personagem é do universo DC?")

    raiz.sim.sim = Node(personagem="Hulk")
    raiz.sim.nao = Node(personagem="Homem-Aranha")

    raiz.nao.sim = Node("O personagem é animado?")
    raiz.nao.nao = Node("O personagem é de outro universo?")

    raiz.nao.sim.sim = Node(personagem="Mulher Maravilha")
    raiz.nao.sim.nao = Node(personagem="Superman")

    raiz.nao.nao.sim = Node("O personagem tem superpoder?")
    raiz.nao.nao.nao = Node("O personagem é humano?")

    raiz.nao.nao.sim.sim = Node(personagem="Elsa")
    raiz.nao.nao.sim.nao = Node(personagem="Harry Potter")

    raiz.nao.nao.nao.sim = Node("O personagem é humano?")
    raiz.nao.nao.nao.nao = Node("O personagem é animado?")

    raiz.nao.nao.nao.sim.sim = Node(personagem="Sherlock Holmes")
    raiz.nao.nao.nao.sim.nao = Node(personagem="Gandalf")

    raiz.nao.nao.nao.nao.sim = Node(personagem="Katniss Everdeen")
    raiz.nao.nao.nao.nao.nao = Node(personagem="SpongeBob")

    # Adicionando novos personagens à árvore
    novo_no_1 = Node("O personagem é do universo Pokémon?")
    novo_no_1.sim = Node(personagem="Pikachu")
    novo_no_1.nao = Node(personagem="Optimus Prime")

    novo_no_2 = Node("O personagem é do universo Tomb Raider?")
    novo_no_2.sim = Node(personagem="Lara Croft")
    novo_no_2.nao = Node(personagem="Indiana Jones")

    raiz.nao.nao.nao.sim.nao.sim = novo_no_1
    raiz.nao.nao.nao.sim.nao.nao = novo_no_2

    novo_no_3 = Node("O personagem é do universo Disney?")
    novo_no_3.sim = Node(personagem="Mickey Mouse")
    novo_no_3.nao = Node(personagem="Fiona")

    raiz.nao.nao.nao.nao.nao.sim = novo_no_3
    raiz.nao.nao.nao.nao.nao.nao = Node(personagem="Groot")

    return raiz

def jogar(node):
    global sair
    if node.personagem:
        resposta = input(f"Seu personagem é {node.personagem}? (sim/nao): ")
        if resposta.lower() == 'sim':
            print("Acertei!")
            sair = False
            print("Saindo ", end="")
            for _ in range(3):
                time.sleep(1.5)
                print(". ", end="", flush=True)
            print()
        else:
            print("Errei. Vamos tentar novamente!")
    else:
        resposta = input(f"{node.pergunta} (sim/nao): ")
        if resposta.lower() == 'sim' and node.sim:
            jogar(node.sim)
        elif node.nao:
            jogar(node.nao)
        else:
            print("Não consegui adivinhar. Vamos tentar novamente!")

# Iniciar jogo
arvore = criar_arvore()
while sair:
    jogar(arvore)