# Extrator de E-mails Únicos

Este script em Python foi desenvolvido para extrair e-mails únicos de arquivos de texto (.txt) e arquivos CSV presentes em um diretório específico. Ele utiliza expressões regulares para identificar e-mails nos arquivos de texto e CSV e salva os e-mails únicos em arquivos de saída separados.

## Funcionalidades

**1. Extração de E-mails:** O script percorre recursivamente um diretório especificado, procura por arquivos de texto (.txt) e arquivos CSV e extrai e-mails de cada arquivo.

**2. Remoção de Duplicatas:** Os e-mails extraídos são armazenados em conjuntos (sets) separados para arquivos de texto e CSV, garantindo que apenas e-mails únicos sejam mantidos.

**3. Interatividade com o Usuário:** O usuário é solicitado a fornecer o caminho do diretório onde os arquivos de texto e CSV estão localizados.

**4. Finalização Controlada:** Ao pressionar Ctrl+C durante a execução, o script perguntará se o usuário deseja finalizar o programa.

## Como Usar

**1. Requisitos:**

- Python 3.x instalado.

**2. Execução:**

- Execute o script no terminal ou prompt de comando.
- O script solicitará o caminho do diretório onde os arquivos de texto e CSV estão localizados.
- Os e-mails únicos serão extraídos e salvos em arquivos chamados `emails_extraidos_txt.txt` (para arquivos de texto) e `emails_extraidos_csv.txt` (para arquivos CSV).

**3. Exemplo:**

    ```
    $ python extrator_emails.py
    Insira o caminho das pastas: C:\caminho\do\seu\diretorio
    E-mails únicos extraídos e salvos em `emails_extraidos_txt.txt`.
    E-mails únicos extraídos e salvos em `emails_extraidos_csv.txt`.
    ```

**4. Finalização Controlada:**

- Ao pressionar Ctrl+C, o script perguntará se deseja realmente finalizar o programa.

**Notas Importantes**

- Certifique-se de que o diretório fornecido contenha apenas arquivos de texto (.txt) e arquivos CSV.
- Os e-mails extraídos são salvos em arquivos separados para arquivos de texto e CSV no mesmo diretório do script.

Este script é uma ferramenta útil para organizar e identificar e-mails únicos em conjuntos de arquivos de texto e CSV. Certifique-se de respeitar a privacidade e conformidade ao usar este script em dados sensíveis.
