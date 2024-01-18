window.onload = function loadMonitoringData() {
    fetch('../shared_data/monitoring_data.json')
        .then(response => response.json())
        .then(data => {
            // Manipule os dados como desejar
            displayData(data);
        })
        .catch(error => console.error('Erro ao carregar dados:', error));
}

// Função para exibir os dados na página
function displayData(data) {
    // Construa a representação HTML dos dados, por exemplo:
    let htmlContent = '<h2>Dados de Monitoramento:</h2>';
    
    for (const containerId in data) {
        const containerData = data[containerId];
        htmlContent += `<div>`;
        htmlContent += `<p><strong>Container ID:</strong> ${containerId}</p>`;
        htmlContent += `<p><strong>CPU Percent:</strong> ${containerData.cpu_percent}%</p>`;
        htmlContent += `<p><strong>Memory Percent:</strong> ${containerData.mem_percent}%</p>`;
        htmlContent += `<p><strong>Timestamp:</strong> ${new Date(containerData.timestamp * 1000)}</p>`;
        htmlContent += `<p><strong>Host IP:</strong> ${containerData.host_ip}</p>`;
        htmlContent += `<p><strong>Ping Latency:</strong> ${containerData.ping_latency} ms</p>`;
        htmlContent += `</div>`;
    }

    document.getElementById('monitoring-data').innerHTML = htmlContent;
}
