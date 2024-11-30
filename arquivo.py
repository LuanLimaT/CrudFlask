from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.mundo

# Coleções com o banco
paises_collection = db.paises
cidades_collection = db.cidades
rios_collection = db.rios

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Adicionar país
@app.route('/adicionar_pais', methods=['POST'])
def adicionar_pais():
    pais_data = {
        'nome': request.form['pais_nome'],
        'continente': request.form['pais_continente'],
        'populacao': request.form['pais_populacao'],
        'pib': request.form['pais_pib'],
        'expectativa': request.form['pais_expec'],
    }
    paises_collection.insert_one(pais_data)
    return redirect(url_for('listar_paises'))

# Listar países com filtros
@app.route('/listar_paises', methods=['GET'])
def listar_paises():
    filtro_nome = request.args.get('pais_nome', '')
    filtro_continente = request.args.get('pais_continente', '')
    filtro_populacao = request.args.get('pais_populacao', '')
    filtro_pib = request.args.get('pais_pib', '')
    filtro_expec = request.args.get('pais_expec', '')

    # Construa o filtro para a consulta no MongoDB
    query = {}

    if filtro_nome:
        query['nome'] = {'$regex': filtro_nome, '$options': 'i'}
    if filtro_continente:
        query['continente'] = {'$regex': filtro_continente, '$options': 'i'}
    if filtro_populacao:
        query['populacao'] = {'$gte': int(filtro_populacao)}
    if filtro_pib:
        query['pib'] = {'$gte': float(filtro_pib)}
    if filtro_expec:
        query['expectativa'] = {'$gte': float(filtro_expec)}

    # Realiza a consulta no MongoDB com o filtro
    paises = paises_collection.find(query)

    return render_template('listagem_paises.html', paises=paises, filtro_nome=filtro_nome, filtro_continente=filtro_continente, filtro_populacao=filtro_populacao, filtro_pib=filtro_pib, filtro_expec=filtro_expec)

# Deletar país
@app.route('/deletar_pais/<pais_id>', methods=['POST'])
def deletar_pais(pais_id):
    paises_collection.delete_one({'_id': ObjectId(pais_id)})
    return redirect(url_for('listar_paises'))

# Atualizar país (exibe o formulário)
@app.route('/atualizar_pais/<pais_id>', methods=['GET'])
def atualizar_pais(pais_id):
    pais = paises_collection.find_one({'_id': ObjectId(pais_id)})
    return render_template('atualizar_pais.html', pais=pais)

# Atualizar país (processa a atualização)
@app.route('/atualizar_pais/<pais_id>', methods=['POST'])
def processar_atualizacao_pais(pais_id):
    pais_data = {
        'nome': request.form['pais_nome'],
        'continente': request.form['pais_continente'],
        'populacao': request.form['pais_populacao'],
        'pib': request.form['pais_pib'],
        'expectativa': request.form['pais_expec'],
    }
    paises_collection.update_one({'_id': ObjectId(pais_id)}, {'$set': pais_data})
    return redirect(url_for('listar_paises'))

# Adicionar cidade
@app.route('/adicionar_cidade', methods=['POST'])
def adicionar_cidade():
    cidade_data = {
        'nome': request.form['cidade_nome'],
        'pais': request.form['cidade_pais'],
        'populacao': request.form['cidade_populacao'],
        'capital': request.form['cidade_capital'] == 'Sim'
    }
    cidades_collection.insert_one(cidade_data)
    return redirect(url_for('listar_cidades'))

# Listar cidades com filtros
@app.route('/listar_cidades', methods=['GET'])
def listar_cidades():
    filtro_nome = request.args.get('cidade_nome', '')
    filtro_pais = request.args.get('cidade_pais', '')
    filtro_populacao = request.args.get('cidade_populacao', '')
    filtro_capital = request.args.get('cidade_capital', '')

    query = {}

    if filtro_nome:
        query['nome'] = {'$regex': filtro_nome, '$options': 'i'}
    if filtro_pais:
        query['pais'] = {'$regex': filtro_pais, '$options': 'i'}
    if filtro_populacao:
        query['populacao'] = {'$gte': int(filtro_populacao)}
    if filtro_capital:
        query['capital'] = True if filtro_capital.lower() == 'sim' else False

    cidades = cidades_collection.find(query)

    return render_template('listagem_cidades.html', cidades=cidades, filtro_nome=filtro_nome, filtro_pais=filtro_pais, filtro_populacao=filtro_populacao, filtro_capital=filtro_capital)

# Deletar cidade
@app.route('/deletar_cidade/<cidade_id>', methods=['POST'])
def deletar_cidade(cidade_id):
    cidades_collection.delete_one({'_id': ObjectId(cidade_id)})
    return redirect(url_for('listar_cidades'))

# Atualizar cidade (exibe o formulário)
@app.route('/atualizar_cidade/<cidade_id>', methods=['GET'])
def atualizar_cidade(cidade_id):
    cidade = cidades_collection.find_one({'_id': ObjectId(cidade_id)})
    return render_template('atualizar_cidade.html', cidade=cidade)

# Atualizar cidade (processa a atualização)
@app.route('/atualizar_cidade/<cidade_id>', methods=['POST'])
def processar_atualizacao_cidade(cidade_id):
    cidade_data = {
        'nome': request.form['cidade_nome'],
        'pais': request.form['cidade_pais'],
        'populacao': request.form['cidade_populacao'],
        'capital': request.form['cidade_capital'] == 'Sim'
    }
    cidades_collection.update_one({'_id': ObjectId(cidade_id)}, {'$set': cidade_data})
    return redirect(url_for('listar_cidades'))

# Adicionar rio
@app.route('/adicionar_rio', methods=['POST'])
def adicionar_rio():
    rio_data = {
        'nome': request.form['rio_nome'],
        'nascente': request.form['rio_nascente'],
        'pais': request.form['rio_pais'],
        'comprimento': request.form['rio_comprimento']
    }
    rios_collection.insert_one(rio_data)
    return redirect(url_for('listar_rios'))

# Listar rios com filtros
@app.route('/listar_rios', methods=['GET'])
def listar_rios():
    filtro_nome = request.args.get('rio_nome', '')
    filtro_nascente = request.args.get('rio_nascente', '')
    filtro_pais = request.args.get('rio_pais', '')
    filtro_comprimento = request.args.get('rio_comprimento', '')

    query = {}

    if filtro_nome:
        query['nome'] = {'$regex': filtro_nome, '$options': 'i'}
    if filtro_nascente:
        query['nascente'] = {'$regex': filtro_nascente, '$options': 'i'}
    if filtro_pais:
        query['pais'] = {'$regex': filtro_pais, '$options': 'i'}
    if filtro_comprimento:
        query['comprimento'] = {'$gte': int(filtro_comprimento)}

    rios = rios_collection.find(query)

    return render_template('listagem_rios.html', rios=rios, filtro_nome=filtro_nome, filtro_nascente=filtro_nascente, filtro_pais=filtro_pais, filtro_comprimento=filtro_comprimento)

# Deletar rio
@app.route('/deletar_rio/<rio_id>', methods=['POST'])
def deletar_rio(rio_id):
    rios_collection.delete_one({'_id': ObjectId(rio_id)})
    return redirect(url_for('listar_rios'))

# Atualizar rio (exibe o formulário)
@app.route('/atualizar_rio/<rio_id>', methods=['GET'])
def atualizar_rio(rio_id):
    rio = rios_collection.find_one({'_id': ObjectId(rio_id)})
    return render_template('atualizar_rio.html', rio=rio)

# Atualizar rio (processa a atualização)
@app.route('/atualizar_rio/<rio_id>', methods=['POST'])
def processar_atualizacao_rio(rio_id):
    rio_data = {
        'nome': request.form['rio_nome'],
        'nascente': request.form['rio_nascente'],
        'pais': request.form['rio_pais'],
        'comprimento': request.form['rio_comprimento']
    }
    rios_collection.update_one({'_id': ObjectId(rio_id)}, {'$set': rio_data})
    return redirect(url_for('listar_rios'))



# Detalhar país
@app.route('/detalhar_pais/<pais_id>', methods=['GET'])
def detalhar_pais(pais_id):
    pais = paises_collection.find_one({'_id': ObjectId(pais_id)})
    return render_template('detalhar_pais.html', pais=pais)

# Detalhar cidade
@app.route('/detalhar_cidade/<cidade_id>', methods=['GET'])
def detalhar_cidade(cidade_id):
    cidade = cidades_collection.find_one({'_id': ObjectId(cidade_id)})
    return render_template('detalhar_cidade.html', cidade=cidade)


# Detalhar rio
@app.route('/detalhar_rio/<rio_id>', methods=['GET'])
def detalhar_rio(rio_id):
    rio = rios_collection.find_one({'_id': ObjectId(rio_id)})
    return render_template('detalhar_rio.html', rio=rio)



if __name__ == '__main__':
    app.run(debug=True)
