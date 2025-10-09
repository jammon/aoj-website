# Internetseite von AldOndJong eG

Die Internetseite der AldOndJong eG wird gestaltet mit dem Static Site Generator [Lektor](https://getlektor.com).
Für die Hauptseite und die Blogposts wurden spezielle Models und Templates angepasst.
Als CSS-Framework kommt [Tailwind](https://tailwindcss.com) zum Einsatz.
Alle Bilder gehören der AldOndJong eG und sind nicht gemeinfrei.

Die Inhalte werden in Markdown geschrieben.
Eine Besonderheit sind Mailadressen:
Um die Adressen etwas vor Spam-Harvestern zu schützen, werden sie in der Form von `[acount](/email)` eingegeben und
eine Javascriptfunktion macht daraus `<a href="mailto:account@aldondjong.de">account@aldondjong.de</a>`

Um die Entwicklungsumgebung auf deinem Rechner zu installieren, [installiere zunächst Lektor](https://www.getlektor.com/docs/installation/) und das [lektor-tailwind-Plugin](https://github.com/frostming/lektor-tailwind).
Dann clone dieses Repo in ein eigenes Verzeichnis.
Für das Deployment müssen die Zugangsdaten in `AldOndJong.lektorproject` angepasst werden.

Development Server starten: `lektor server`

Deployment auf Staging-Server: `lektor deploy staging`

Deployment auf Production erfolgt mit FTP/rclone.
