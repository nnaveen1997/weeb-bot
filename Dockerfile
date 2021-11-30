#Base Image
FROM python:3

#Directory for application
WORKDIR /weeb_bot

#Install dependencies 
COPY requirements.txt .


RUN pip install -r requirements.txt

#Copy source code
COPY main.py .
COPY scraper.py .
COPY scraper_search.py .
COPY db_connection.py . 

#Run the app
CMD ["python", "main.py"]