# AI Log - Equipo Guayaberos

## Herramientas
- Gemini

## Filosofía de uso
Decidimos usar la guia como maestro y para tareas repetitivas, 
debido a que nuestro equipo no estaba acostumbrado a todas las tecnologias. 
Ni implementaciones
## Registro de uso 

### 2026-03-22 | Gemini | Depuración de ETL y Gestión de Dependencia
- **Tarea**: Le pedimos que nos ayudara con un error en las conexiones entre las bases sqlite
  y nuestro codigo para leer los ex proporcionado por la Inegi.
- **Prompt**: "[Código del script] + Error sqlite3.DatabaseError: database disk image is malformed +
  ModuleNotFoundError: No module named 'openpyxl'"
- **Resultado**: Sugerencia de implementar executemany y un único commit al final del proceso,
  en lugar de realizar transacciones individuales por cada celda.
- **Decisión**: Nos ayudo a cambiar nuesto sistema de recolección de datos lo cual
  fue escensial para el resto de tablas.

### 2026-04-05 | Gemini | Optimización
- **Tarea**: Reducir el tiempo de ejecución y prevenir la corrupción de la base de datos durante la carga masiva.
- **Prompt**: "Mi script inserta fila por fila y marca error de base de datos malformada, ¿cómo lo hago más seguro?"
- **Resultado**: Nos ayudo a ver lo errores al momento de incrustar los datos.
- **Decisión**: Nos ayudo a cambiar nuesto sistema de recolección de datos lo cual
  fue escensial para el resto de tablas.

### NO usamos IA para hacer lo siguiente:
- La selección de las ODS.
- La narrativa del tablero (redacción propia)
