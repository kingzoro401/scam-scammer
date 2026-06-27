from flask import Flask, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Cyber Scanner</title>
    </head>
    <body style="background:black; color:lime; font-family:monospace; text-align:center;">
        <h1>💻 CYBER SCAM SCANNER</h1>
        <p>Enter text or link below</p>

        <form action="/scan">
            <input name="q" size="40" placeholder="Paste here">
            <br><br>
            <button>SCAN</button>
        </form>
    </body>
    </html>
    """

@app.route('/scan')
def scan():
    text = request.args.get('q', '')
    t = text.lower()

    score = 0
    reasons = []

    # keywords
    keywords = ["free", "win", "claim", "gift", "password", "verify", "login", "urgent"]
    for word in keywords:
        if word in t:
            score += 2
            reasons.append("Keyword: " + word)

    # links
    if "http://" in t or "https://" in t:
        score += 2
        reasons.append("Contains link")

    # short links
    if "bit.ly" in t or "tinyurl" in t:
        score += 3
        reasons.append("Shortened link")

    # numbers
    if len(re.findall(r'\d', t)) > 5:
        score += 1
        reasons.append("Too many numbers")

    # result
    if score >= 6:
        result = "HIGH RISK SCAM"
        color = "red"
    elif score >= 3:
        result = "SUSPICIOUS"
        color = "orange"
    else:
        result = "SAFE"
        color = "lime"

    reason_text = "<br>".join(reasons) if reasons else "No threats detected"

    return f"""
    <body style="background:black; color:white; font-family:monospace; text-align:center;">
        <h1>RESULT</h1>
        <p>{text}</p>
        <h2 style="color:{color};">{result}</h2>
        <p>{reason_text}</p>
        <br><a href="/" style="color:cyan;">GO BACK</a>
    </body>
    """

if __name__ == "__main__":
    app.run()