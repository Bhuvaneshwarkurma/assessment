from flask import Flask, request, jsonify, send_file
import pdfplumber
import re
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------- Extract Fields ----------
def extract_fields(text):

    data = {
        "policyNumber": "",
        "policyholderName": "",
        "date": "",
        "location": "",
        "claimType": "",
        "estimatedDamage": ""
    }

    try:
        pn = re.findall(r"Policy Number[:\- ]*(\S+)", text)
        name = re.findall(r"Name[:\- ]*(.*)", text)
        date = re.findall(r"Date[:\- ]*(.*)", text)
        location = re.findall(r"Location[:\- ]*(.*)", text)
        claimType = re.findall(r"Claim Type[:\- ]*(.*)", text)
        damage = re.findall(r"Estimated Damage[:₹ ]*(\d+)", text)

        data["policyNumber"] = pn[0] if pn else ""
        data["policyholderName"] = name[0] if name else ""
        data["date"] = date[0] if date else ""
        data["location"] = location[0] if location else ""
        data["claimType"] = claimType[0] if claimType else ""
        data["estimatedDamage"] = damage[0] if damage else ""

    except Exception as e:
        print("Extraction Error:", e)

    return data


# ---------- Routing Rules ----------
def apply_rules(data, text):

    missing = [k for k,v in data.items() if v == ""]

    route = "Manual Review"
    reason = ""

    if missing:
        route = "Manual Review"
        reason = "Mandatory fields missing"

    elif "injury" in data["claimType"].lower():
        route = "Specialist Queue"
        reason = "Injury claim detected"

    elif any(word in text.lower() for word in ["fraud","staged","inconsistent"]):
        route = "Investigation Flag"
        reason = "Suspicious keywords found"

    elif data["estimatedDamage"] and int(data["estimatedDamage"]) < 25000:
        route = "Fast-track"
        reason = "Damage below ₹25,000"

    return route, reason, missing


# ---------- Extract Text ----------
def extract_text(filepath):

    try:
        if filepath.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()

        elif filepath.endswith(".pdf"):
            text = ""
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
            return text
    except Exception as e:
        print("File Read Error:", e)

    return ""


# ---------- Routes ----------
@app.route("/")
def home():
    return send_file("index.html")


@app.route("/process", methods=["POST"])
def process():
    try:
        if "file" not in request.files:
            return jsonify({"error":"No file uploaded"}), 400

        file = request.files["file"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        text = extract_text(path)

        fields = extract_fields(text)
        route, reason, missing = apply_rules(fields, text)

        return jsonify({
            "extractedFields": fields,
            "missingFields": missing,
            "recommendedRoute": route,
            "reasoning": reason
        })

    except Exception as e:
        print("SERVER ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
