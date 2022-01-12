import requests
from flask import Flask

app = Flask(__name__)

index = 1
total_numbers = []


# 1. Extract
# Método responsável por carregar os dados por endpoint da API
def load_api(page):
    response = requests.get(f"http://challenge.dienekes.com.br/api/numbers?page={page}")
    if response.status_code == 200:
        data = response.json()
        if len(data["numbers"]) != 0:
            global index
            for number in data["numbers"]:
                total_numbers.append(number)
            index += 1
            return True
        else:
            return False
    else:
        return True


# 2. Transform
# Método responsável por ordenar os números (crescente) de todos os endpoints armazenados na lista
def order_number():
    print("Ordenando os números")
    global total_numbers
    order_dictionary = {}

    # Faz um loop da esquerda para direita em cada item da linha
    for line in total_numbers:

        # Faz um loop da esquerda para direita em cada item da coluna
        for column in total_numbers:

            # Compara se o número do índice atual da linha é menor que o da coluna, caso seja
            # faz uma subistituição
            if total_numbers[total_numbers.index(line)] <= total_numbers[total_numbers.index(column)]:

                # Armazena o número da linha
                aux = total_numbers[total_numbers.index(line)]

                # Substitui o número do índice da linha pelo número do índice da coluna
                total_numbers[total_numbers.index(line)] = total_numbers[total_numbers.index(column)]

                # Substitui o número do índice da coluna pelo número do índice da linha
                total_numbers[total_numbers.index(column)] = aux

        order_dictionary["numbers"] = total_numbers
    return order_dictionary


# 3. Load
@app.route('/')
def get_all():
    print("Carregando resultado")
    global index
    while load_api(index):
        load_api(index)
    return order_number()


app.run()
