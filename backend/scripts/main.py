import uvicorn

from ml_models import config
from ml_models.bootstrap import create_app

app = create_app(config)

if __name__ == "__main__":
    uvicorn.run(app=app, use_colors=True)
