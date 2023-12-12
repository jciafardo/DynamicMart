FROM python:3.11.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /Ecom_Store_Project

WORKDIR /Ecom_Store_Project

COPY . /Ecom_Store_Project/
RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirments.txt

COPY . /Ecom_Store_Project/

RUN python ecom_store/manage.py collectstatic --noinput

RUN apt-get update
# Clean up unnecessary files and packages
RUN rm -rf /var/lib/apt/lists/* /root/.cache


CMD ["python", "ecom_store/manage.py", "runserver"]
