# StockF
Simple web application for aggregating stock forecasts.

* [RU Documentation on Pages](https://github.com/nah990/StockF/wiki/)
* [Current Tasks](https://github.com/nah990/StockF/projects/1?add_cards_query=is%3Aopen)
* [Bug tracker](https://github.com/nah990/StockF/projects/2?add_cards_query=is%3Aopen)
* [Apache Benchmark testing](APACHE.md)

# Installation

**Clone the sources**

```
# Get the code
git clone https://github.com/nah990/StockF.git
```

<br />

Make sure you have Docker installed then write in dir.
For version with one backend.
```
docker-compose --profile solo-backend up -d --build
```

or
For version with multiple backend to enable nginx rebalancing features.
```
docker-compose --profile multi-backend up -d --build
```

After that just visit
```
http://localhost:1337/
```
Enjoy!
