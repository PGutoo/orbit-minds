import json
from flask import Flask, request, render_template
from service.groq_service import groq

app = Flask(__name__)

@app.route('/groq', methods=['POST'])
def groq_test():
    try:
        response = groq(request.json['prompt'])
        return response #render_template('groq_form.html', response=response)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)


# TODO
# 1 Qual especiencia queremos passar?
# 2 Atrelar a fonte de dados ao conhecimento da IA