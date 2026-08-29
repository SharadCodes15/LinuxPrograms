from app import Viewer

DB_NAME = "sample_store.db"

app = Viewer(DB_NAME)
try:
    tables = app.get_tables()
    print(f"\n=== Tables in {DB_NAME} ===")
    if tables:
        for table in tables:
            print(table)
    else:
        print("No tables found")

    result = app.get_table_data(tables)
    print("\n=== Data ===")
    print(result)
except Exception as e:
    print(f"Error: {e}")
finally:
    app.close()