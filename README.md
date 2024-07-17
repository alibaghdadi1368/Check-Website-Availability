#     Check-Website-Availability


This is a simple Python web application built using Streamlit and the Requests library to check the availability of websites.

**Features**

1- Input a list of website URLs.
2- Check the availability of each website.
3- Display the status of each website (e.g., reachable, not reachable).


#     Installation

**Clone the repository:**

    
```markdown
git clone https://github.com/alibaghdadi1368/Check-Website-Availability.git
```
    


Create a virtual environment and activate it:

```markdown
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```




Install the required packages:

```markdown
pip install -r requirements.txt
```



#     Usage

1- Run the Streamlit application:
   
  
    ```markdown
    streamlit run app.py
    ```
   
    

2- Open your web browser and go to the provided URL (usually http://localhost:8501).

3- Enter the website URLs you want to check (one per line) and click the "Check All" button.

4- The status of each website will be displayed.

#     Dependencies

1- Python 3.7 or higher
2- Streamlit
3- Requests


#     Project Structure

```markdown
website-availability-checker/
│
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md           # Project readme
```

#     Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

#     License

This project is licensed under the MIT License. See the LICENSE file for details.