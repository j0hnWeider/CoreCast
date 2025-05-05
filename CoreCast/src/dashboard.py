from flask import Flask, render_template, jsonify
import pandas as pd
import json

app = Flask(__name__)

# Simulação de dados para o dashboard
data = {
    'sensor': ['A', 'B', 'C', 'D'],
    'valor': [23, 45, 12, 67]
}
df = pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
