from flask import Flask, request

import clone_deal

app = Flask(__name__)


@app.route("/hook", methods=['POST'])
def index():
    content = request.get_json(silent=True)
    print(request)
    print(content)
    print("-" * 50)
    clone_deal.clone_deal(content)
    return "", 200

if __name__ == "__main__":
    app.run(port=5000)
    