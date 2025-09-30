from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual Google Apps Script Web App URL
GAS_WEBAPP_URL = "https://script.google.com/macros/s/AKfycbxCdq1GIHEyY2xiA38Xp6RViJg9z7khFBtxsOckf685ubUq9Zl99Ul4lnzzuz8xuZRx/exec"

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
