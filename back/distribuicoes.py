from flask import Flask, render_template
from flask_cors import CORS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, cauchy, pareto, triang, gumbel_r, zipf, randint, nbinom
from scipy.special import beta as beta2
import io
import base64

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('<html><head></head><body><h2>Testando</h2></body></html>')


def get_beta():
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

    plt.clf()

    return { 'name': 'Beta', 'graph': beta_image }

def get_cauchy():
    # Parâmetros da distribuição de Cauchy
    x0, gamma = 0, 1
    # Valores do eixo x
    x = np.linspace(cauchy.ppf(0.01, x0, gamma), cauchy.ppf(0.99, x0, gamma), 100)
    # Plotando o gráfico
    plt.plot(x, cauchy.pdf(x, x0, gamma), 'r-', lw=5, alpha=0.6, label='cauchy pdf')

    cauchy_bytes = io.BytesIO()
    plt.savefig(cauchy_bytes, format='jpg')
    cauchy_bytes.seek(0)
    cauchy_image = base64.b64encode(cauchy_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Cauchy', 'graph': cauchy_image }

def get_pareto():
    # Parâmetros da distribuição de Pareto
    b = 2.62
    # Valores do eixo x
    x = np.linspace(pareto.ppf(0.01, b), pareto.ppf(0.99, b), 100)
    # Plotando o gráfico
    plt.plot(x, pareto.pdf(x, b), 'r-', lw=5, alpha=0.6, label='pareto pdf')

    pareto_bytes = io.BytesIO()
    plt.savefig(pareto_bytes, format='jpg')
    pareto_bytes.seek(0)
    pareto_image = base64.b64encode(pareto_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Pareto', 'graph': pareto_image }


def get_triangular():
    # Parâmetros da distribuição Triangular
    c = 0.158
    # Valores do eixo x
    x = np.linspace(triang.ppf(0.01, c), triang.ppf(0.99, c), 100)
    # Plotando o gráfico
    plt.plot(x, triang.pdf(x, c), 'r-', lw=5, alpha=0.6, label='triang pdf')

    triangular_bytes = io.BytesIO()
    plt.savefig(triangular_bytes, format='jpg')
    triangular_bytes.seek(0)
    triangular_image = base64.b64encode(triangular_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Triangular', 'graph': triangular_image }

def get_gumbel():
    # Parâmetros da distribuição Gumbel
    loc, scale = 0, 1
    # Valores do eixo x
    x = np.linspace(gumbel_r.ppf(0.01, loc, scale), gumbel_r.ppf(0.99, loc, scale), 100)
    # Plotando o gráfico
    plt.plot(x, gumbel_r.pdf(x, loc, scale), 'r-', lw=5, alpha=0.6, label='gumbel_r pdf')

    gumbel_bytes = io.BytesIO()
    plt.savefig(gumbel_bytes, format='jpg')
    gumbel_bytes.seek(0)
    gumbel_image = base64.b64encode(gumbel_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Gumbel', 'graph': gumbel_image }

def get_zipf():
    # Parâmetros da distribuição Zipf
    a = 2
    # Valores do eixo x
    x = np.arange(1, 11)
    # Plotando o gráfico
    plt.plot(x, zipf.pmf(x, a), 'r-', lw=5, alpha=0.6, label='zipf pmf')

    zipf_bytes = io.BytesIO()
    plt.savefig(zipf_bytes, format='jpg')
    zipf_bytes.seek(0)
    zipf_image = base64.b64encode(zipf_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Zipf', 'graph': zipf_image }

def zipf_mandelbrot_pdf(x, q, s, N):
    HN = np.sum(1 / np.power(np.arange(1, N + 1) + q, s))
    return 1 / (np.power(x + q, s) * HN)

def get_zipf_mandelbrot():
    # Parâmetros da distribuição de Zipf-Mandelbrot
    q, s = 2.7, 1.1

    # Gera uma sequência de números x
    x = np.arange(1, 100)

    # Limites superiores para a função harmônica generalizada
    N = 1000

    # Calcula a pdf para cada x
    y = zipf_mandelbrot_pdf(x, q, s, N)

    # Desenha o gráfico
    plt.plot(x, y, 'r-', lw=5, alpha=0.6, label='zipf-mandelbrot pmf')

    zipf_bytes = io.BytesIO()
    plt.savefig(zipf_bytes, format='jpg')
    zipf_bytes.seek(0)
    zipf_image = base64.b64encode(zipf_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Zipf-Mandelbrot', 'graph': zipf_image }

def get_rademacher():
    # Parâmetros da distribuição Rademacher
    low, high = -1, 2
    # Valores do eixo x
    x = np.arange(randint.ppf(0.01, low, high), randint.ppf(0.99, low, high))
    # Plotando o gráfico
    plt.plot(x, randint.pmf(x, low, high), 'r-', lw=5, alpha=0.6, label='rademacher pmf')

    rademacher_bytes = io.BytesIO()
    plt.savefig(rademacher_bytes, format='jpg')
    rademacher_bytes.seek(0)
    rademacher_image = base64.b64encode(rademacher_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Rademacher', 'graph': rademacher_image }

def get_nbinom():
    # Parâmetros da distribuição Binomial Negativa
    n, p = 5, 0.5
    # Valores do eixo x
    x = np.arange(nbinom.ppf(0.01, n, p), nbinom.ppf(0.99, n, p))
    # Plotando o gráfico
    plt.plot(x, nbinom.pmf(x, n, p), 'r-', lw=5, alpha=0.6, label='nbinom pmf')

    nbinom_bytes = io.BytesIO()
    plt.savefig(nbinom_bytes, format='jpg')
    nbinom_bytes.seek(0)
    nbinom_image = base64.b64encode(nbinom_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Binomial negativa', 'graph': nbinom_image }

def waring_pdf(x, a, b):
    return beta2(x + b, a - 1) / beta2(b, a)

def get_waring():
    # Parâmetros da distribuição de Waring
    a, b = 2, 1

    # Gera uma sequência de números x
    x = np.arange(1, 100)

    # Calcula a pdf para cada x
    y = waring_pdf(x, a, b)

    plt.plot(x, y, 'r-', lw=5, alpha=0.6, label='waring pmf')

    waring_bytes = io.BytesIO()
    plt.savefig(waring_bytes, format='jpg')
    waring_bytes.seek(0)
    waring_image = base64.b64encode(waring_bytes.read()).decode()

    plt.clf()

    return { 'name': 'Waring', 'graph': waring_image }

@app.route('/distribuicoes', methods=['GET'])
def get_distribuicoes():
    distribuicoes = [
        {
            "name": "Contínuas",
            "func": []
        },
        {
            "name": "Discretas",
            "func": []
        }
    ]
    continuas = distribuicoes[0]["func"]
    discretas = distribuicoes[1]["func"]

    continuas.append(get_beta())
    continuas.append(get_cauchy())
    continuas.append(get_pareto())
    continuas.append(get_triangular())
    continuas.append(get_gumbel())
    
    discretas.append(get_zipf())
    discretas.append(get_zipf_mandelbrot())
    discretas.append(get_rademacher())
    discretas.append(get_nbinom())
    discretas.append(get_waring())
    

    return distribuicoes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)