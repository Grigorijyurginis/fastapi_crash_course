from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, drop_tables
from routers import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print('бд очищена')
    await create_tables()
    print('бд создана')
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
