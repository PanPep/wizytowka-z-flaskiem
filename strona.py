from flask import Flask, request,redirect,render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return f"Witaj na mojej stronie"

@app.route('/me')
def main():
    return render_template("strona.html")


@app.route('/kontakt', methods=['GET'])
def contact_get():
    return render_template("kontakt.html")
    print("We received GET")


@app.route('/kontakt', methods=['POST'])
def contact_post():
    print("We received POST")
    print(request.form)
    return redirect("/")


if __name__ == "__main__":
    app.run()
