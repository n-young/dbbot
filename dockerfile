FROM tensorflow/tensorflow:2.1.0-py3

# Copy requirements file
COPY requirements.txt requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt

# Copy files
COPY ./ ./

# Expose port and run server
EXPOSE 5000
CMD ["python3", "app.py"]
