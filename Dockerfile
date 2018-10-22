FROM python:3.7.0-slim-stretch

LABEL maintainer='James Hibbard'

EXPOSE 5000

COPY . /app

RUN apt-get update && apt-get install -y \
    dumb-init \
    && pip install /app \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Example entrypoint command for a flask server
# CMD ["dumb-init", "--", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "housing.app:app"]

# Example entrypoint command for an idle container
CMD ["dumb-init", "--", "tail", "-f", "/dev/null"]