### PostgreSQL RESTful API with Flask example

## Getting Started

### Prerequisites

Kindly ensure you have the following installed:
- [ ] [Python 3.6](https://www.python.org/downloads/release/python-365/)
- [ ] [Pip](https://pip.pypa.io/en/stable/installing/)
- [ ] [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [ ] [PostgreSQL](https://www.postgresql.org/)

### Setting up + Running

1. With Python 3.6 and Pip installed:

    ```
    $ virtualenv --python=python3 env --no-site-packages
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ```

2. Create PostgreSQL database named relok_dev with schema relok (Need to change src url):

    ```
    Inside schema make table rl_lokacija with attributes naziv & adresa
    ```

3. Export the required environment variables:

    ```
    $ export FLASK_APP=app.py
    ```

6. Run the Flask API:

    ```
    $ flask run
    ```

7. Navigate to `http://localhost:5000/lokacije` to view the locations data.


