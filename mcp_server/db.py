import aiosqlite

from pathlib import Path



database = "mcp_database.db"
table = """
CREATE TABLE IF NOT EXISTS Session (
    access_token TEXT NOT NULL
);

"""



# creating a connection and closing

async def init_db():
    try:
        base_directory = Path("/home/tupac/abdo-toggle/toggle-mcp/mcp_database.db")
        base_directory.touch()

        async with aiosqlite.connect(str(base_directory)) as conn:
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
            cursor = conn.cursor()
            await cursor.execute(table)
            await conn.commit()
    except aiosqlite.Error as e:
        print("Failed to open database:", e)









