from flask import Flask, render_template, request
app = Flask(__name__)

uploaded_file = None


@app.route('/')
def index():
    with open('your_file.txt', 'r') as file:
        lines = file.readlines()
    first_words = [line.split()[0] for line in lines]

    uploaded_lines = []
    if uploaded_file:
        with open(uploaded_file, 'r') as uploaded:
            uploaded_lines = uploaded.readlines()
    first_word = [line.split()[0] for line in uploaded_lines]

    return render_template('index.html', first_words=first_words, lines=lines,  first_word=first_word)


@app.route('/line/<int:index>')
def show_line(index):
    with open('your_file.txt', 'r') as file:
        lines = file.readlines()
    line = lines[index - 1]
    return line


@app.route('/upload', methods=['POST'])
def upload_file():
    global uploaded_file
    file = request.files['file']
    file.save('upload.txt')
    uploaded_file = 'upload.txt'
    return 'Гайд добавлен!'


if __name__ == '__main__':
    app.run(debug=True)
