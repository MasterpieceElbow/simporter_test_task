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

### 1.3 Production environment
- Type `export FLASK_ENV=prodution` and `flask run` in order to run app in the production environment.
- This uses `config.py` with private settings, don't share this file. It was added just for the explanation.

### 1.4 API response screenshot
Example API response screenshot for query `/api/timeline/?startDate=2018-01-01&endDate=2018-07-01&Grouping=monthly&Type=cumulative&stars=5&source=amazon`

<img width="266" alt="image" src="https://user-images.githubusercontent.com/80070761/221438396-33c025ff-17a3-4272-a785-76acccbdcc04.png">
