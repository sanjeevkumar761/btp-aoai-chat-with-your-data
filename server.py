import os
from flask import Flask, request
from promptflow.client import load_flow
from promptflow.entities import AzureOpenAIConnection
from promptflow.entities import FlowContext
import subprocess
from dotenv import load_dotenv

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))

load_dotenv()

llm_connection = AzureOpenAIConnection(
    name="llm_connection", api_key=os.getenv("AZURE_OPENAI_API_KEY"), api_base=os.getenv("AZURE_OPENAI_ENDPOINT")
)

f = load_flow(".")
chat_history=[]
f.context = FlowContext(
    # override flow connections with connection object created above
    connections={"process_results": {"connection": llm_connection}}
)


@app.route('/chat')
def chat():
    question=request.args.get("question")
    print(question)
    result = f(user_query=question, chat_history=chat_history)
    #result = f(user_query=question)
    print(result)
    #chat_history.append({"inputs": {'user_query': question}, "outputs": result})
    return result["processed_result"]
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)