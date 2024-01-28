import os
import re
import csv

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

def extract_emails_from_text(text):
    # Utilizando uma expressão regular para encontrar endereços de e-mail
    emails = re.findall(r'\b[A-Za-z0-9._%+-]{1,30}@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails

def extract_emails(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()
        emails = extract_emails_from_text(text)
        
        # Mostrando os e-mails na tela
        if emails:
            print(f"E-mails extraídos de {file_path}:")
            for email in emails:
                print(f"- {email}")
            print("-----------------------------")
        else:
            print(f"Nenhum e-mail encontrado em {file_path}")
        
        return emails

def process_directory(directory_path, txt_output_file, csv_output_file):
    txt_emails = set()
    csv_emails = set()

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".txt"):
                emails = extract_emails(file_path)
                txt_emails.update(emails)
            elif file.endswith(".csv"):
                with open(file_path, 'r', encoding='latin-1') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        for item in row:
                            emails = extract_emails_from_text(item)
                            csv_emails.update(emails)

    with open(txt_output_file, 'w', encoding='utf-8') as txt_output:
        for email in txt_emails:
            txt_output.write(email + '\n')

    with open(csv_output_file, 'w', encoding='utf-8') as csv_output:
        for email in csv_emails:
            csv_output.write(email + '\n')

if __name__ == "__main__":
    try:
        print_banner()
        
        directory_path = input("Insira o caminho das pastas: ")
        txt_output_file = "emails_extraidos_txt.txt"
        csv_output_file = "emails_extraidos_csv.txt"

        process_directory(directory_path, txt_output_file, csv_output_file)

        print(f"E-mails extraídos de arquivos de texto salvos em {txt_output_file}.")
        print(f"E-mails extraídos de arquivos CSV salvos em {csv_output_file}.")

    except KeyboardInterrupt:
        response = input("\nVocê pressionou Ctrl+C. Deseja realmente finalizar o programa? (S/N): ").strip().lower()
        if response == 's':
            print("Programa finalizado.")
        else:
            print("Continuando a execução do programa.")
