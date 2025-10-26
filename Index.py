from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "segredo_seguro"  # necessário para mensagens flash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    email = request.form.get('email')
    if not email:
        flash('Por favor, insira um e-mail válido.', 'erro')
        return redirect(url_for('home'))
    
    # Aqui você pode salvar o e-mail em um banco de dados, arquivo, ou planilha.
    # Exemplo simples: salvar em arquivo texto
    with open("emails_cadastrados.txt", "a", encoding="utf-8") as f:
        f.write(email + "\n")
    
    flash('Cadastro realizado com sucesso! Obrigado por se inscrever.', 'sucesso')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
