from flask import Flask

import NLPfunctions

app = Flask(__name__)
# 处理中文编码
app.config['JSON_AS_ASCII'] = False


@app.route("/key_words", methods=["GET"])
def key_words():
    return NLPfunctions.key_words()


@app.route("/sentiment_scores", methods=["GET"])
def sentiment_scores():
    return NLPfunctions.sentiment_scores()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
