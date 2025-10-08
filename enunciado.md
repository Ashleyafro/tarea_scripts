
# Sales Clean & Report CLI

## ¿Qué vas a construir?
Un pequeño **programa de línea de comandos (CLI)** que:
- Lee un CSV de pedidos,
- Aplica **filtros opcionales** por fechas y país,
- Calcula 3 **KPIs** (solo con `status="paid"`):  
  **num_orders**, **total_revenue**, **avg_order_value**,
- Exporta un **resumen** (TXT/JSON) y, opcionalmente, los **pedidos filtrados**.

Además, harás una **mini exploración en un Notebook** para entender los datos, **graficar** y **acordar reglas** que luego aplicarás en el script.

---

## Requisitos
- Python 3.11 (recomendado) con `conda`.
- Editor VS Code o similar y terminal.
- Cuenta de GitHub.

---

## 0) Preparación del entorno y GitHub

### 0.1 Crear entorno conda e instalar dependencias
1) Crea y activa un entorno `salescli` con Python 3.11.
2) En la raíz del proyecto, crea `requirements.txt` con:
```

pandas==2.2.*
matplotlib==3.8.*

```
3) Instala las dependencias con `pip install -r requirements.txt`.

**Comprobación**
- `python -V` → 3.11.x
- `python -c "import pandas, matplotlib; print('ok')"` → debe imprimir `ok`.

### 0.2 Iniciar repositorio Git y conectar con GitHub
1) Inicializa Git y renombra a `main`.
2) Crea `.gitignore` excluyendo caches, checkpoints y `outputs/`.
3) Primer commit.
4) Crea un repo vacío en GitHub y conéctalo (URL de tu repo).

**Comprobación**
- `git status` limpio.
- `git push` sin errores.

---

## 1) Estructura del proyecto

Crea (si no existen):

```

taller-sales-cli/
├─ data/
│  └─ raw/
├─ notebooks/
└─ src/

````

**Checklist**
- [ ] `data/raw/`
- [ ] `notebooks/`
- [ ] `src/`

---

## 2) Datos de ejemplo (CSV)

Crea **`data/raw/orders_sample.csv`** con este contenido:

```csv
order_id,date,country,product,units,unit_price,status,shipping
3001,2025-09-27,ES,Taza Yo <3 Data,2,12.0,paid,standard
3002,2025-09-27,FR,Calcetines con patitos,1,9.0,cancelled,express
3003,2025-09-28,ES,Portatil Modo Kaggle,1,640.0,paid,express
3004,2025-09-28,PT,USB-C Hub Por si acaso,3,29.9,paid,standard
3005,2025-09-28,IT,Monitor 27p 4K para plots,1,179.0,paid,standard
3006,2025-09-29,ES,Raton Click Feliz,4,15.0,paid,express
3007,2025-09-29,FR,Teclado RGB Hacker,1,24.0,paid,express
3008,2025-09-30,ES,Monitor 27p 4K para plots,1,185.0,paid,standard
3009,2025-09-30,DE,Taza Yo <3 Data,2,12.5,cancelled,standard
3010,2025-09-30,FR,Portatil Modo Kaggle,1,655.0,paid,express
3011,2025-10-01,ES,USB-C Hub Por si acaso,2,32.0,paid,standard
3012,2025-10-01,PT,Raton Click Feliz,3,14.5,paid,standard
3013,2025-10-01,IT,Taza Commit > Push > Pray,1,13.5,cancelled,express
3014,2025-10-01,ES,Portatil Modo Kaggle,1,645.0,paid,express
3015,2025-10-02,FR,Monitor 27p 4K para plots,1,175.0,paid,standard
3016,2025-10-02,ES,Teclado RGB Hacker,1,26.0,paid,standard
3017,2025-10-02,DE,Raton Click Feliz,2,15.0,paid,express
3018,2025-10-03,ES,Portatil Modo Kaggle,1,648.0,paid,express
3019,2025-10-03,PT,Monitor 27p 4K para plots,1,171.0,paid,standard
3020,2025-10-03,IT,Raton Click Feliz,5,14.0,paid,standard
3021,2025-10-04,ES,Teclado RGB Hacker,3,25.0,cancelled,express
3022,2025-10-04,FR,USB-C Hub Por si acaso,1,31.0,paid,standard
3023,2025-10-04,ES,Monitor 27p 4K para plots,1,182.0,paid,standard
3024,2025-10-05,DE,Portatil Modo Kaggle,1,660.0,paid,express
3025,2025-10-05,ES,Raton Click Feliz,2,15.0,paid,express
3026,2025-10-05,UK,Taza Yo <3 Data,2,12.0,paid,standard
3027,2025-10-06,ES,Raton Click Feliz,1,15.0,paid,standard
3028,2025-10-06,FR,Portatil Modo Kaggle,1,652.0,cancelled,express
3029,2025-10-06,PT,USB-C Hub Por si acaso,1,30.5,paid,standard
3030,2025-10-06,IT,Monitor 27p 4K para plots,1,176.0,paid,standard
````

**Comprobación**

* ~30 filas, `status` con `paid` y `cancelled`.

---

## 3) Mini exploración (Notebook) — **al principio**

Crea **`notebooks/01_exploracion.ipynb`** con **seis celdas**. A continuación tienes **snippets incompletos** (rellena los `TODO`/`...`). No cambies el orden.

### Celda 1 — Imports y carga

Objetivo: importar librerías, cargar CSV parseando fechas, ver 5 filas y dtypes.

```python
# Celda 1 — Imports y carga
import pandas as pd
import matplotlib.pyplot as plt

# Ruta relativa desde /notebooks a /data/raw
csv_path = ...  # p. ej.: "../data/raw/orders_sample.csv"

# Carga parseando la columna de fecha
df = pd.read_csv(..., parse_dates=[...])  # TODO: completa argumentos

# Vistazo rápido
...  # mostrar 5 filas
...  # mostrar dtypes
```


---

### Celda 2 — Conteos y columna derivada

Objetivo: distribuciones y columna `order_total`.

```python
# Celda 2 — Conteos y columna derivada
# Conteo de estados y países
status_counts = ...      # TODO: value_counts sobre df["status"]
country_counts = ...     # TODO: value_counts sobre df["country"]

# Crear columna order_total = units * unit_price
df["order_total"] = ...  # TODO: operación vectorizada

# Vista de algunas columnas clave
df[[..., ..., "order_total"]].head()  # TODO: selecciona columnas
```

**Pistas:** operaciones por columna tipo `df["a"] * df["b"]`.

---

### Celda 3 — Gráfica 1: ingresos diarios (solo paid)

Objetivo: filtrar `paid`, agrupar por fecha y sumar `order_total`, graficar barras.

```python
# Celda 3 — Ingresos diarios (paid)
df_paid = df[ ... ] .copy()  # TODO: condición por status

daily_rev = df_paid.groupby(...)[ ... ].sum()  # TODO: agrupa por "date" y suma "order_total"

ax = daily_rev.plot(kind="bar", title="Ingresos diarios (solo paid)")
ax.set_xlabel("Fecha")
ax.set_ylabel("Ingresos")
plt.tight_layout()
plt.show()
```


---

### Celda 4 — Gráfica 2: pedidos por país (solo paid)

Objetivo: conteos por país en subset `paid` y gráfico de barras.

```python
# Celda 4 — Pedidos por país (paid)
paid_country_counts = df_paid[ ... ].value_counts()  # TODO: columna país

ax = paid_country_counts.plot(kind="bar", title="Pedidos por país (paid)")
ax.set_xlabel("País")
ax.set_ylabel("Nº pedidos")
plt.tight_layout()
plt.show()
```


---

### Celda 5 — Filtros + KPIs manuales

Objetivo: aplicar rango de fechas + país y calcular KPIs solo sobre `paid`.

```python
# Celda 5 — Filtros + KPIs manuales
start = "una fecha"   # puedes cambiarlo
end   = "otra fecha"   # puedes cambiarlo
country = "codigo del pais"         # puedes cambiarlo

mask = (
    (df["date"] >= pd.to_datetime(...)) &   # TODO: start
    (df["date"] <= pd.to_datetime(...)) &   # TODO: end
    (df["country"] == ...)                  # TODO: país
)
sub = df[mask].copy()
sub_paid = sub[ sub["status"] == ... ].copy()   # TODO: paid (aprovecha para fijarte como funciona una mascara)

num_orders = ...  # TODO: nº filas
total_revenue = ...  # TODO: suma de units * unit_price en sub_paid
avg_order_value = ...  # TODO: media condicionada (cuidado con 0 pedidos)

(num_orders, total_revenue, avg_order_value)
```



---

### Celda 6 — Markdown: Reglas acordadas

Escribe (sin código) las reglas oficiales que usarás en el script:

* Filtros aplicables (`start`, `end`, `country`).
* KPIs **solo con `status="paid"`**.
* Redondeos (p. ej., 2 decimales).
* Si `num_orders==0`, `avg_order_value = 0.0`.

---

## 4) CLI — construcción del script

Crea **`src/sales_cli.py`**. Completa los bloques en orden..

### 4.1 Esqueleto y argumentos — *principio del script*

Objetivo: definir argumentos y verlos por pantalla (temporalmente).

```python
#!/usr/bin/env python3
import argparse
import sys
import json
from pathlib import Path
import pandas as pd

def main():
    parser = argparse.ArgumentParser(
        description="Filtra pedidos y genera un resumen de KPIs."
    )
    # TODO: añade argumentos:
    # --input (obligatorio), --outdir (por defecto 'outputs'),
    # --start, --end, --country,
    # --summary-format (choices: txt, json; default=txt),
    # --export-filtered (flag)

    ### ...AÑADE 6 ARGUMENTOS AQUI COMO ESE DE ABAJO

    parser.add_argument("--export-filtered", action="store_true",
                        help="Guardar CSV con pedidos filtrados.")

    args = parser.parse_args()
    print("[INFO] Args:", args)  # TEMP: borra al finalizar

    # TODO: el resto del script irá aquí

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**Prueba** ↓↓↓

```bash
python3 src/sales_cli.py --help
python3 src/sales_cli.py --input data/raw/orders_sample.csv
```

---

### 4.2 Validaciones y rutas — *parte media*

Objetivo: validar entrada y preparar carpeta de salida.

**NOTA** la clase Path transforma una ruta string en un objeto con metodos para trabajar con rutas, ficheros, folders, etc...

```python
in_path = Path(...)      # TODO: desde args
outdir = Path(...)       # TODO: desde args

if not in_path.exists():
    print(f"[ERROR] No existe el fichero: {in_path}", file=sys.stderr)
    sys.exit(1)

outdir.mkdir(parents=True, exist_ok=True)
print(f"[INFO] outdir listo en {outdir}")
```

---

### 4.3 Carga del CSV — *parte media*

Objetivo: leer CSV parseando fechas, manejar errores.

```python
try:
    df = pd.read_csv # TODO: columna fecha CARGAMOS EL DATASET 
except Exception as e:
    print(f"[ERROR] Al leer CSV: {e}", file=sys.stderr) #POSIBLES FALLOS DE SEPARADOR, ENCODING, ETC...
    sys.exit(2)

print("[INFO] filas cargadas:", ...)  # TODO: nº de filas
```

---

### 4.4 Filtros opcionales — *parte media*

Objetivo: aplicar `--start`, `--end`, `--country` si se pasan.

```python
if args.start:
    df = df[ df["date"] >= pd.to_datetime(...) ]   # TODO
if args.end:
    df = df[ df["date"] <= pd.to_datetime(...) ]   # TODO
if args.country:
    df = df[ df["country"].str.upper() == ... ]    # TODO: normaliza comparación

print("[INFO] filas tras filtros:", ...)  # TODO: nº de filas
```

---

### 4.5 Cálculo de KPIs — *parte media (función + llamada)*

Objetivo: encapsular reglas de KPIs dentro de una función.

```python
def compute_kpis(df: pd.DataFrame) -> dict:
    """
    Aplica reglas acordadas en el Notebook:
    - Solo status == "paid"
    - num_orders, total_revenue, avg_order_value
    - Redondeo a 2 decimales cuando proceda
    """
    df_paid = df[ df["status"] == ... ].copy()  # TODO
    num_orders = ...                            # TODO
    total_revenue = ...                         # TODO: suma de units*unit_price
    avg_order_value = ...                       # TODO: evita división por 0
    return {
        "num_orders": ... ,                     # TODO: int
        "total_revenue": ... ,                  # TODO: round(..., 2)
        "avg_order_value": ... ,                # TODO: round(..., 2)
    }

kpis = compute_kpis(df)
print("[INFO] KPIs:", kpis)
```

---

### 4.6 Exportar resumen — *parte final*

Objetivo: escribir TXT o JSON en `outdir` con metadatos y KPIs.

```python
summary_path = None
if args.summary_format == "txt":
    summary_path = outdir / "summary.txt"
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("=== Sales Summary ===\n")
        f.write(f"Input: {in_path}\n")
        # TODO: si hay filtros, escríbelos en una línea
        # TODO: escribe cada KPI en su propia línea
else:
    summary_path = outdir / "summary.json"
    payload = {
        "input": ... ,     # TODO: str(in_path)
        "filters": {
            "start": ... , # TODO
            "end": ... ,
            "country": ...
        },
        "kpis": ...        # TODO: el dict de KPIs
    }
    with summary_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"[OK] Resumen guardado en {summary_path}")
```

---

### 4.7 Exportar pedidos filtrados — *parte final (opcional)*

Objetivo: guardar el subset final si se solicita.

```python
if args.export_filtered:
    filtered_path = outdir / "filtered.csv"
    df.to_csv(filtered_path, index=..., encoding="utf-8")  # TODO: index False
    print(f"[OK] Filtrado guardado en {filtered_path}")
```

---

### 4.8 Códigos de salida — *final del script*

Objetivo: usar códigos coherentes.

* `sys.exit(1)` si falta el fichero,
* `sys.exit(2)` si falla la lectura,
* `sys.exit(0)` si todo OK (ya presente al final del `main`).

---

## 5) Comandos de prueba 

```bash
# Ayuda
python3 src/sales_cli.py --help

# Sin filtros, resumen TXT
python3 src/sales_cli.py --input data/raw/orders_sample.csv

# JSON + filtros
python3 src/sales_cli.py --input data/raw/orders_sample.csv \
  --start 2025-10-01 --end 2025-10-03 --country ES --summary-format json

# Exportar filtrados
python3 src/sales_cli.py --input data/raw/orders_sample.csv \
  --country FR --export-filtered
```

**Qué verificar**

* Se crea `outputs/` cuando hace falta.
* Cambia el nº de filas tras filtros.
* El resumen (TXT/JSON) refleja filtros y KPIs correctos.

---

## 6) Checklist de aceptación (auto-evaluación)
COMPRUEBA QUE LO HAS HECHO TODO

**Entorno y repo**

* [ ] Entorno conda y dependencias instaladas desde `requirements.txt`.
* [ ] Repo Git inicializado y conectado a GitHub.

**Datos y Notebook**

* [ ] CSV en `data/raw/` con ~30 filas.
* [ ] Notebook con:

  * [ ] 2 gráficas (ingresos diarios y pedidos por país con `paid`),
  * [ ] Reglas explicadas en Markdown,
  * [ ] KPIs manuales probados con al menos **dos** combinaciones de filtros.

**Script CLI**

* [ ] Acepta argumentos (`--help` funcional).
* [ ] Valida rutas y crea `outputs/`.
* [ ] Aplica filtros de fecha/país.
* [ ] Calcula KPIs solo con `paid`.
* [ ] Genera resumen TXT/JSON con metadatos.
* [ ] Exporta filtrados si se pide.
* [ ] Usa códigos de salida coherentes (0/1/2).

---

## 7) Notas, pistas y trucos

* Ejecuta desde la **raíz** del proyecto para que las rutas relativas encajen.
* Fechas en formato `YYYY-MM-DD`; usa `pd.to_datetime(...)` para comparar.
* Redondea a 2 decimales `total_revenue` y `avg_order_value`.
* Si no hay `paid`, define `avg_order_value = 0.0` para evitar divisiones por cero.
* Normaliza `country` a mayúsculas para comparar (`.str.upper()`). # o a lower!
* Para ver el **exit code** (Linux/macOS): justo después del comando, `echo $?`.

**BONUS:** Incluye logs
> **Tip de depuración**: logs `[INFO]` entre fases (carga → filtros → KPIs → export).
