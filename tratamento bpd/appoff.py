import requests, json
import pandas as pd

# Parâmetros
caminho_arquivo_txt = "ata2.txt"
caminho_arquivo_xlsx = "Tópicos - Ata de Reunião.xlsx"
apiKey = "hNPmG5PijUi5HQDylSSB2Q"

# Função para ler a transcrição da reunião a partir de um arquivo .txt
def ler_transcricao(caminho_arquivo_txt):
    with open(caminho_arquivo_txt, 'r', encoding='utf-8') as file:
        return print(file.read())

# Função para ler os tópicos e contextos a partir de um arquivo .xlsx
def ler_topicos_contextos(caminho_arquivo_xlsx):
    df = pd.read_excel(caminho_arquivo_xlsx)
    # Verifique os nomes das colunas e ajuste conforme necessário
    print(f"Colunas do arquivo Excel: {df.columns.tolist()}")
    topicos_contextos = df.to_dict(orient='records')
    return (topicos_contextos)

# Função para fazer a chamada à API da SAI LIBRARY
def chamar_api_sai(apiKey, str_reuniao, str_topico, str_contexto):
    url = "https://gpt-templates.saiapplications.com"
    headers = {"X-Api-Key": apiKey}
    data = {
        "inputs": {
            "str_reuniao": str_reuniao,
            "str_topico": str_topico,
            "str_contexto": str_contexto,
        }
    }
    response = requests.post(f"{url}/api/templates/66884d94334f6817e38a633a/execute", json=data, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Erro na chamada da API: {response.status_code}")
        print(response.text)
        return ""

# Função principal para gerar a ata
def gerar_ata(caminho_arquivo_txt, caminho_arquivo_xlsx, apiKey):
    transcricao = ler_transcricao(caminho_arquivo_txt)
    topicos_contextos = ler_topicos_contextos(caminho_arquivo_xlsx)
    
    html_saida = "<html><head><title>Ata da Reunião</title></head><body>"
    
    for item in topicos_contextos:
        if 'topico' in item and 'contexto' in item:
            topico = item['topico']
            contexto = item['contexto']
            print(f"Processando tópico: {topico}")  # Verifique qual tópico está sendo processado
            resultado_html = chamar_api_sai(apiKey, transcricao, topico, contexto)
            if resultado_html.strip():  # Verifique se o resultado não está vazio
                html_saida += f"<h2>{topico}</h2>"
                html_saida += resultado_html
            else:
                print(f"Sem resultado para o tópico: {topico}")
        else:
            print(f"Chave 'topico' ou 'contexto' não encontrada no item: {item}")
    
    html_saida += "</body></html>"
    
    with open("ata_reuniao.html", "w", encoding='utf-8') as file:
        file.write(html_saida)
    print("Ata gerada com sucesso e salva como 'ata_reuniao.html'")


# Gerar a ata
gerar_ata(caminho_arquivo_txt, caminho_arquivo_xlsx, apiKey)