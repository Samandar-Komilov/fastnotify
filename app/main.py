import os
import aioredis
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette_admin.contrib.sqla import Admin, ModelView

from app.core.database import engine
from app.models import User

load_dotenv()


app = FastAPI()


admin = Admin(engine, title="Example: SQLAlchemy")

# Add view
admin.add_view(ModelView(User))

# Mount admin to your app
admin.mount_to(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", reload=True)