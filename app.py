from flask import Flask, render_template

# TODO: import books blueprint here

app = Flask(__name__)

# TODO: register books blueprint here

if __name__ == '__main__':
    app.run(debug=True)
