# Leo's Music Shop API in Python (FastAPI)

This is the coolest API for Leo's Music Shop.

For now this API only sells bass guitars. 

## Running

First define a `.env` file with two variables, like below:

```ini
JWT_SECRET="abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
JWE_SECRET="abcdabcdabcdabcd"
SEGMENT_WRITE_ID="your-segment-write-id"
```

Make sure you have all the requirements installed:

```sh
pip install -r requirements.txt
```

Make sure you have a database created and initialized with data:

```sh
python -m commands
```

Then run it:

```sh
uvicorn main:app --reload
```

## Running with Docker

First build the image:

```sh
docker build -t leos-music-shop-api-python .
```

Then run it:

```sh
docker run -dp 80:8001 -e SEGMENT_WRITE_ID "your-segment-write-id" leos-music-shop-api-python
```

This will run the app at port 8001.