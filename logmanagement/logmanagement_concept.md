# Konzept: Zentrales Logmanagement

## Ziel
Zentrale, durchsuchbare Speicherung aller Logs (Syslog, Apache, Applikationen), inkl. Visualisierung und Alerting.

## Herausforderungen
- Unterschiedliche Formate (JSON, Apache, CSV, Syslog)
- Fehlende Struktur und Metadaten
- Hohes Logvolumen → Storage- und Performanceprobleme
- Kein zentrales Alerting oder Retention-Plan

## Tools
- **Graylog** (einfach, aber schwächer in Visualisierung)
- **ELK Stack (Elasticsearch, Logstash, Kibana)** → besser für Analyse & Dashboards
- **Promtail + Loki + Grafana** → leichtgewichtig

## Vorschläge
- Log-Collector (z. B. Filebeat) auf jedem Server
- Strukturierung mit JSON/Logstash
- Einheitliches Logging-Schema (z. B. `timestamp`, `app`, `severity`, `message`)
- Retention z. B. 90 Tage
- Alerting bei bestimmten Patterns oder Error-Raten
