import os
import time
import psutil
import json
import socket
import subprocess

def get_host_ip():
    try:
        # Obtém o IP do host usando a biblioteca de soquetes
        host_ip = socket.gethostbyname(socket.gethostname())
        return host_ip
    except socket.error as e:
        print(f"Erro ao obter o IP do host: {e}")
        return None

def get_ping_latency(host='google.com'):
    try:
        # Executa o comando de ping e captura a latência
        result = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            lines = result.stdout.splitlines()
            last_line = lines[-1].split()
            latency = float(last_line[4].replace('time=', ''))
            return latency
        else:
            print(f"Erro ao executar ping: {result.stderr}")
            return None
    except Exception as e:
        print(f"Erro ao obter a latência do ping: {e}")
        return None

def monitor_containers():
    host_ip = get_host_ip()
    ping_latency = get_ping_latency()

    containers = os.listdir('/sys/fs/cgroup/memory/docker/')
    data = {}

    for container in containers:
        container_id = container[:12]
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent

        timestamp = int(time.time())
        data[container_id] = {
            'cpu_percent': cpu_percent,
            'mem_percent': mem_percent,
            'timestamp': timestamp,
            'host_ip': host_ip,
            'ping_latency': ping_latency
        }

    with open('/shared_data/monitoring_data.json', 'w') as file:
        json.dump(data, file)

while True:
    monitor_containers()
    time.sleep(60)  # Atualiza a cada 60 segundos

