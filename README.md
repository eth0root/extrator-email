#  **Extrator de E-mails Únicos**
Este script em Python foi desenvolvido para extrair e-mails únicos de arquivos de texto (.txt) presentes em um diretório específico. Ele utiliza expressões regulares para identificar e-mails nos arquivos de texto e salva os e-mails únicos em um arquivo de saída.

###  Funcionalidades

****1. Extração de E-mails:****  O script percorre recursivamente um diretório especificado, procura por arquivos de texto (.txt) e extrai e-mails de cada arquivo.

****2. Remoção de Duplicatas:**** Os e-mails extraídos são armazenados em um conjunto (set), garantindo que apenas e-mails únicos sejam mantidos.

****3. Interatividade com o Usuário:**** O usuário é solicitado a fornecer o caminho do diretório onde os arquivos de texto estão localizados.

****4. Finalização Controlada:**** Ao pressionar Ctrl+C durante a execução, o script perguntará se o usuário deseja finalizar o programa.

### Como Usar

1. ****Requisitos:****

- Python 3.x instalado.

2.  ****Execução:****

- Execute o script no terminal ou prompt de comando.
- O script solicitará o caminho do diretório onde os arquivos de texto estão localizados.
- Os e-mails únicos serão extraídos e salvos em um arquivo chamado emails_sem_duplicatas.txt.

3. ****Exemplo:****

	****$ python extrator_emails.py****<br>
	****Insira o caminho das pastas: C:\caminho\do\seu\diretorio****<br>
	****E-mails únicos extraídos e salvos em emails_sem_duplicatas.txt****

4. ****Finalização Controlada:****

- Ao pressionar Ctrl+C, o script perguntará se deseja realmente finalizar o programa.

****Notas Importantes****

- Certifique-se de que o diretório fornecido contém apenas arquivos de texto (.txt).
- Os e-mails extraídos são salvos no arquivo emails_sem_duplicatas.txt no mesmo diretório do script.

Este script é uma ferramenta útil para organizar e identificar e-mails únicos em um conjunto de arquivos de texto. Certifique-se de respeitar a privacidade e conformidade ao usar este script em dados sensíveis.
