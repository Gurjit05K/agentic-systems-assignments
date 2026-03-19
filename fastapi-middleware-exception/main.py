from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Middleware & Exception Handling Demo",
    description="Assignment for logging requests and custom 404 handling"
)


@app.get("/hello")
async def hello():
    return {"message": "Hello, Welcome to FastAPI!"}


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    # Print BEFORE the request is processed
    print(f"➡️ Incoming Request: {request.method} {request.url.path}")
    
    # Process the request
    response = await call_next(request)
    
    # Print AFTER the response is returned
    print(f"⬅️  Response Sent: {response.status_code} for {request.url.path}")
    
    return response


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "The requested resource was not found"}
    )


# Optional: Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Welcome to the Middleware Assignment!"}