FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PROJECT_DIR=English

WORKDIR /workspace

# Both language folders use the same dependency set.
COPY English/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

COPY . /workspace

EXPOSE 8501

ENTRYPOINT ["bash", "-lc"]
CMD ["cd \"$PROJECT_DIR\" && streamlit run app/streamlit_app.py --server.address=0.0.0.0 --server.port=8501"]
