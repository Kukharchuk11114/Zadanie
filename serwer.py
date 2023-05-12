from flask import Flask, request
import datetime
import socket

app = Flask(__name__)

# Pobranie informacji o dacie, autorze i porcie serwera
startup_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
author = "Illia Kukharchuk"  
port = 5000  # Port, na którym serwer będzie nasłuchiwał

# Wyświetlenie informacji w logach
print("Serwer został uruchomiony.")
print("Data uruchomienia:", startup_time)
print("Autor:", author)
print("Port:", port)

@app.route("/")
def index():
    # Pobranie adresu IP klienta
    client_ip = request.remote_addr

    # Pobranie daty i godziny w strefie czasowej klienta
    client_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

    # Generowanie treści strony
    content = f"<h1>Informacje o kliencie</h1>"
    content += f"<p>Adres IP klienta: {client_ip}</p>"
    content += f"<p>Data i godzina w strefie czasowej klienta: {datetime.datetime.now(client_timezone)}</p>"

    return content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)

