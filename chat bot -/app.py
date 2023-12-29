from flask import Flask, render_template, request
from langchain.llms import GooglePalm

app = Flask(__name__)

# Set your ChatGPT API key
api_key = ""
llm = GooglePalm(google_api_key=api_key, temperature=1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = llm(user_input)
    return render_template('index.html', user_input=user_input, bot_response=bot_response)
   

if __name__ == '__main__':
    app.run(debug=True)
