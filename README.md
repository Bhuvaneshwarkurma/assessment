Here’s a **clean, professional README.md** you can directly paste into your project (GitHub-ready and suitable for evaluation submission).

---

# 🧾 FNOL Claims Processing Agent

Autonomous Insurance FNOL (First Notice of Loss) processing system that extracts claim details from uploaded documents and applies intelligent routing rules to recommend the next workflow step.

---

## 🚀 Project Overview

This project simulates an AI-assisted insurance claims intake system.
Users upload FNOL documents (PDF/TXT), the backend extracts structured data, evaluates business rules, and returns a JSON decision output.

The system demonstrates:

* Document ingestion
* Field extraction
* Missing data detection
* Claim routing automation
* Simple interactive UI

---

## ✨ Features

✅ Upload FNOL claim documents
✅ Extract structured fields from files
✅ Identify missing mandatory information
✅ Apply routing rules:

* Fast-track processing
* Specialist queue
* Investigation flag
* Manual review

✅ Download JSON decision output
✅ Modern responsive UI

---

## 🧱 Tech Stack

**Frontend**

* HTML5
* CSS3
* Vanilla JavaScript

**Backend**

* Python
* Flask
* pdfplumber (PDF text extraction)
* Regex-based field parsing

---

## 📂 Project Structure

```
project/
│
├── app.py              # Flask backend
├── index.html          # UI interface
├── uploads/            # Uploaded files
└── README.md
```

---

## ⚙️ Installation & Setup
- clone the the repo https://github.com/Bhuvaneshwarkurma/assessment.git
- install the requirements file pip install - r requirements.txt
- run the index.html file & pyhton app.py
- open http://127.0.0.1:5000
 
### 1️⃣ Install Dependencies

```bash
pip install flask pdfplumber
```

### 2️⃣ Run the Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧠 Processing Logic

After upload, the system:

1. Extracts text from PDF/TXT
2. Detects fields like:

   * Policy Number
   * Name
   * Date
   * Location
   * Claim Type
   * Estimated Damage
3. Applies routing rules:

| Condition                | Route              |
| ------------------------ | ------------------ |
| Missing mandatory fields | Manual Review      |
| Injury detected          | Specialist Queue   |
| Fraud keywords detected  | Investigation Flag |
| Damage < ₹25,000         | Fast-track         |

---

## 📤 Example Output

```json
{
  "extractedFields": {
    "policyNumber": "PN-12345",
    "policyholderName": "Ramesh Kumar",
    "date": "2026-02-01",
    "location": "Hyderabad",
    "claimType": "damage",
    "estimatedDamage": "20000"
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Damage below ₹25,000"
}
```

---

## 🎯 Evaluation Goals

This project demonstrates:

* Autonomous claim intake simulation
* Business rule automation
* Structured JSON outputs
* Clean UX for insurance workflows

---

## 🔒 Disclaimer

This is a demonstration project using dummy data and simplified logic.
Not intended for production insurance processing.

---

## 👨‍💻 Author

**KURMA Bhuvaneshwar**
Autonomous Insurance Claims Processing Project

---

