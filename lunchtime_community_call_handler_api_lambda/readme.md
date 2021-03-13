# Lunchtime.io API
There are 4 main endpoints
## /Health
Health status checks. If up, will return 'ok'

## /Meeting - POST {time allocated, number of people in meeting, UID }

If running on localhost, use this to test:

<code> curl -XPOST -H 'id: ddd' -H "Content-type: application/json" -d '{TEST}' 'http://127.0.0.1:5000/meeting'</code>