# Apache Konfiguration

Diese Datei dokumentiert die Konfiguration von drei virtuellen Hosts:

- routenplaner.verkehrsauskunft.at
- default-pr1.verkehrsauskunft.at
- localhost

## Besonderheiten

- CGI und Symlinks erlaubt
- Access-Control-Allow-Origin: "*" gesetzt
- `/api/` via Alias auf `/opt/httpd/routenplaner.verkehrsauskunft.at/api`
- Eigene Logfiles pro Domain
