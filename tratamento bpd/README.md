# tratamento bpd

Este diretório contém scripts e utilitários para o tratamento, análise e geração de documentos relacionados a transcrições e atas de reuniões do projeto BPD (Business Process Documentation).

## Funcionalidades principais

- **Leitura e processamento de transcrições**: Scripts para ler arquivos `.txt` de transcrições de reuniões.
- **Extração e organização de tópicos**: Leitura de tópicos e contextos a partir de planilhas Excel.
- **Geração automática de atas**: Utilização de IA (API SAI) para gerar atas em HTML a partir das transcrições e tópicos definidos.
- **Conversão e manipulação de documentos**: Funções para extrair texto de arquivos `.docx` e `.pdf`.
- **Integração com planilhas de requisitos e gaps**: Scripts para tratar e organizar informações de requisitos, gaps e processos do projeto.

## Principais arquivos

- `appoff.py`: Script principal para geração de atas de reunião.
- `script_bpd_v17.py`: Diversas funções para manipulação de documentos, integração com APIs e tratamento de dados do projeto.
- `transcricao.txt` / `transcricoes.txt`: Exemplos de transcrições de reuniões.
- Outros scripts utilitários para leitura, extração e organização de dados.

## Como usar

1. Ajuste os caminhos dos arquivos de entrada (transcrição e tópicos) nos scripts.
2. Execute o script principal (`appoff.py`) para gerar a ata da reunião.
3. O resultado será salvo como `ata_reuniao.html` no diretório.

---

> **Observação:** Os scripts dependem de bibliotecas como `pandas`, `requests` e `openpyxl`. Certifique-se de instalar as dependências antes de executar.
