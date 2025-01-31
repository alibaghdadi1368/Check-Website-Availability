# Check-Website-Availability

This is a simple Python web application built using Streamlit and the Requests library to check the availability of websites.

**Features**

1. Input a list of website URLs.
2. Check the availability of each website.
3. Display the status of each website (e.g., reachable, not reachable).
4. Automatically monitor website statuses at regular intervals.

# Installation

**Clone the repository:**

```bash
git clone https://github.com/alibaghdadi1368/Check-Website-Availability.git
```



Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

# Usage

1. Run the Streamlit application:

```bash
streamlit run app.py
```

1. Open your web browser and go to the provided URL (usually <http://localhost:8501>).
2. Enter the website URLs you want to check (one per line) and click the "Add URL" button.
3. Click the "Check Availability" button to check the status of each website.
4. Click the "Start Monitoring" button to automatically check the status of each website every 10 seconds.
5. Click the "Stop Monitoring" button to stop the automatic checking of website statuses.

# Dependencies

1. Python 3.7 or higher
2. Streamlit
3. Requests
4. Pillow

# Project Structure

Check-Website-Availability/
│
├── images/              # Directory for images
│   └── ACTIVITY.webp    # Banner image
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
└── README.md            # Project readme

# Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

# License

This project is licensed under the MIT License. See the LICENSE file for details.