from flask import Flask, render_template, request, session
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# import os
# os.environ["MISTRAL_API_KEY"] = "sk-your-mistral-key"

app = Flask(__name__)
app.secret_key = 'bharath75'

llm = ChatMistralAI(model="mistral-tiny", temperature=0.7)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []

    result = ""
    if request.method == 'POST':
        query = request.form['query']

        memory = ConversationBufferMemory()
        for q, a in session['chat_history']:
            memory.chat_memory.add_user_message(q)
            memory.chat_memory.add_ai_message(a)

        conversation = ConversationChain(llm=llm, memory=memory)
        result = conversation.run(query)

        session['chat_history'].append((query, result))
        session.modified = True

    return render_template('index.html', result=result, chat_history=session.get('chat_history', []))

if __name__ == '__main__':
    app.run(debug=True)
