# Leo's Music Shop API in Python (FastAPI)

This is the coolest API for Leo's Music Shop.

## Running

First define a `.env` file with two variables, like below:

```ini
JWT_SECRET="abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
JWE_SECRET="abcdabcdabcdabcd"
```

Make sure you have all the requirements installed:

```sh
pip install -r requirements.txt
```

Then run it:

```sh
uvicorn main:app --reload
```