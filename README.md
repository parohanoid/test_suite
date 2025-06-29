# test_suite

A sample repo for API Testing (Pytest + Requests + Allure)

Mock API used: https://dummyjson.com

### Setup:
1. Clone > Run `python3 -m venv .venv`
2. Run `pip install -r requirements.txt`
3. Run `source .venv/bin/activate`
4. Run `pytest`

### Primer / Notes:
1. Arguments to run the tests in pytest.ini
2. Fixtures in tests_api/conftest.py
3. To install additional packages, 
    - Activate venv
    - Install package
    - Run `pip freeze > requirements.txt`

#### Very basic notes
1. Config git username and email:
    - `git config user.name "[name]"`
    - `git config user.email "[email]"`
2. Setup ssh
    - Run `ssh-keygen`
    - Add contents of id_ed25519.pub [here](https://github.com/settings/keys)

https://github.github.io/actions-cheat-sheet/actions-cheat-sheet.html



For Selenium:
1. `apt-get -y update`
2. `apt-get -y install google-chrome-stable`