# API de Consulta de Dados CSV

Esta aplicação Flask expõe uma API para consulta de dados de um arquivo CSV (Prévia da população calculada com base nos resultados do Censo
"Demográfico 2022 até 25 de dezembro de 2022
"UF","COD. UF","COD. MUNIC","NOME DO MUNICÍPIO","POPULAÇÃO").

## Como executar

1. Instale as dependências:
   ```sh
   pip install flask pandas
   ```

2. Execute o app:
   ```sh
   python api_csv_consulta.py
   ```

## Endpoints

- `/` — Teste de status da API.
- `/dados` — Retorna todos os registros do CSV.
- `/dados/<int:index>` — Retorna o registro pelo índice.

## Observações

- O arquivo CSV deve estar no caminho `python\SP_POP2022 (1).csv`.

Prévia da população calculada com base nos resultados do Censo
"Demográfico 2022 até 25 de dezembro de 2022
"UF","COD. UF","COD. MUNIC","NOME DO MUNICÍPIO","POPULAÇÃO"