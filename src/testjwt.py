from jose import jwt

SECRET_KEY = "kD7vP1mN9xTqA4zWsU2eRbGhJcYl0oMf"
ALGORITHM = "HS256"

data = {"sub": "user1@example.com"}
token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
print("Token:", token)

decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print("Decoded:", decoded)
