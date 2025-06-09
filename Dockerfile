# Use an official Python image (make sure it's compatible with your project, fallback to 3.12 if 3.13 isn't stable)
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2

# Set workdir
WORKDIR /app

# Install curl and poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get purge -y curl && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

# Add poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy only the dependency files first
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the project files
COPY . .

RUN poetry install
# Set entrypoint to bash so you can run commands like 'poetry run pytest' manually
ENTRYPOINT ["bash"]
