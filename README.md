# GS_IoT


## **Descrição do Projeto**

O **GS_IoT** é um projeto baseado em IoT que utiliza um ESP32 para coletar dados simulados de consumo de energia e temperatura. Esses dados são enviados via protocolo MQTT para um broker e são monitorados em tempo real em um dashboard Node-RED. Este projeto demonstra uma aplicação prática de sensores conectados e a comunicação eficiente de dados em sistemas IoT.

---

## **Componentes Principais**

1. **Microcontrolador ESP32**
   - Realiza a leitura de sensores, processa os dados e publica no broker MQTT.
   - Utiliza uma conexão Wi-Fi para enviar os dados.

2. **Sensores**
   - **DHT22**: Mede a temperatura ambiente. Os dados são ajustados para simular variações.
   - **LDR**: Um sensor de luz que é usado para simular o consumo energético.

3. **Protocolo MQTT**
   - **Broker MQTT**: HiveMQ (broker público utilizado neste projeto).
   - **Tópicos**:
     - `casa/energia/consumo`: Para dados de consumo energético.
     - `casa/energia/temperatura`: Para dados de temperatura.

4. **Dashboard Node-RED**
   - Exibe os dados recebidos do broker MQTT em tempo real, com gráficos e widgets customizáveis.
    ![image](https://github.com/user-attachments/assets/d4f12a58-d29a-4bc6-9330-afab7a3a0a5e)


---

## **Funcionamento do Sistema**

1. **Conexão Wi-Fi**
   - O ESP32 conecta à rede Wi-Fi configurada.
   - O sistema verifica constantemente a conexão e realiza reconexões automáticas em caso de falha.

2. **Leitura de Dados**
   - **DHT22**: Mede a temperatura, que é ajustada com um valor aleatório (5 a 10 °C).
   - **LDR**: Calcula um valor proporcional para simular o consumo energético (escala de 0 a 100W).

3. **Publicação MQTT**
   - Os dados são enviados para os tópicos configurados:
     - `casa/energia/consumo` (watts simulados).
     - `casa/energia/temperatura` (temperatura ajustada em °C).

4. **Monitoramento**
   - No Node-RED, os dados publicados são consumidos e exibidos em tempo real, com atualizações a cada 5 segundos.

---

## **Fluxo de Execução**

1. **Inicialização**
   - Conexão ao Wi-Fi.
   - Conexão ao broker MQTT.

2. **Loop Principal**
   - Verifica conectividade Wi-Fi e MQTT.
   - Lê os sensores e simula os valores.
   - Publica os dados no broker MQTT.
   - Intervalo de 5 segundos entre ciclos.

3. **Exemplo de Mensagens Publicadas**
   - **Consumo**: `23.5` (watts).
   - **Temperatura**: `30.7` (°C).

---

## **Tecnologias Utilizadas**

- **Hardware**
  - ESP32.
  - Sensor DHT22.
  - Sensor LDR.

- **Software**
  - MicroPython para programação do ESP32.
  - HiveMQ como broker MQTT.
  - Node-RED para monitoramento em tempo real.

- **Protocolo**
  - MQTT para comunicação leve e eficiente.

---

## **How to: Como Replicar e Testar Este Projeto**

### **Requisitos**
1. Conta no [Wokwi](https://wokwi.com/) ou extensão do Wokwi instalada no Visual Studio Code.
2. Software de monitoramento MQTT (ex.: [MQTT Explorer](https://mqtt-explorer.com/)).
3. Node-RED instalado e configurado (opcional, para visualizar os dados enviados pelo MQTT).

---

### **Passo a Passo: Testando no Wokwi**

1. **Configuração do Projeto**
   - Acesse o site do [Wokwi](https://wokwi.com/) e clique em **New Project**.
   - Escolha o **ESP32** como dispositivo principal.
   - Copie e cole o código-fonte do projeto na aba de código (`main.py`).

2. **Adicionar Sensores**
   - No simulador Wokwi:
     - Adicione o sensor **DHT22** e conecte-o ao pino GPIO 15.
     - Adicione o sensor **LDR** e conecte-o ao pino GPIO 34.

3. **Configurar o Broker MQTT**
   - Use o broker público **HiveMQ** ou configure um privado.
   - Certifique-se de que as configurações no código correspondem ao broker que você utilizará.

4. **Iniciar o Simulador**
   - Clique em **Start Simulation** no Wokwi.
   - Verifique no terminal do simulador se o ESP32 está conectado ao Wi-Fi e publicando dados no broker MQTT.

---

### **Passo a Passo: Testando no Visual Studio Code**

1. **Instalar Extensão do Wokwi**
   - No Visual Studio Code, procure e instale a extensão **Wokwi for VS Code**.

2. **Configurar o Projeto**
   - Abra o repositório do projeto no Visual Studio Code.
   - Configure o arquivo `wokwi.toml` com as definições dos sensores utilizados:
     ```toml
     [esp32]
     board = "esp32dev"

     [components.dht22]
     pin = 15

     [components.ldr]
     pin = 34
     ```

3. **Executar a Simulação**
   - Utilize o comando da extensão para iniciar a simulação.
   - Certifique-se de que os dados estão sendo enviados corretamente para o broker MQTT.

---

### **Visualização no Node-RED**
1. Configure um nó **MQTT In** para os tópicos `casa/energia/consumo` e `casa/energia/temperatura`.
2. Adicione nós gráficos (ex.: **chart**) para exibir os dados em tempo real.
3. Conecte os nós e inicie o fluxo para monitorar as leituras.

---
# Integrantes
- Luiz Felipe RM552475
- Rennan Ferreira RM99364
- Jaisy Cibele RM552269
- Tomaz Pecoraro RM98499
- Gabriel Amâncio RM97936

