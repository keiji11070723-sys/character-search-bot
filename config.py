import os

TOKEN = os.getenv("DISCORD_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

print("TOKEN:", "OK" if TOKEN else "NG")
print("DB:", "OK" if DATABASE_URL else "NG")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN が設定されていません。")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL が設定されていません。")