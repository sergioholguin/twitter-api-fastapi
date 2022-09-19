
import time
from fastapi import Request


# Middleware
async def process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    process_time = end_time - start_time

    response.headers["X-Process-Time"] = str(process_time)
    return response
