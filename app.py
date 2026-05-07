from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contacts = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

        return redirect("/")

    return render_template("index.html", contacts=contacts)


@app.route("/delete/<int:index>")
def delete(index):

    contacts.pop(index)

    return redirect("/")


@app.route("/search", methods=["POST"])
def search():

    keyword = request.form["keyword"].lower()

    filtered = []

    for contact in contacts:

        if keyword in contact["name"].lower():

            filtered.append(contact)

    return render_template("index.html", contacts=filtered)


if __name__ == "__main__":
    app.run(debug=True)
