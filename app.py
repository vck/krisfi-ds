from flask import Flask, request, redirect

app = Flask("krisfi-ds")

def lin_reg(x):
    return 42.619*x + -0.814

@app.route("/", methods=["GET", "POST"])
def index_page():
    if request.method == "POST":
        massa = float(request.form["massa"])
        f = lin_reg(massa)
        html = f""" 
        <html>
            <p>{f}</p>
            <form method="post" action="/">
                <p>masukkan nilai massa (Kg)</p>
                <input type="text" name="massa" required>
                <input type="submit" value="Submit">
            </form>
        </html>
        
        """
        return html

    html = """
    <html>
        <form method="post" action="/">
            <p>masukkan nilai massa (Kg)</p>
            <input type="text" name="massa" required>
            <input type="submit" value="Submit">
        </form>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(port=8000)
