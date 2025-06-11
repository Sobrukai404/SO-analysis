import os
import time
import psutil
import threading

# Variáveis globais para monitoramento
peak_memory = 0
peak_cpu = 0
cpu_readings = []
monitoring = True

def monitor_usage(process):
    global peak_memory, peak_cpu, cpu_readings, monitoring
    while monitoring:
        mem = process.memory_info().rss / (1024 * 1024)  # Em MB
        cpu = process.cpu_percent(interval=0.1)  # Percentual de CPU no intervalo 0.1s
        peak_memory = max(peak_memory, mem)
        peak_cpu = max(peak_cpu, cpu)
        cpu_readings.append(cpu)
        time.sleep(0.1)

def quick_sort(words):
    if len(words) <= 1:
        return words

    pivot = words[0]
    less = []
    equal = []
    greater = []

    for word in words:
        if len(word) < len(pivot):
            less.append(word)
        elif len(word) > len(pivot):
            greater.append(word)
        else:
            if word < pivot:
                less.append(word)
            elif word > pivot:
                greater.append(word)
            else:
                equal.append(word)

    return quick_sort(less) + equal + quick_sort(greater)

def main():
    global monitoring
    pasta = 'strings'
    palavras = []

    # Inicia monitoramento
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / (1024 * 1024)
    start_time = time.time()

    # Inicia thread de monitoramento
    monitor_thread = threading.Thread(target=monitor_usage, args=(process,))
    monitor_thread.start()

    # Lê os arquivos
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.txt'):
            caminho = os.path.join(pasta, nome_arquivo)
            with open(caminho, 'r', encoding='utf-8') as f:
                palavra = f.read().strip()
                if palavra:
                    palavras.append(palavra)

    # Ordena
    palavras_ordenadas = quick_sort(palavras)

    # Termina monitoramento
    end_time = time.time()
    mem_after = process.memory_info().rss / (1024 * 1024)
    monitoring = False
    monitor_thread.join()

    # Calcula média do uso de CPU
    cpu_avg = sum(cpu_readings) / len(cpu_readings) if cpu_readings else 0

    # Escreve resultados
    with open('results.txt', 'w', encoding='utf-8') as f:
        for palavra in palavras_ordenadas:
            f.write(palavra + '\n')

        f.write("\n--- Estatísticas ---\n")
        f.write(f"Tempo de execução: {end_time - start_time:.4f} segundos\n")
        f.write(f"Uso de memória: {mem_after - mem_before:.2f} MB\n")
        f.write(f"Pico de memória RAM: {peak_memory:.2f} MB\n")
        f.write(f"Pico de uso de CPU: {peak_cpu:.2f}%\n")
        f.write(f"Média de uso de CPU: {cpu_avg:.2f}%\n")

    print("Arquivo 'results.txt' gerado com sucesso.")

if __name__ == "__main__":
    main()

