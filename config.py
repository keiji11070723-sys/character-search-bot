import os

# Discord Bot Token
TOKEN = os.getenv("DISCORD_TOKEN")

# Railway PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

# 起動時チェック
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN が設定されていません。")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL が設定されていません。")