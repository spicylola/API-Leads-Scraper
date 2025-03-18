# API-Leads-Scraper
A scraping tool that grabs business leads using Google Maps Api, Youtube API, IG API, Maybe Tiktok API

# API Leads Scraper 🚀

A Python-based tool that scrapes business leads from Google Maps and exports them as a CSV file.

## 📌 Features

- **Extracts business data from Google Maps API**
- **Stores leads in an SQLite database**
- **Exports business leads to a CSV file**
- **Uses Flask CLI commands for easy automation**

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/api-leads-scraper.git
cd api-leads-scraper
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # (For macOS/Linux)
venv\Scripts\activate     # (For Windows)
```

### 3️⃣ Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 4️⃣ Set Up the Database

```bash
flask db init
flask db migrate
flask db upgrade
```

### 5️⃣ Configure Environment Variables

Set your Flask app and Google Maps API Key:

For macOS/Linux:
```bash
export FLASK_APP=api_leads_scraper.app
export GOOGLE_MAPS_API_KEY={your_google_maps_api_key}
```

For Windows PowerShell:
```powershell
$env:FLASK_APP="api_leads_scraper.app"
$env:GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
```

## 🛠️ Usage

### 🔍 Scrape & Export Business Leads

Run the following command to scrape fitness classes in NYC and export them to CSV:

```bash
flask make_csv --text_queries "fitness classes nyc" --business_type "fitness classes"
```

Modify the query to target different businesses:

```bash
flask make_csv --text_queries "yoga studios brooklyn, pilates classes manhattan" --business_type "yoga"
```

## 📂 Output

The script generates a CSV file containing business leads with the following details:

- Business Name
- Address
- Phone Number
- Website
- Google Rating

## ⚠️ API Limits & Considerations

- Google Maps API has a free tier limit — check your quota to avoid overuse fees.
- Ensure your API key has the correct permissions (Places API, Geocoding API).

## 📏 To-Do / Future Improvements

- *List any upcoming features or enhancements here.*

## 📜 License

This project is open-source under the MIT License.

## 👨‍💻 Author

Lola – Reach out on lolashonaikedev@gmail.com

🚀 **Happy Scraping!**
```
