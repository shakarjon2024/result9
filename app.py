from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result9():
    if request.method == "POST":
        phone = request.form.get("phone")
        date = request.form.get("date")
        
        return render_template("result9.html")


    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
