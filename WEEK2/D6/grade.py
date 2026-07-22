from fastapi import FastAPI

app = FastAPI()

@app.get("/grade/{mark}")
def get_grade(mark: int):
    if mark >= 90:
        return {"grade": "A"}
    elif mark >= 80:
        return {"grade": "B"}
    elif mark >= 70:
        return {"grade": "C"}
    elif mark >= 60:
        return {"grade": "D"}
    elif mark >= 50:
        return {"grade": "E"}
    else:
        return {"grade": "F"}