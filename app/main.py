from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from core.database import async_engine, Base
from api.auth import auth_router
from api.users import user_router
from api.admin import admin_router

import uvicorn
import uvloop

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await async_engine.dispose()

app = FastAPI(lifespan=lifespan, title="Advertisement Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors()},
    )

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(admin_router)

if __name__ == '__main__':
    # from core.database import async_engine, Base
    # import asyncio
    #
    #
    # async def reset_db():
    #     async with async_engine.begin() as conn:
    #         await conn.run_sync(Base.metadata.drop_all)
    #         await conn.run_sync(Base.metadata.create_all)
    #
    #
    # asyncio.run(reset_db())
    uvloop.install()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)