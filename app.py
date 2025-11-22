from flask import Flask, request, redirect, url_for, render_template_string
import uuid

app = Flask(__name__)

# In-memory storage for notes
notes = {}

@app.route('/')
def home():
    return 'Bilhetinho App funcionando!'

@app.route('/create', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        message = request.form.get('message', '').strip()
        if not message:
            return 'Por favor, forneça uma mensagem.', 400
        code = uuid.uuid4().hex[:8]
        notes[code] = message
        return redirect(url_for('view_note', code=code))
    return '''
        <h1>Criar Bilhetinho</h1>
        <form method="post">
            <textarea name="message" rows="4" cols="50" placeholder="Escreva seu bilhetinho aqui"></textarea><br>
            <button type="submit">Gerar bilhetinho</button>
        </form>
    '''

@app.route('/note/<code>')
def view_note(code):
    message = notes.get(code)
    if not message:
        return 'Bilhetinho não encontrado.', 404
    return render_template_string(
        "<h1>Bilhetinho</h1><p>{{message}}</p>",
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)
