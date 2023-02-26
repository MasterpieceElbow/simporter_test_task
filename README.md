## Simporter's Flask test task

### 1.1 Features:
- Aggregating data
- Grouping by weekly/bi-weekly/monthly
- Filtering data by startDate, endDate, brand, stars, ets.
  
### 1.2 Launching
Tools: Python 3.11.2, SQLite3 3.37.0
- Install venv `python3 -m venv venv`
- Activate venv `source venv/bin/activate`
- Install requirements `pip3 install -r requirements.txt`
- Runserver `flask run`
- Visit `http://127.0.0.1:5000/api/info/` for filtering info
- Visit `http://127.0.0.1:5000/api/timeline/?startDate=2018-01-01&endDate=2018-07-01&Grouping=weekly&Type=cumulative&stars=5` as an timeline example
- Run tests `python3 -m pytest`