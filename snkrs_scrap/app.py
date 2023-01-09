from flask import Flask, render_template
import os
from dotenv import load_dotenv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from snkrs_scrap.util.database.mysql import (
    mySqlConnection,
    insert_sneaker,
    update_sneaker,
    select_sneaker,
)

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'), strict_slashes=False)
def index():

    url_to_scrap = os.getenv('URL')
    page = urlopen(url_to_scrap)

    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    snkr_name = soup.find_all(
        os.getenv('HTML_ELEMENT_SNKR_NAME'),
        class_=os.getenv('CSS_CLASS_SNKR_NAME'),
    )
    snkr_price = soup.find_all(
        os.getenv('HTML_ELEMENT_SNKR_PRICE'),
        class_=os.getenv('CSS_CLASS_SNKR_PRICE'),
    )
    current_datetime = datetime.now()

    insert_sneaker(snkr_name, snkr_price, current_datetime)
    update_sneaker(snkr_name, snkr_price, current_datetime)
    result = select_sneaker()

    return render_template('index.html', snkr_tag=result)


mySqlConnection(app)
app.run()
