from flask import Flask, request, jsonify
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from
import re

app = Flask(__name__) # panggil Flask
app.json_encoder = LazyJSONEncoder

swagger_template = dict(
info = {
    'title' : LazyString(lambda: 'percobaan Swagger'),
    'version' : LazyString(lambda: '1'),
    'description' : LazyString(lambda: 'ini belajar Swagger dengan Flask'),
    },
    host = LazyString(lambda: request.host)
)

swagger_config = {
    'headers': [],
    'specs': [
        {
            "endpoint":'docs',
            "route":'/docs.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path":"/flassger_static",
    "swagger_ui": True,
    "specs_route":"/docs/"
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "", s)

@swag_from("swagger_config_post.yml", methods=['POST'])
@app.route("/clean_text/v1", methods=['POST'])
def remove_punct_post():
    s = request.get_json()
    non_punct = _remove_punct(s['text'])
    return jsonify({"hasil bersih":non_punct})

# GET
@swag_from("swagger_config.yml", methods=['GET'])
@app.route("/get_text/v1", methods=['GET']) # DECORATOR; ini mau bikin path endpoint. dan tambahin metode yang mau kita pake.
                                            # (mau merubah tingkah laku function di bawahnya biar sesuai keinginan Flask)
def return_text():         # bikin function
    name_input = request.args.get("name")
    nohp_input = request.args.get("nomerhp")
    return_text = {
        "text":f"halo semua, nama saya adalah {name_input}",
        "no_hape":nohp_input
    }
    return jsonify(return_text) # kita ganti dictionary jadi jsonify karena pengennya si Flask.

if __name__ == "__main__":
    app.run(port=1234, debug=True) # kalo ada input yang salah dia bakal auto restart proses dan ganti pake coding yang baru
