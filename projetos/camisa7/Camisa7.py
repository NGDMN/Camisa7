import time
import schedule
import subprocess
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging

# Configuração de log com data e hora
logging.basicConfig(filename=r"C:\Users\Neil\OneDrive\Documentos\Python\Projetos\Camisa7\log_acesso_site.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')

def carregar_credenciais_do_bitwarden(item_id):
    try:
        # Troque manualmente a chave de sessão sempre que necessário
        session_key = "nW00OMjo4BrKJ7ElnzPENllzKEZWuZui4hYWvvCgnBiHOJn0T1lTjkaMlffwdNTcecoJtUoksRth6c0F/yxKug=="
        
        # Obtenha o item especificado do Bitwarden
        result = subprocess.run(["bw", "get", "item", item_id, "--session", session_key], capture_output=True, text=True)
        item = json.loads(result.stdout)
        
        # Extraia o e-mail e a senha
        email = item['login']['username']
        senha = item['login']['password']
        return {"email": email, "senha": senha}
    except Exception as e:
        logging.error(f"Erro ao carregar credenciais do Bitwarden: {e}")
        return None

def acessar_site():
    try:
        # Carrega as credenciais do Bitwarden
        credenciais = carregar_credenciais_do_bitwarden('7dbc0a84-3bde-40c2-a554-b20d0116fb26')
        if credenciais is None:
            logging.error("Falha ao carregar as credenciais do Bitwarden. Abortando...")
            return
        
        email_bitwarden = credenciais["email"]
        senha_bitwarden = credenciais["senha"]
        
        # Configurações para rodar o Chrome com o perfil padrão
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Remova esta linha para depurar
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Configura o caminho do ChromeDriver
        service = Service(r"C:\Users\Neil\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        
        # Inicializa o navegador com o serviço e opções
        driver = webdriver.Chrome(service=service, options=chrome_options)
        time.sleep(5)
        # Acessa o site
        driver.get("https://camisa7.botafogo.com.br/entrar")
        time.sleep(3)
        
        # Verifica se o login é necessário
        try:
            Email_CPF = driver.find_element(By.ID, 'mat-input-0')
            Senha = driver.find_element(By.ID, 'mat-input-1')
            Btn_Entrar = driver.find_element(By.CSS_SELECTOR, 'button.feng-btn.feng-btn--primary.feng-btn--medium[type="submit"]')
            
            if Email_CPF:
                # Login
                Email_CPF.send_keys(email_bitwarden)
                # Use a senha carregada do Bitwarden
                Senha.send_keys(senha_bitwarden)
                Btn_Entrar.click()
                time.sleep(3)
        except Exception as e:
            logging.error(f"Erro ao realizar o login: {e}")
        
        # Acessa a página de experiências
        driver.get("https://camisa7.botafogo.com.br/experiencias")
        time.sleep(3)
        
        # Fecha o navegador
        driver.quit()
        
        # Log de sucesso com data e hora
        logging.info("Acesso ao site realizado com sucesso.")
    except Exception as e:
        # Log de erro em caso de falha, com data e hora
        logging.error(f"Falha ao acessar o site: {e}")

if __name__ == "__main__":
    acessar_site()
    
    # Agendar o script para rodar diariamente às 5 da manhã
    schedule.every().day.at("05:00").do(acessar_site)

    # Loop para manter o agendamento ativo
    while True:
        schedule.run_pending()
        time.sleep(60)
