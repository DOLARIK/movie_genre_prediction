FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV API_URI http://plot_summary_genre_api:8501/v1/models/bert:predict

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY plot_summary_genre ./plot_summary_genre
COPY main.py main.py
# COPY boot.sh ./
# RUN chmod 755 boot.sh
# RUN chmod +x boot.sh

ENV FLASK_APP main.py 

# EXPOSE 5000

# CMD ["python", "main.py"]
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "--timeout=30000", "main:app"]
