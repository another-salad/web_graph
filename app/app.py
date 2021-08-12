"""Main application"""

from flask import Flask

from common.gen_graph import Graph


app = Flask(__name__)


@app.route("/")
def temp_graph():
    """The default temp line graph"""
    graph = Graph()
    return graph.generate()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
