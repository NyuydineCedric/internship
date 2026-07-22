from fastapi import FastAPI

app = FastAPI()

@app.get("/table/{num}")
def multiplication_table(num: int):
    table = []

    for i in range(1, 11):
        table.append(f"{num} x {i} = {num * i}")

    return {"table": table}