from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {
        'foo': 'bar'
    }

@app.get("/urls")
def get_all_urls():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list

app2 = FastAPI()

@app2.get("/health-check")
def healthcheck():
    return {
        'status': 'OK'
    }


def main():
    pass
    
if __name__ == "__main__":
    main()