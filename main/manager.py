from main import app, db
from flask_migrate import Migrate, migrate #, MigrateCommand


migrates = Migrate(app, db)

if __name__ == '__main__':
    # Crea el directorio de migraciones
    migrates.init_app(app, db)

    # Genera una migración inicial
    migrate()

    # Aplica las migraciones a la base de datos
    #migrate.upgrade()