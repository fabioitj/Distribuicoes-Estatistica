from flask import Flask
from flask_cors import CORS
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, cauchy, pareto, triang, gumbel_r
import io
import base64

app = Flask(__name__)
CORS(app)

@app.route('/distribuicoes', methods=['GET'])
def get_beta():
    distribuicoes = [
        {
            "name": "Contínuas",
            "func": [
                {
                    "name": "beta",
                    "image": ""
                },
                {
                    "name": "cauchy",
                    "image": ""
                },
                {
                    "name": "pareto",
                    "image": ""
                },
                {
                    "name": "triangular",
                    "image": ""
                },
                {
                    "name": "gumbel",
                    "image": ""
                },
            ]
        },
        {
            "name": "Discretas",
            "func": [
                {
                    "name": "beta",
                    "image": ""
                },
                {
                    "name": "cauchy",
                    "image": ""
                },
                {
                    "name": "pareto",
                    "image": ""
                },
                {
                    "name": "triangular",
                    "image": ""
                },
                {
                    "name": "gumbel",
                    "image": ""
                },
            ]
        }
    ]

    # Parâmetros da distribuição Beta
    a, b = 2, 5
    # Valores do eixo x
    x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99, a, b), 100)
    # Plotando o gráfico
    plt.plot(x, beta.pdf(x, a, b), 'r-', lw=5, alpha=0.6, label='beta pdf')
   
    beta_bytes = io.BytesIO()
    plt.savefig(beta_bytes, format='jpg')
    beta_bytes.seek(0)
    beta_image = base64.b64encode(beta_bytes.read()).decode()




@app.route('/cauchy', methods=['GET'])
def get_cauchy():
    return '2'

@app.route('/pareto', methods=['GET'])
def get_pareto():
    return '2'

@app.route('/triangular', methods=['GET'])
def get_triangular():
    return '2'

@app.route('/gumbel', methods=['GET'])
def get_gumbel():
    return '2'

if __name__ == '__main__':
    app.run()