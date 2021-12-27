# StockF
Simple web application for aggregating stock forecasts.

[RU Documentation](DOCS.md)

# Installation

**Clone the sources**

```
# Get the code
git clone https://github.com/nah990/StockF.git
```

<br />

Make sure you have PostgreSQL installed then install modules with pip.
For Linux you need additional preparations.

```
sudo apt-get install libpq-dev
pip install psycopg2-binary==2.8.6
```

```
pip3 install -r requirements.txt
```

Run setup.py to configure your PostgreSQL integration with Django.
After that just type
```
python manage.py runserver
```
Enjoy!