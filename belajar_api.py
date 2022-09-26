from flask import Flask, request, jsonify
import re

app = Flask(__name__) # panggil Flask

def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "",s)

@app.route("/clean_text/v1", methods=['POST'])
def remove_punct_post():
    s = request.get_json()
    non_punct = _remove_punct(s['text'])
    return jsonify({"hasil_bersih":non_punct})

# GET

@app.route("/get_text/v1", methods=['GET']) # DECORATOR; ini mau bikin path endpoint. dan tambahin metode yang mau kita pake.
                                            # (mau merubah tingkah laku function di bawahnya biar sesuai keinginan Flask)
def return_text():         # bikin function
    name_input = request.args.get("name")
    nohp_input = request.args.get("nomerhp")
    print(name_input)
    return_text = {
        "text":f"halo semua, nama saya adalah {name_input}", # f = format string jadi bisa masukkin variabel name_input
        "no_hape": nohp_input
    }
    return jsonify(return_text) # kita ganti dictionary jadi jsonify karena pengennya si Flask.

if __name__ == "__main__":
    app.run(port=1234, debug=True) # kalo ada input yang salah dia bakal auto restart proses dan ganti pake coding yang baru
