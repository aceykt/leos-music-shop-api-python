# 
FROM python:3.10

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./commands /code/commands
COPY ./dependencies /code/dependencies
COPY ./routes /code/routes
COPY ./main.py /code

RUN python -m commands

ENV JWT_SECRET="abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
ENV JWE_SECRET="abcdabcdabcdabcd"
ENV SEGMENT_WRITE_ID="change-this"

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]