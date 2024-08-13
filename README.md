# Daily-Word
Jednostavan projekat iz predmeta CS230 - Distribuirani sistemi koji implementira direktni pretplatnički sistem u Python-u.

## Predlog teme

Tema projektnog zadatka je “Daily Word” (“Pretplata na dnevnu reč”). Ovaj projekat omogućava korisnicima da se pretplate preko sajta, i svakog jutra u 9.30 dobijaju mejl sa dnevnom rečju.

## Struktura aplikacije

Aplikacija koristi Flask framework za komunikaciju sa sajtom. Unete mejl adrese se čuvaju u SQLite bazi podataka, a mejlovi se šalju koristeći SMTP protokol i MIME ekstenziju. BackgroundScheduler pokreće funkciju za slanje mejlova svakog jutra u 9.30 sati.

## Opis funkcionalnosti

Aplikacija je podeljena na nekoliko Python fajlova:

- **database.py:** Kreira vezu sa bazom podataka i formira tabele `daily_words` (za čuvanje dnevnih reči) i `emails` (za čuvanje pretplaćenih mejlova).
- **add_words.py:** Definiše funkciju `add_daily_word` za unos reči u bazu podataka.
- **send_words.py:** Sadrži funkcije `send_daily_word` za slanje dnevne reči na email adresu i `send_daily_word_to_all` za slanje reči svim pretplatnicima. Ove funkcije koriste SMTP server za slanje emailova.
- **app.py:** Postavlja osnovu za veb aplikaciju pomoću Flask-a, uključuje rute za prikaz početne stranice i obradu korisničkih prijava. Takođe, koristi BackgroundScheduler za zakazivanje dnevnog slanja emailova.

## Izgled aplikacije

Početna stranica aplikacije:

![image](https://github.com/user-attachments/assets/a71af1f7-0660-439d-a84e-35cdb80b7b0b)


## Zaključak

Projekat “Daily Word” demonstrira uspešnu upotrebu Flask frameworka, SQLite baze podataka, SMTP protokola i BackgroundScheduler-a. Kreirana aplikacija omogućava pretplatu i svakodnevno slanje novih reči engleskog jezika putem mejla.

