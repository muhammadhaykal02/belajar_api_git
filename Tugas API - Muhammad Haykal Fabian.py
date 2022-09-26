from flask import Flask, request, jsonify
import re

app = Flask(__name__) # panggil Flask

# GET
@app.route("/get_text/v1", methods=['GET'])     # ini endpoint/urlnya dan metodenya pake GET
def return_text():                              # kita bikin fuction dulu
    name_input = request.args.get("nama")       # name input sebagai input karena ada function get pake query nama
    print(name_input)
    if name_input == "jokowi":                  # karena ada certain condition, jadinya pake IF kalo name_inputnya "jokowi"
        return_text = {
        "nama":f"ya ndak tau kok tanya saya"    # ini bentukannya dictionary karena JSON, pake f karena ngeformat string biar bisa ada inputnya.
    }
        return jsonify(return_text)             # kita ngereturn text as json makanya pake function jsonify
    else:                                       # ini condition selain kalo inputnya jokowi
        return_text = {
        "nama":f"nama beliau adalah {name_input}"
    }
    return jsonify(return_text)

# POST
def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "",s)          # kita bikin function remove punct biar gampang nanti dicallnya.

@app.route("/clean_text/v1", methods=['POST'])  # endpoint/url dan metodenya POST
def len_and_eggs():                             # bikin function lagi
    s = request.get_json()                      # kita ngerequest dalam bentuk json
    non_punct = _remove_punct(s['text'])        # ngehapus punctuation pake string yang keynya text. karena di API requestnya json => dict
    total_karakter = len(s['text'])             # dari soal minta panjang karakternya berapa banyak
    non_punct = non_punct.lower()               # buat ngitung telor, kita seragamin dulu
    non_punct = non_punct.split()               # ngepisah kalimat telor biar jadi list
    filtered_telor = []                         # kita bikin list kosong dulu
    for telor in non_punct:                     # bikin loop buat ngefilter list non_punct (yang tadi dibikin) jadi cuma telor doang
        if telor == "telor":                    # kita bikin variabel telor = telor, buat ngeaddress yang listnya itu telor
            filtered_telor.append(telor)        # kita tambahin/append semua variabel telor ke list kosong tadi (filtered_telor)
    total_telor = len(filtered_telor)           # dari soal minta berapa banyak telor di kalimat
    return jsonify({"total_char":total_karakter, "total_telor":total_telor})    # return dalam jsonify buat total char sama total telor


if __name__ == "__main__":
    app.run(port=2309, debug=True)
