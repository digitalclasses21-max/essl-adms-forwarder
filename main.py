arsalan stddyut jhygrlo bhfjft vhg hbvfg bnsgrfhtge fhtgfghg 7678014988 vtygtjy vhhgkkygmhfff ootgvjt  ftyehf   dghfdbngf tejj65773mjk htj  abcdefghijklomnpqrstuvwxyz ryykhgy fghgfh y gytmr gyutghg  yufgfg nfrom flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual Google Apps Script Web App URL
GAS_WEBAPP_URL = "YOUR_GAS_WEB_APP_URL_HERE"

@app.route('/DeviceService/DeviceData', methods=['POST'])
def device_data():
    try:
        # ESSL device sends form-data, parse it here
        data = request.form.to_dict()

        # Prepare JSON data to forward to Google Apps Script
        payload = {
            "EmployeeID": data.get("Pin"),
            "Date": data.get("Date"),
            "TimeIn": data.get("Time"),
            "TimeOut": "",
            "DeviceName": "ESSL_Device",
            "Remarks": ""
        }

        # Forward to Google Apps Script Web App
        response = requests.post(GAS_WEBAPP_URL, json=payload)

        return jsonify({"status": "success", "forward_response": response.text})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
bjghr jghhrhg jkgjhhyg h;rhhg;j 'dgfttgt' yrhhg4u bhgjfy tyughr hfggrb hgrjh htygjf hgyhu 