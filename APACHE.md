# Apache BenchMark

## Single backend
ab -n 100000 -c 400 -k http://127.0.0.1:1337/api/v1/

```
Server Software:        Stockf
Server Hostname:        127.0.0.1
Server Port:            1337

Document Path:          /api/v1/
Document Length:        2218 bytes

Concurrency Level:      400
Time taken for tests:   568.667 seconds
Complete requests:      100000
Failed requests:        0
Keep-Alive requests:    100000
Total transferred:      271900000 bytes
HTML transferred:       221800000 bytes
Requests per second:    175.85 [#/sec] (mean)
Time per request:       2274.670 [ms] (mean)
Time per request:       5.687 [ms] (mean, across all concurrent requests)
Transfer rate:          466.93 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   3.3      0      86
Processing:    38 2270 103.6   2268    2577
Waiting:       21 2270 103.6   2268    2577
Total:         55 2270 101.1   2268    2577

Percentage of the requests served within a certain time (ms)
  50%   2268
  66%   2289
  75%   2303
  80%   2314
  90%   2351
  95%   2393
  98%   2444
  99%   2484
 100%   2577 (longest request)
```

## Multiple backends
ab -n 100000 -c 400 -k http://127.0.0.1:1337/api/v1/

```
Server Software:        Stockf
Server Hostname:        127.0.0.1
Server Port:            1337

Document Path:          /api/v1/
Document Length:        2218 bytes

Concurrency Level:      400
Time taken for tests:   315.886 seconds
Complete requests:      100000
Failed requests:        0
Keep-Alive requests:    100000
Total transferred:      271900000 bytes
HTML transferred:       221800000 bytes
Requests per second:    316.57 [#/sec] (mean)
Time per request:       1263.544 [ms] (mean)
Time per request:       3.159 [ms] (mean, across all concurrent requests)
Transfer rate:          840.58 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   3.0      0      77
Processing:     5 1259 1253.6    636    3225
Waiting:        5 1259 1253.6    636    3225
Total:          5 1259 1253.5    649    3225

Percentage of the requests served within a certain time (ms)
  50%    649
  66%   2431
  75%   2485
  80%   2518
  90%   2621
  95%   2709
  98%   2824
  99%   2895
 100%   3225 (longest request)
```