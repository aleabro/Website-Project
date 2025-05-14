## Setup PostgreSQL
- installazione su windows: https://www.postgresql.org/download/windows/
- durante l'installazione verrà richiesta una password del database. Sarà necessaria per accedervi e servirà passarla anche a django
- creare un database con nome e proprietario (anche questi due sarà necessario fornirli ai setting di django)

## Setup Django
nei settings sarà necessario inserire le istruzioni per accedere al database e sarà una cosa del genere:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_database',
        'USER': 'postgres',
        'PASSWORD': 'la_tua_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
I campi da sostituire saranno localhost (se si omette la riga HOST dovrebbe funzionare visto che Django utilizzerà l'host di default), user, password e name (ed anche la porta se nella configurazione del database sarà diversa).
Questi dati non andranno inseriti direttamente nel database bensì dovrete creare un file chiamato local_auth.py in cui inserire le vostre credenziali. esso sarà ignorato automaticamente da .gitignore (potete constatarlo se vedete il file grigio se 
siete su vs code) ed inserire all'interno di esso il codice che vedete sopra. oltre a quello dovrete aggiungere anche la SECRET_KEY che viene automaticamente creata da django quando create un progetto.

## Passaggi finali
Ultimati i passaggi di configurazione del Database e delle impostazioni potete utilizzare l'applicazione attraverso i comandi
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Aprite il sito alla porta 8000 e dovreste vedere l'home page.
Se runserver non funziona potreste dover eseguire il comando da ambiente virtuale 
