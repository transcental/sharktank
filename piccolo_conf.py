from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from sharktank.config import config

DB = PostgresEngine(
    config={"dsn": config.database_url.encoded_string()},
    auto_create_extensions=False
)

APP_REGISTRY = AppRegistry(apps=["sharktank.piccolo_app"])
