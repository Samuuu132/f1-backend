# F1 Drivers API 🏎️

API REST para gestionar pilotos de Fórmula 1, construida con FastAPI y SQLite.

## Screenshot

<img width="1001" height="1060" alt="image" src="https://github.com/user-attachments/assets/86452695-fe8b-4a46-9315-15cf073c280d" />


## Tecnologías usadas

- Python 3.11
- FastAPI
- SQLite
- Docker

## Cómo correr el proyecto localmente

### Opción 1 — Con Docker (recomendado)

1. Tener Docker Desktop instalado y corriendo
2. Clonar el repositorio:
git clone https://github.com/Samuuu132/f1-backend.git
cd f1-backend/backend
3. Correr el contenedor:
docker-compose up --build
4. Abrir en el navegador: `http://localhost:8000`

### Opción 2 — Sin Docker

1. Clonar el repositorio:
git clone https://github.com/Samuuu132/f1-backend.git
cd f1-backend/backend
2. Instalar dependencias:
pip install -r requirements.txt
3. Correr el servidor:
uvicorn main:app --reload
4. Abrir en el navegador: `http://localhost:8000`

## API en producción

👉 https://backend-8xza.onrender.com

## Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /drivers | Listar todos los pilotos |
| GET | /drivers/{id} | Obtener un piloto por ID |
| POST | /drivers | Crear un piloto nuevo |
| PUT | /drivers/{id} | Editar un piloto existente |
| DELETE | /drivers/{id} | Eliminar un piloto |

## Parámetros disponibles en GET /drivers

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| page | Número de página | ?page=1 |
| limit | Resultados por página | ?limit=5 |
| q | Buscar por nombre | ?q=max |
| sort | Campo para ordenar | ?sort=nombre |
| order | Dirección del orden | ?order=asc |

## Documentación Swagger

👉 https://backend-8xza.onrender.com/docs

## Sobre CORS

CORS es una política de seguridad del navegador que bloquea las peticiones
entre dominios distintos. Como el cliente y el servidor corren en puertos
diferentes, configuramos CORS en el servidor para permitir explícitamente
las peticiones del frontend.

Configuramos los siguientes headers:
- Access-Control-Allow-Origin: *
- Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
- Access-Control-Allow-Headers: Content-Type

## Challenges implementados

- ✅ Swagger UI corriendo desde el backend
- ✅ Códigos HTTP correctos (201, 204, 404, 400)
- ✅ Validación server-side con mensajes descriptivos en JSON
- ✅ Paginación con ?page= y ?limit=
- ✅ Búsqueda por nombre con ?q=
- ✅ Ordenamiento con ?sort= y ?order=
- ✅ Soporte para imágenes en Base64
- ✅ Docker configurado

## Reflexión

Elegí FastAPI como framework principal porque ofrece generación automática de
documentación Swagger, lo cual facilita tanto el desarrollo como la revisión
del proyecto. Opté por SQLite como base de datos ya que no requiere un servidor
adicional y es suficiente para el alcance de este proyecto. En cuanto a los
desafíos, implementar la paginación, búsqueda y ordenamiento me ayudó a
entender mejor cómo diseñar endpoints flexibles. Utilizaría estas tecnologías
nuevamente en proyectos de escala similar.

## Link al repositorio del cliente

👉 https://github.com/Samuuu132/f1-frontend
