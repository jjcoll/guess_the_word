from flask import Flask, session

# Create the Flask application instance
app = Flask(__name__)

# must set a secret key to use session
app.secret_key = "walahi"

# Register the blueprint for routes
from app.routes import bp

app.register_blueprint(bp)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
