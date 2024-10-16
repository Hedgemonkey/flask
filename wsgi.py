print("Importing app from app.py")

from app import app  # Import your Flask app instance
import os


if __name__ == "__main__":
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=True
        )