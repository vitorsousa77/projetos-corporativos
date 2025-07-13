import pandas as pd 
from flask import Flask, request, render_template, send_file

df = pd.read_csv('planilha_transitus.csv')

#print(df)

# Seleção de colunas a para exibição
colunasSelect = ['Requisito', 
                 'Descrição', 
                 'Módulo', 
                 'Nome BPD', 
                 'Processo', 
                 'Subprocesso', 
                 'SCOPE_ITEM', 
                 'ID_GAP',
                 'GAP Descrição']

# Separar os valores em `SCOPE_ITEM` por vírgula
df['SCOPE_ITEM'] = df['SCOPE_ITEM'].str.split(',')

# "Explodir" a coluna para criar uma nova linha para cada valor separado por vírgula
df_exploded = df.explode('SCOPE_ITEM')

# Define a Seleção de colunas no dataframe
df_exploded = df_exploded[colunasSelect]

# Reconta os índices 
#df_exploded.reset_index(drop=True, inplace=True)

print(df_exploded)

# Renomear as colunas
df_exploded.rename(columns={
    'Requisito': 'cod_requisito',
    'Descrição': 'requisito_descricao',
    'Módulo': 'modulo',
    'Nome BPD': 'nome_bpd',
    'Processo': 'processo',
    'Subprocesso': 'sub_processo',
    'SCOPE_ITEM': 'scope_item',
    'ID_GAP': 'cod_gap',
    'GAP Descrição': 'gap_descricao'
}, inplace=True)

#print(df_exploded)

app = Flask(__name__)

@app.route('/')
def home():
    # Extrair nomes únicos da coluna 'nome_bpd'
    unique_nomes_bpd = df_exploded['nome_bpd'].unique()
    return render_template('index.html', nomes_bpd=unique_nomes_bpd)

@app.route('/filter')
def filter_data():
    nome_bpdf = request.args.get('nome_bpd')  # Obtém o parâmetro de consulta
    if nome_bpdf:
        # Filtra o DataFrame com base no nome BPD
        filtered_df = df_exploded[df_exploded['nome_bpd'].str.contains(nome_bpdf, case=False, regex=False, na=False)] 
        file_name = f"Resultado_filtro_{nome_bpdf}.xlsx"
        filtered_df.to_excel(file_name, index=False)
        print(filtered_df)
    #else:
    #   filtered_df = df_exploded  # Se nenhum filtro for especificado, retorna todos os dados
    file_url = f"/download/{file_name}"
    return render_template('filter.html', tables=[filtered_df.to_html(classes='data')], titles=filtered_df.columns.values, file_url=file_url) 

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

#filtered_df.to_excel('arquivo3dj02.xlsx', index=False)

if __name__ == '__main__':
    app.run(debug=True) 
