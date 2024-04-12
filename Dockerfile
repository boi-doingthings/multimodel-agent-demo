# Use the official Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's source code
COPY . .

# Expose the port Streamlit is running on
EXPOSE 8501

ENV STLIT_IN_DOCKER 1

# Run the Streamlit app
CMD ["streamlit", "run", "Rank_+_Search.py"] 

