# Build Service

## Start Local
### With docker
```shell
docker compose up --build
```
### Without docker
#### Install dependencies
##### if poetry 
```shell
poetry install
```
##### if venv
```shell
pip install -r requirements.txt
```
#### Start service
```shell
uvicorn src.asgi:app --host 0.0.0.0 --port 9999
```

## Tests
### With docker
```shell
docker compose -f docker-compose_test.yml up --build
```
### Without docker
#### Install dependencies
##### if poetry 
```shell
poetry install
```
##### if venv
```shell
pip install -r requirements.txt
```
#### Start tests
```shell
python3 -m unittest tests/test.py
```