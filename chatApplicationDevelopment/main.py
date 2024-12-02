from flask import Flask
from routes import auth_routes, chat_routes

app = Flask(__name__)

# Configuration settings
app.config.from_envvar('APP_CONFIG_FILE')

# Registering blueprints
app.register_blueprint(auth_routes)
app.register_blueprint(chat_routes)

if __name__ == '__main__':
    app.run(debug=True)
