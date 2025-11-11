from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from discoveryengine_v1 import answer_query_sample

app = Flask(__name__)
CORS(app)

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
ENGINE_ID = os.getenv("ENGINE_ID")

@app.route('/query', methods=['POST'])
def query():
  data = request.get_json()
  query_text = data.get('query', '')

  try:
    response = answer_query_sample(PROJECT_ID,LOCATION,ENGINE_ID,query_text)
    answer_text = reponse.answer.answer_text if response.answer else "No answer generated"
    reference = [
        {
            "title": ref.chunk_info.document_metadata.title,
            "uri": ref.chunk_info.document_metadata.uri}
        for ref in response.answer.reference
    ] if response.answer and response.answer.references esle []
    return jsonify({"answer": answer_text, "references": references})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
        
