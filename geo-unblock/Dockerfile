FROM python:3.12-alpine
WORKDIR /app
RUN pip install --no-cache-dir aiohttp==3.11.18
COPY proxy.py /app/proxy.py
USER 10001:10001
EXPOSE 8080
CMD ["python", "/app/proxy.py"]
