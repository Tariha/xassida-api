# Tariha api

---

This API aims to make it easy for anyone to read, study, and learn xassidas of different senegalese authors from different Tariha. The project is open source and is built as a collaboration between core team members.

#### Installation

**Requirements**

- **Python 3.9 and later**
  
  ```bash
  pip install -r requirements.txt
  ```

#### Folder Structure

```bash
── README.md
├── api
├── data
│   ├── example.png
│   └── xassidas
│       └── tidjian
│           ├── elhadj-malick-sy
│           │   ├── khilass-zahab
│           │   │   ├── en
│           │   │   │   └── khilass-zahab.txt
│           │   │   ├── fr
│           │   │   │   └── khilass-zahab.txt
│           │   │   └── khilass-zahab.txt
│           └── serigne-babacar
│               └── xassidas.json
├── db.sqlite3
├── manage.py
├── requirements.txt
├── utils
│   ├── db
│   │   ├── helpers.py
│   │   └── insert.py
└── xassida
```

### Global usage

#### Server

```bash
python manage.py runserver
```

## ENDPOINTS DOCUMENTATION HERE
