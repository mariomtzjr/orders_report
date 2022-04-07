# orders_report

Order Report API it's an django REST API running without or with docker container.
Includes API documentation using drf-spectacular, so you will be able to know all endpoints supported.
This project it was created and executed over MacOS.

## Setup enviroment
1. Create and virtual environment
`python3 -m venv order_api` where __order_report__ it's venv's name  
2. Activate virtual environment  
`source order_report/bin/activate`  
3. Install dependencies (with venv activated)  
`pip3 install -r requirements.txt`

## Run server without Docker
1. Create models (run migrations)  
`python3 manage.py migrate`
2. Start server (port 8000 by default)  
`python3 manage.py runserver 0.0.0.0:9091`
3. The server is running on http://localhost:9091

## Run server with Docker
1. Start Docker service
2. Build container  
`docker-compose build`
3. Up container  
`docker-compose up`
4. The server is running on http://localhost:9091

## API Docs
You can access it on `http://localhost:9091/api/v1/schema/redocs/` or `http://localhost:9091/api/v1/schema/swagger-ui/`. Also you can download the schema going to `http://localhost:9091/api/v1/schema/`