from flask import Flask
from housing.exception import HousingException  
import os,sys
from housing.logger import logging
app =  Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    try:
        raise Exception("We are raising custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
        return "Hello Match"

if __name__=="__main__":
    app.run(debug=True)