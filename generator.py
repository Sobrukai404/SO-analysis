import os
import random
import string
import time
import psutil

def gerar_palavra(tamanho):
    return ''.join(random.choices(string.ascii_lowercase, k=tamanho))

def gerar_arquivos_palavras_unicas(quantidade):
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / (1024 * 1024)  # MB
    cpu_start = psutil.cpu_percent(interval=None)
    start_time = time.time()

    # Cria pasta se não existir
    pasta = 'strings'
    os.makedirs(pasta, exist_ok=True)

    palavras_unicas = set()

    tentativas = 0
    while len(palavras_unicas) < quantidade:
        tamanho = random.randint(2, 15)
        palavra = gerar_palavra(tamanho)
        palavras_unicas.add(palavra)
        tentativas += 1

    for palavra in palavras_unicas:
        nome_arquivo = os.path.join(pasta, f"{palavra}.txt")
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(palavra)

    end_time = time.time()
    mem_after = process.memory_info().rss / (1024 * 1024)
    cpu_end = psutil.cpu_percent(interval=1)

    print("\n--- Estatísticas ---")
    print(f"{quantidade} palavras únicas geradas em {tentativas} tentativas.")
    print(f"{quantidade} arquivos salvos na pasta '{pasta}'.")
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
    print(f"Uso de memória: {mem_after - mem_before:.2f} MB")
    print(f"Uso de CPU (final): {cpu_end}%")

# Exemplo de uso
if __name__ == "__main__":
    gerar_arquivos_palavras_unicas(quantidade=10000)

