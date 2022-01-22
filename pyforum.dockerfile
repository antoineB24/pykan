FROM django
COPY . /app
RUN make /app
CMD python /app/manage.py 