FROM python:3.7-slim-buster

COPY . /api
WORKDIR /api

# Install requirements
RUN pip install -r requirements.txt

# Set flask variables
RUN export FLASK_APP=main.py
ENV FLASK_ENV=development

# Make Entrypoint
RUN chmod +x /api/entrypoint.sh

# Run app when the container launches
CMD ["/bin/bash", "/api/entrypoint.sh"]