FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# ffmpeg is REQUIRED by PyTgCalls / yt-dlp
RUN apt-get update && apt-get install -y --no-install-recommends \
        ffmpeg git curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p cache assets

EXPOSE 8080

CMD ["python", "-m", "AjayMusic"]
