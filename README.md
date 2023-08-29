# DRF Test task about simple api

This is simple api project for qortex`s test task
 
## Features
- Python
- Django
- PostgreSQL
- Docker
- DRF

## How to install
```
1)Clone the project:
- git clone https://github.com/Capsize7/test_task_qortex

2)Run the dockers images
- docker-compose up -d --build

3)Apply migrations for db
- docker-compose exec app python manage.py migrate --noinput

4)Go to http://localhost:8000/api/v1/albums

```

## License

The MIT License (MIT)
