"""Flask Hello World App"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Root page."""
    app.logger.debug("hello_world")
    return 'Hello, World! - modified version'


if __name__ == "__main__":
    app.run()
