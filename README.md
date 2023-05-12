# Zadanie
# /Zadanie1$ sudo docker build -t zadanie1 .
# Sending build context to Docker daemon   5.12kB
# Step 1/7 : FROM python:3.9
#  ---> 27ac39eccd1f
# Step 2/7 : WORKDIR /app
#  ---> Using cache
#  ---> 87f46a731c19
# Step 3/7 : COPY requirements.txt .
#  ---> fc9e725132ed
# Step 4/7 : RUN pip install --no-cache-dir -r requirements.txt
#  ---> Running in 87c686293120
# Collecting Flask==2.0.0
#   Downloading Flask-2.0.0-py3-none-any.whl (93 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.2/93.2 KB 1.6 MB/s eta 0:00:00
# Collecting Werkzeug>=2.0
#   Downloading Werkzeug-2.3.4-py3-none-any.whl (242 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.5/242.5 KB 2.6 MB/s eta 0:00:00
# Collecting Jinja2>=3.0
#   Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 KB 6.8 MB/s eta 0:00:00
# Collecting click>=7.1.2
#   Downloading click-8.1.3-py3-none-any.whl (96 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 KB 2.5 MB/s eta 0:00:00
# Collecting itsdangerous>=2.0
#   Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
# Collecting MarkupSafe>=2.0
#   Downloading MarkupSafe-2.1.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
# Installing collected packages: MarkupSafe, itsdangerous, click, Werkzeug, Jinja2, Flask
# Successfully installed Flask-2.0.0 Jinja2-3.1.2 MarkupSafe-2.1.2 Werkzeug-2.3.4 click-8.1.3 itsdangerous-2.1.2
# WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a # virtual environment instead: https://pip.pypa.io/warnings/venv
# WARNING: You are using pip version 22.0.4; however, version 23.1.2 is available.
# You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
# Removing intermediate container 87c686293120
#  ---> 13aaccc66fa2
# Step 5/7 : COPY serwer.py .
#  ---> 98cd3921aa2a
# Step 6/7 : EXPOSE 5000
#  ---> Running in 40eaac2c4bac
# Removing intermediate container 40eaac2c4bac
#  ---> 2e277c4ccdba
# Step 7/7 : CMD ["python", "serwer.py"]
#  ---> Running in 2e48974b7318
# Removing intermediate container 2e48974b7318
#  ---> 45188861116c
# Successfully built 45188861116c
# Successfully tagged zadanie1:latest
# VirtualBox:~/Zadanie1$ sudo docker run -p 5000:5000 zadanie1
# Serwer został uruchomiony.
# Data uruchomienia: 2023-05-12 16:49:59
# Autor: Illia Kukharchuk
# Port: 5000
#  * Serving Flask app 'serwer' (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on all addresses (0.0.0.0)
#  * Running on http://127.0.0.1:5000
#  * Running on http://172.17.0.2:5000
# Press CTRL+C to quit
# Serwer HTTP przy użyciu biblioteki Flask. Po uruchomieniu kontenera, serwer wypisuje informacje o dacie uruchomienia, autorze oraz porcie, na którym nasłuchuje. # Połączenia od klientów obsługiwane są przez funkcję index, która zwraca stronę informacyjną zawierającą adres IP klienta oraz datę i godzinę w strefie czasowej # klienta. Adres IP klienta jest pobierany z nagłówka żądania HTTP.
# Dockerfile bazuje na oficjalnym obrazie Pythona w wersji 3.9. Kopiuje plik server.py oraz plik requirements.txt 
# Instaluje zależności z pliku requirements.txt i eksponuje port 5000, na którym serwer nasłuchuje. W końcu, uruchamia program serwera server.py po starcie  
# 
# Zadanie 3
#  Zbudowanie obrazu kontenera:
#  docker build -t zadanie1 .
#  Wynik powyżej
# Uruchomienie kontenera na podstawie zbudowanego obrazu:
# docker run -p 5000:5000 zadanie1
# Wynik powyżej
# Aby uzyskać informacje wygenerowane przez serwer w trakcie uruchamiania kontenera, przeglądnie logi kontenera. Można to zrobić za pomocą polecenia:
# VirtualBox:~/Zadanie1$ sudo docker logs optimistic_sutherland
# Serwer został uruchomiony.
# Data uruchomienia: 2023-05-12 16:49:59
# Autor: Illia Kukharchuk
# Port: 5000
#  * Serving Flask app 'serwer' (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on all addresses (0.0.0.0)
#  * Running on http://127.0.0.1:5000
#  * Running on http://172.17.0.2:5000
# Press CTRL+C to quit
# Aby sprawdzić, ile warstw posiada zbudowany obraz
# VirtualBox:~/Zadanie1$ sudo docker image inspect zadanie1 | grep "Layers" -c
# 1
