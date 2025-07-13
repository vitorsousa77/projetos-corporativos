import pandas as pd
from flask import Flask, jsonify, send_from_directory

# Le arquivos
arquivosCsv = [
    'SP_POP2022 (1).csv',
    'RJ_POP2022.csv',
    'BA_POP2022.csv',
    'PA_POP2022.csv']


# Leitura e processamento dos arquivos CSV
listaDeFrames = []
for arquivo in arquivosCsv:
    df = pd.read_csv(arquivo, skiprows=2)

# Tratamento dos dados da dataframe (DataFrame)
    df = df.dropna()
    df['POPULAÇÃO'] = df['POPULAÇÃO'].str.replace('.', '', regex=False)
    df['COD. UF'] = df['COD. UF'].astype(int)
    df['COD. MUNIC'] = df['COD. MUNIC'].astype(int)
    df['COD. CONCATENADO'] = df['COD. UF'].astype(str) + df['COD. MUNIC'].astype(str)
    df['COD. CONCATENADO'] = df['COD. CONCATENADO'].str.replace('.', '', regex=False)
    df['COD. CONCATENADO'] = df['COD. CONCATENADO'].astype(int)
    
        
# Adiciona o DataFrame à lista
    listaDeFrames.append(df)

# Concatenando todos os DataFrames em um único DataFrame
dframe = pd.concat(listaDeFrames, ignore_index=True)
    
# Seleção das colunas que devem ser exibidas no retorno da API
colunasSelecionadas = ['COD. CONCATENADO', 'POPULAÇÃO', 'NOME DO MUNICÍPIO', 'UF']

# Verifica o dataframe no terminal
print(dframe) 

# Criação da API
app = Flask(__name__)

# Rotas ------------------------------------------------
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/dados')
def dados():
    dadosSelect = dframe[colunasSelecionadas]
    json_dados = dadosSelect.to_dict(orient='index')    
    return jsonify(json_dados)
  
@app.route('/dados/<cod>', methods=['GET'])
def cidade(cod):
    codMun = int(cod)
    cidadeData = dframe[dframe['COD. CONCATENADO'] == codMun]
    cidadeDadosSelect = cidadeData[colunasSelecionadas]
    jsonDados = cidadeDadosSelect.to_dict(orient='index')
    return jsonify(jsonDados)

if __name__ == '__main__':
    app.run(debug=True)
