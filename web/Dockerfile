FROM python
WORKDIR /home/myapp
# Install dependencies first for better layer caching
RUN pip install --no-cache-dir flask pymongo

# Copy application files and folders
COPY ./templates ./templates
COPY ./static ./static
COPY ./app.py .

EXPOSE 8080
CMD ["python", "/home/myapp/app.py"]