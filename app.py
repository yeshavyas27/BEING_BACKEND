import os
#
from global_utilities import app, ssl_context


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=os.environ.get("FLASK_PORT"),
        ssl_context=ssl_context
    )