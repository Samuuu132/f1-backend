from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from database import create_tables, get_connection
from models import DriverCreate

app = FastAPI(
    title="F1 Drivers API",
    description="API para gestionar pilotos de Fórmula 1",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()

@app.get("/")
def root():
    return {"message": "F1 Drivers API funcionando"}

@app.get("/drivers")
def get_drivers(
    page: int = 1,
    limit: int = 10,
    q: str = None,
    sort: str = "id",
    order: str = "asc"
):
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail={"error": "order debe ser asc o desc"}
        )
    campos_validos = ["id", "nombre", "equipo", "nacionalidad", "numero"]
    if sort not in campos_validos:
        raise HTTPException(
            status_code=400,
            detail={"error": f"sort debe ser uno de: {campos_validos}"}
        )
    conn = get_connection()
    if q:
        query = f"SELECT * FROM drivers WHERE nombre LIKE ? ORDER BY {sort} {order}"
        drivers = conn.execute(query, (f"%{q}%",)).fetchall()
    else:
        query = f"SELECT * FROM drivers ORDER BY {sort} {order}"
        drivers = conn.execute(query).fetchall()
    conn.close()
    total = len(drivers)
    inicio = (page - 1) * limit
    fin = inicio + limit
    drivers_paginated = drivers[inicio:fin]
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": [dict(d) for d in drivers_paginated]
    }

@app.get("/drivers/{driver_id}")
def get_driver(driver_id: int):
    conn = get_connection()
    driver = conn.execute("SELECT * FROM drivers WHERE id = ?", (driver_id,)).fetchone()
    conn.close()
    if driver is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "Piloto no encontrado", "id": driver_id}
        )
    return dict(driver)

@app.post("/drivers", status_code=201)
def create_driver(driver: DriverCreate):
    if not driver.nombre.strip():
        raise HTTPException(status_code=400, detail={"error": "El nombre no puede estar vacío"})
    if not driver.equipo.strip():
        raise HTTPException(status_code=400, detail={"error": "El equipo no puede estar vacío"})
    if driver.numero < 1 or driver.numero > 99:
        raise HTTPException(status_code=400, detail={"error": "El número debe estar entre 1 y 99"})
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO drivers (nombre, equipo, nacionalidad, numero, imagen) VALUES (?, ?, ?, ?, ?)",
        (driver.nombre, driver.equipo, driver.nacionalidad, driver.numero, driver.imagen)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, **driver.model_dump()}

@app.put("/drivers/{driver_id}")
def update_driver(driver_id: int, driver: DriverCreate):
    if not driver.nombre.strip():
        raise HTTPException(status_code=400, detail={"error": "El nombre no puede estar vacío"})
    if not driver.equipo.strip():
        raise HTTPException(status_code=400, detail={"error": "El equipo no puede estar vacío"})
    if driver.numero < 1 or driver.numero > 99:
        raise HTTPException(status_code=400, detail={"error": "El número debe estar entre 1 y 99"})
    conn = get_connection()
    existing = conn.execute("SELECT * FROM drivers WHERE id = ?", (driver_id,)).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail={"error": "Piloto no encontrado", "id": driver_id})
    conn.execute(
        "UPDATE drivers SET nombre=?, equipo=?, nacionalidad=?, numero=?, imagen=? WHERE id=?",
        (driver.nombre, driver.equipo, driver.nacionalidad, driver.numero, driver.imagen, driver_id)
    )
    conn.commit()
    conn.close()
    return {"id": driver_id, **driver.model_dump()}

@app.delete("/drivers/{driver_id}", status_code=204)
def delete_driver(driver_id: int):
    conn = get_connection()
    existing = conn.execute("SELECT * FROM drivers WHERE id = ?", (driver_id,)).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail={"error": "Piloto no encontrado", "id": driver_id})
    conn.execute("DELETE FROM drivers WHERE id = ?", (driver_id,))
    conn.commit()
    conn.close()
    return Response(status_code=204)