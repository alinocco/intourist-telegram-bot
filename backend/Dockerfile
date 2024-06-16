# Use an official Python runtime as a parent image
FROM python:3.12.1-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /backend

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Copy Poetry files
COPY pyproject.toml poetry.lock /backend/

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

# Copy project files
COPY . /backend/

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
