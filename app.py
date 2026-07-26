import os
from flask import Flask, jsonify

app = Flask(__name__)

# ==========================================
# CHANGE THIS TO: "dev", "testing", OR "prod"
# ==========================================

CURRENT_ENV = "UAT"

# Set configurations based on hardcoded environment
if CURRENT_ENV == "UAT":

    app.config.update(
        DEBUG=False,
        TESTING=False,
        ENV_NAME="UAT",
        DATABASE_URL="postgresql://prod_user:password@prod-db-host:5432/mydb",
        PORT=8080,
    )
elif CURRENT_ENV == "testing":
    app.config.update(
        DEBUG=True,
        TESTING=True,
        ENV_NAME="Testing",
        DATABASE_URL="sqlite:///:memory:",
        PORT=5001,
    )
else:  # "dev" (default)
    app.config.update(
        DEBUG=True,
        TESTING=False,
        ENV_NAME="Development",
        DATABASE_URL="sqlite:///dev.db",
        PORT=5000,
    )


@app.route("/", methods=["POST"])
def home():
    return jsonify({
        "status": "success",
        "environment": app.config["ENV_NAME"],
        "debug_mode": app.config["DEBUG"],
        "testing_mode": app.config["TESTING"],
        "database": app.config["DATABASE_URL"],
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP", "environment": CURRENT_ENV}), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=app.config["PORT"],
        debug=app.config["DEBUG"],
    )
