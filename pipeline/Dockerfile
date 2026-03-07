FROM python:3.13.10-slim

# 從官方把uv image 複製進來，放入bin
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./

RUN uv sync --locked 

 
COPY pipeline.py . 

ENTRYPOINT ["python" , "pipeline.py"]