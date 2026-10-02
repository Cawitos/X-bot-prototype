import os

X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")

# Usernames (sin @) que nunca pueden ganar, sin importar lo que comenten.
# Se puede configurar por variable de entorno BLACKLISTED_USERS="user1,user2,user3"
BLACKLISTED_USERS = set(
    u.strip().lower().lstrip("@")
    for u in os.getenv("BLACKLISTED_USERS", "").split(",")
    if u.strip()
)