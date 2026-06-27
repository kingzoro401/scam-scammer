from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Scam Scanner is running successfully!"

# This part is VERY IMPORTANT for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render gives the port
    app.run(host="0.0.0.0", port=port)