from flask import Flask, request, jsonify, send_file, abort
import os
from gerador_ata import main

app = Flask(__name__)

# Diretório temporário para salvar transcrições
TEMP_DIR = 'temp_transcricoes'

os.makedirs(TEMP_DIR, exist_ok=True)

@app.route('/gerar_ata', methods=['POST'])
def gerar_ata():
    try:
        if 'transcricao' not in request.files:
            return jsonify({"error": "Arquivo de transcrição não encontrado."}), 400
        
        transcricao_file = request.files['transcricao']
        transcricao_path = os.path.join(TEMP_DIR, 'transcricao.txt')
        transcricao_file.save(transcricao_path)
        
        # Chama a função main e passa o caminho da transcrição
        doc_base64 = main(transcricao_path)
        
        
        # Remove o arquivo de transcrição após o processamento
        if os.path.exists(transcricao_path):
            os.remove(transcricao_path)
        
        return jsonify({
            "filename": "resultado.xlsx",
            "file": doc_base64
            })
        
        # URL para download do arquivo gerado
        # return jsonify({
        #     "message": "Documento gerado com sucesso.",
        #     "download_url_formatado": request.url_root + 'gerar_ata/download?filename=ATA_Reuniao_Gerada.docx'
        # })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#--------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
