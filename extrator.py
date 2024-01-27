import os
import re

def print_banner():
    print()
    print("+==================================================+")
    print("| Autor: Marcio Cruz                               |")
    print("| Sobre: EXTRATOR DE E-MAIL                        |")
    print("|                                                  |")
    print("| Linkedin: linkedin.com/in/marciosecurity         |")
    print("| Telegram: @eth0root                              |")
    print("+==================================================+")
    print()

def extract_emails(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()
        # Utilizando uma expressão regular para encontrar endereços de e-mail
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        
        # Mostrando os e-mails na tela
        if emails:
            print(f"E-mails extraídos de {file_path}:")
            for email in emails:
                print(f"- {email}")
            print("-----------------------------")
        else:
            print(f"Nenhum e-mail encontrado em {file_path}")
        
        return emails

def process_directory(directory_path, output_file):
    unique_emails = set()

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                emails = extract_emails(file_path)
                unique_emails.update(emails)

    with open(output_file, 'w', encoding='utf-8') as output:
        for email in unique_emails:
            output.write(email + '\n')

if __name__ == "__main__":
    try:
        print_banner()
        
        directory_path = input("Insira o caminho das pastas: ")
        output_file = "emails_sem_duplicatas.txt"

        process_directory(directory_path, output_file)

        print(f"E-mails únicos extraídos e salvos em {output_file}.")

    except KeyboardInterrupt:
        response = input("\nVocê pressionou Ctrl+C. Deseja realmente finalizar o programa? (S/N): ").strip().lower()
        if response == 's':
            print("Programa finalizado.")
        else:
            print("Continuando a execução do programa.")
