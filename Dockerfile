FROM python:3.8.5-buster
LABEL author="Richard Crouch"
LABEL description="Weather Forecast microservice"

# generate logs in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Install Python dependencies
RUN pip3 install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy

# Copy application and files
RUN mkdir /app
COPY app/*.py /app/
WORKDIR /app

EXPOSE 9501

# run Python unbuffered so the logs are flushed
CMD ["python3", "-u", "forecaster_service.py"]
