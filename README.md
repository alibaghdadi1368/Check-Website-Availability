# Check-Website-Availability

**Check-Website-Availability**

This is a simple Python web application built using Streamlit and the Requests library to check the availability of websites.
Features

    Input a list of website URLs.
    Check the availability of each website.
    Display the status of each website (e.g., reachable, not reachable).

**Installation**

#     Clone the repository:

    ```console
    git clone https://github.com/alibaghdadi1368/Check-Website-Availability.git
    ```


Create a virtual environment and activate it:


```console
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```



Install the required packages:


```console
pip install -r requirements.txt

```


**Usage**

#     Run the Streamlit application:
   
    ```console
    streamlit run app.py
    ```
    

    Open your web browser and go to the provided URL (usually http://localhost:8501).

    Enter the website URLs you want to check (one per line) and click the "Check All" button.

    The status of each website will be displayed.

**Dependencies**

    Python 3.7 or higher
    Streamlit
    Requests

**Project Structure**

```markdown
website-availability-checker/
│
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md           # Project readme
```

**Contributing**

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

**License**

This project is licensed under the MIT License. See the LICENSE file for details.