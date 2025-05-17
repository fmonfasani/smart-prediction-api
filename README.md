### Predicciones utilizando smart contracts

Esquma
ml-smart-contract-project/
├── ml/ # Entrenamiento del modelo ML (train_model.py)
├── backend/ # FastAPI + SQLite + JWT + CRUD
│ ├── models/ # SQLAlchemy ORM: Usuario, Predicción, Log
│ ├── routers/ # Rutas protegidas: /users, /predictions, /logs
│ ├── auth/ # Lógica de autenticación JWT
│ ├── app.py # App principal FastAPI
│ ├── database.py # Conexión a SQLite
│ ├── schemas.py # Pydantic (validación)
│ ├── utils.py # Hashing, JWT helpers
│ ├── .env # Claves secretas y config
│ └── requirements.txt # Dependencias
├── contract/ # Solidity + deploy script
│ ├── MLContract.sol
│ ├── deploy.py
│ └── hardhat.config.js
├── frontend/ # Vite + React + Tailwind
├── test/ # test_workflow.py (flujo ML + contrato + backend)
├── README.md # Doc técnica para programadores
├── INFORME_PROYECTO.docx # Documento Word para presentación
└── .gitignore # Archivos a ignorar

Contenido

Backend FastAPI listo para ejecutar (con JWT y SQLite)

Modelos, rutas CRUD, endpoints ML + blockchain, documentación Swagger/OpenAPI.

Archivo .env para claves JWT, conexión a SQLite, etc.

✅ Frontend con Vite + React

Pantalla de login.

Panel principal con predicciones + logs.

Acciones seguras vía token JWT.

✅ Smart Contract en Solidity + Script de despliegue Python

Contrato que guarda lastPrediction.

Actualización desde FastAPI con web3.py.

✅ Informe Word (.docx)

Explicación técnica con imágenes, arquitectura, captura de código y resultado final.

Estilo profesional, para mostrar a inversores o empresas.

✅ README técnico + comandos + scripts de prueba (test_workflow.py)
