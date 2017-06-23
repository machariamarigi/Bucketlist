[![Build Status](https://travis-ci.org/machariamarigi/Bucketlist.svg?branch=master)](https://travis-ci.org/machariamarigi/Bucketlist)
# Bucketlist

The Bucketlist is an application allows users to record and share things they want to achieve or experience before reaching a certain age. The application's goal is to make it easy for users to keep track pf their dreams and goals.


## Intallation

1. Clone this repo into any directory in your machine

2. Ensure you have `python 3.5` and `virualenv` installed in your machine

3. Create a virtual environment for the project and activate it:
    ```
    virtualenv env
    source env/bin/activate
    ```

4. Enter the app directory
    ```
    cd Bucketlist
    ```

5. Make sure you are in the development branch
    ```
    git checkout development
    ```

6. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Launching the Program
Set the FLASK_APP and FLASK_CONFIG variables as follows:

* `export FLASK_APP=run.py`
* `export FLASK_CONFIG=development`

You can now run the app with the following command: `flask run`