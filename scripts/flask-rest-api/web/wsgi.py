import os

from web import create_app

app = create_app(os.environ.get("FLASK_ENV") or 'default')

if __name__ == "__main__":
    app.run()
