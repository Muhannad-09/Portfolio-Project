# run.py
from app import create_app  # create_app returns a Flask app configured
import os

app = create_app()

if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_PORT", 5000))
    app.run(host=host, port=port, debug=True)
