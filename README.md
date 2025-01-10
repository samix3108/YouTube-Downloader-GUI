Este código é uma aplicação GUI em Python para download de vídeos e áudios do YouTube utilizando as bibliotecas `tkinter` para a interface gráfica e `yt_dlp` para realizar as operações de download. Ele é intuitivo e fácil de usar, com funcionalidades para verificar links, selecionar qualidade, e escolher um diretório para salvar os arquivos.

---

### **Descrição do Código**

#### **Objetivo**
O programa permite que os usuários façam download de vídeos ou áudios do YouTube diretamente para seus computadores, com opções de qualidade e escolha de diretório de salvamento.

---

#### **Componentes Principais**

1. **Interface Gráfica (`tkinter`)**
   - **Campos de Entrada:**
     - Campo para o link do vídeo do YouTube.
     - Campo para o diretório onde o arquivo será salvo.
   - **Botões:**
     - Verificar Link: Confirma a validade do link e obtém informações do vídeo.
     - Escolher Diretório: Abre um seletor para escolher onde salvar o arquivo.
     - Baixar: Inicia o download com as configurações selecionadas.
   - **Opções:**
     - Escolha entre download de áudio ou vídeo.
     - Defina a qualidade do arquivo (Alta ou Baixa).

2. **Função de Verificação do Link**
   - Usa o `yt_dlp` para verificar se o link é válido e extrair o título do vídeo.
   - Habilita as opções de download após a validação.

3. **Função de Download**
   - Configura as opções de download, como formato e qualidade, com base nas seleções do usuário.
   - Baixa o arquivo usando `yt_dlp` e salva no diretório especificado.

4. **Configuração das Opções de Download**
   - **Áudio:** Converte o áudio para MP3 com qualidade de 192 kbps.
   - **Vídeo:** Escolhe entre alta ou baixa qualidade com base na seleção.

5. **Mensagens de Feedback**
   - Utiliza `tkinter.messagebox` para exibir mensagens de sucesso, aviso ou erro.

6. **Atualização Automática dos Botões**
   - Os botões são habilitados ou desabilitados com base nas ações do usuário, garantindo uma experiência intuitiva.

---

#### **Requisitos**
- Python 3.x
- Bibliotecas: `tkinter`, `yt_dlp`

#### **Como Usar**
1. Insira o link do vídeo do YouTube no campo "Link do vídeo".
2. Clique em "Verificar Link" para validar o vídeo.
3. Escolha o diretório de salvamento clicando em "Escolher Diretório".
4. Selecione se deseja baixar Áudio ou Vídeo e defina a qualidade.
5. Clique em "Baixar" para iniciar o download.

---

#### **Licença**
Este código está licenciado sob a **Licença MIT**, permitindo uso, modificação e redistribuição livre, desde que seja feita a atribuição ao autor original.
