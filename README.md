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

Parte 1: Backend FastAPI + ML + Blockchain (completo y funcional)
Incluye:
CRUD completo de:

✅ Usuarios (/users)

✅ Predicciones (/predictions)

✅ Logs de actividad (/logs)

Endpoints de ML y contrato inteligente:

/predict → hace predicción usando el modelo.

/trigger → envía predicción a la blockchain.

/status → consulta el estado actual del contrato.

Autenticación JWT:

/auth/register

/auth/login

Base de datos SQLite (app.db) lista o vacía.

Swagger automático disponible en http://localhost:8000/docs

.env con claves (puede ser editado).

ML: modelo LogisticRegression, guardado como model.pkl

⚙️ Herramientas extra incluidas:
start_backend.bat: ejecuta FastAPI en Windows.

.vscode/launch.json: corre el backend con F5 en VSCode.

install.bat: instala dependencias + entrena el modelo.

reset_db.bat: borra y reinicia la base SQLite.

También incluye:
README.md con instrucciones claras.

🧠 Primer avance del documento Word INFORME_PROYECTO.docx, con:

Introducción

Estructura y flujo del sistema

Comparación DB vs Blockchain

Capturas y ejemplos

Listo para presentación o exportar a PDF

Pasos:

Integrar la predicción con el contrato inteligente (que /predict llame al contrato).

Testear y validar el deploy del contrato en contract/deploy.py.

Crear una interfaz web mínima para probar el flujo end-to-end (FastAPI + Swagger o frontend mínimo).

Auditar logs o guardar predicciones en logs.log o en la DB app.db.

Mejorar y documentar el pipeline de predicción para producción.

Hacer pruebas automáticas con test/test_workflow.py.
