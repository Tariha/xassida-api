<br />
<p align="center">
  <a href="https://xassida.sn">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <p align="center">
    Le code source officiel de l'API Xassida.sn
    <br />
    <a href="https://chat.whatsapp.com/JHyMbb1hOLj51yTXKy6fwM"><strong>Rejoignez la communauté »</strong></a>
    <br />
    <br />
    <a href="https://xassida.sn">Visiter Xassida.sn</a>
    ·
    <a href="https://github.com/Tariha/xassida-api/issues">Signalez un Bug</a>
  </p>
</p>

## Requirements
- Python 3.9 or later

## Installation

Faudra d'abord cloner le projet:
   ```bash
   git clone https://github.com/Tariha/xassida-api.git
   cd xassida-api
   ```
### Executer en locale
2. Intaller les dépendances
   ```bash
   pip install -r requirements.txt
   ```
3. Executer les migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Remplir la base de donnée
   ```bash
   ./load_db.sh
   ```
5. Executer le serveur
   ```bash
   python manage.py runserver
   ```

### Executer avec Docker
1. Créer l'image
    ```bash
    docker build . -t xassidapi
    ```
2. Executer un conteneur
    ```bash
    docker run -p 8000:8000 xassidapi
    ```
### Utilisation
 - Ouvrez votre navigateur sous `localhost:8000`

## Comment contribuer ?
  Vous pouvez aider en ouvrant ou résolvant les **issues** ouverts [ici](https://github.com/Tariha/xassida-api/issues)
  
## Documentation de l'api bientôt

## License
This project is licensed under the MIT License.
