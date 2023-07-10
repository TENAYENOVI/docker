FROM python:3.2

WORKDIR /app

#copy the python script and data file to the container
COPY script.py datos.txt .

#Define the command to run when the container starts 
CMD ["python","script.py","datos.txt"]