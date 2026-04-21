FROM python:3.13-alpine

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv venv --clear .venv
RUN uv sync --all-groups
RUN uv pip install --python .venv/bin/python pytest

RUN .venv/bin/pytest src/calculator/test_calculator.py

CMD [".venv/bin/python", "src/calculator/calculator.py"]