# ATA_API

API para geração automática de atas de reunião a partir de transcrições de áudio/texto.

## Objetivo
Esta aplicação permite transformar transcrições de reuniões em documentos de ata formatados automaticamente, facilitando o registro e a documentação de decisões e discussões.

## Funcionalidades
- Recebe arquivos de transcrição via API (upload).
- Processa o texto e gera um documento de ata estruturado.
- Retorna o arquivo gerado em formato base64 para download.
- Utiliza processamento de texto e integração com modelos de linguagem.

## Como funciona
1. O usuário faz upload de um arquivo de transcrição (texto) para o endpoint `/gerar_ata`.
2. O backend processa o texto, gera a ata e retorna o arquivo pronto para download.

## Requisitos
- Python 3.8+
- Bibliotecas: Flask, pandas, python-docx, requests, beautifulsoup4, psycopg2, chardet, python-dotenv, etc.
- (Opcional) Banco de dados PostgreSQL para integração com tabelas de tópicos/contextos.

## Instalação
```bash
pip install -r requirements.txt
```

## Executando a API
```bash
python api.py
```
Acesse: `http://localhost:5000/gerar_ata`

## Exemplo de uso (via cURL)
```bash
curl -X POST -F "transcricao=@/caminho/para/transcricao.txt" http://localhost:5000/gerar_ata
```

## Estrutura dos arquivos
- `api.py`: API Flask para upload e download das atas.
- `gerador_ata.py`: Lógica de processamento, integração com modelos e geração do documento.
- `temp_transcricoes/`: Pasta temporária para transcrições recebidas.

## Observações importantes
- **Todos os nomes de pessoas, empresas e dados sensíveis foram anonimizados para fins de portfólio.**
- Não utilize credenciais reais ou dados confidenciais neste repositório.
- Este projeto é um exemplo didático e pode ser adaptado conforme a necessidade.

## Autor
Projeto adaptado e anonimizado por [Seu Nome].
