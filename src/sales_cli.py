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
    parser.add_argument("--input", required= True,
                        help="Ruta CSV.")
    parser.add_argument("--outdir", default ="output",
                        help="Ruta de salida")
    parser.add_argument("--start",
                        help="Fecha de inicio")
    parser.add_argument("--end",
                        help="Fecha de salida")
    parser.add_argument("--country",
                        help="Pais")
    parser.add_argument("--summary-format", choices = ["txt", "json"], default="txt",
                        help = "Tipo de formato")
    parser.add_argument("--export-filtered", action="store_true",
                        help="Guardar CSV con pedidos filtrados.")

    args = parser.parse_args()
    print("[INFO] Args:", args)  # TEMP: borra al finalizar

    # TODO: el resto del script irá aquí
    in_path = Path(args.input)      # TODO: desde args
    outdir = Path(args.outdir)      # TODO: desde args
    if not in_path.exists():
        print(f"[ERROR] No existe el fichero: {in_path}", file=sys.stderr)
        sys.exit(1)

    outdir.mkdir(parents=True, exist_ok=True)
    print(f"[INFO] outdir listo en {outdir}")
    try:
        df = pd.read_csv(in_path, parse_dates=["date"]) # TODO: columna fecha CARGAMOS EL DATASET 
    except Exception as e:
        print(f"[ERROR] Al leer CSV: {e}", file=sys.stderr) #POSIBLES FALLOS DE SEPARADOR, ENCODING, ETC...
        sys.exit(2)
    print("[INFO] filas cargadas:", df.shape[0])  # TODO: nº de filas
    if args.start:
        df = df[ df["date"] >= pd.to_datetime(args.start) ]   # TODO
    if args.end:
        df = df[ df["date"] <= pd.to_datetime(args.end) ]   # TODO
    if args.country:
        df = df[ df["country"].str.upper() == args.country ]    # TODO: normaliza comparación

    print("[INFO] filas tras filtros:", df.shape[0])  # TODO: nº de filas
    def compute_kpis(df: pd.DataFrame) -> dict:
        """
        Aplica reglas acordadas en el Notebook:
        - Solo status == "paid"
        - num_orders, total_revenue, avg_order_value
        - Redondeo a 2 decimales cuando proceda
        """
        df_paid = df[df["status"] == "paid"].copy()  # TODO
        num_orders = df_paid["country"].count()                           # TODO
        total_revenue = (df_paid["units"]*df_paid["unit_price"]).sum()                       # TODO: suma de units*unit_price
        avg_order_value = round(total_revenue/num_orders, 2) if num_orders > 0 else 0.0   
        avg_order_value = avg_order_value               # TODO: evita división por 0
        return {
            "num_orders": int(num_orders),                     # TODO: int
            "total_revenue":float(total_revenue),                  # TODO: round(..., 2)
            "avg_order_value": float(avg_order_value),                # TODO: round(..., 2)
        }

    kpis = compute_kpis(df)
    
    print("[INFO] KPIs:", kpis)
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
            "input": str(in_path) ,     # TODO: str(in_path)
            "filters": {
                "start": args.start , # TODO
                "end": args.end,
                "country": args.country,
            },
            "kpis": kpis        # TODO: el dict de KPIs
        }
        with summary_path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"[OK] Resumen guardado en {summary_path}")
    if args.export_filtered:
        filtered_path = outdir / "filtered.csv"
        df.to_csv(filtered_path, index=False, encoding="utf-8")  # TODO: index False
        print(f"[OK] Filtrado guardado en {filtered_path}")
    sys.exit(0)
if __name__ == "__main__":
    main()
