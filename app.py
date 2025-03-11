from flask import Flask, render_template, request

app = Flask(__name__)

def totalmarks(pt1, pt2, hy, f, pracs, theorymax):
    marks = (theorymax / 400) * (pt1 + pt2 + (120 / theorymax) * (hy + 2 * f)) + pracs
    return marks

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Convert inputs to float to support both integers and decimals
            pt1 = float(request.form["pt1"])
            pt2 = float(request.form["pt2"])
            hy = float(request.form["hy"])
            f = float(request.form["f"])
            pracs = float(request.form["pracs"])
            theorymax = float(request.form["theorymax"])

            final_score = totalmarks(pt1, pt2, hy, f, pracs, theorymax)
            return render_template("index.html", result=round(final_score, 2))
        except ValueError:
            return render_template("index.html", error="Invalid input! Please enter numbers only.")

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
