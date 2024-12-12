create project using pycharm.
create file outrside .venv folder as it help to run your project in local ide as it handles all python dependency.
we will not copy this folder in docker we will handle it in docker file.


steps to  start running code:

1. Create a Virtual Environment: python3 -m venv .venv
2. Activate the Virtual Environment: source .venv/bin/activate
3. Upgrade pip (inside the virtual environment): pip install --upgrade pip
4. Install Dependencies: pip install -r requirements.txt
5. run the scrape.py

