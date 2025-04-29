from flask import Flask
from models import db, User, People, Planets, Favorite
import os

app = Flask(__name__)
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    # Crear todas las tablas
    db.create_all()

    # ---------- Poblar USERS ----------
    user1 = User(email='luke@jedi.com', password='force123', is_active=True)
    user2 = User(email='leia@rebellion.org', password='hope456', is_active=True)

    db.session.add_all([user1, user2])
    db.session.commit()

    # ---------- Poblar PEOPLE ----------
    p1 = People(name='Luke Skywalker', height='172', mass='77', hair_color='Blond', skin_color='Fair')
    p2 = People(name='Darth Vader', height='202', mass='136', hair_color='None', skin_color='White')

    db.session.add_all([p1, p2])
    db.session.commit()

    # ---------- Poblar PLANETS ----------
    pl1 = Planets(name='Tatooine', diameter='10465', rotation_period='23', orbital_period='304', gravity='1 standard', population='200000')
    pl2 = Planets(name='Alderaan', diameter='12500', rotation_period='24', orbital_period='364', gravity='1 standard', population='2000000000')

    db.session.add_all([pl1, pl2])
    db.session.commit()

    # ---------- Poblar FAVORITES ----------
    f1 = Favorite(user_id=user1.id, people_id=p1.id)
    f2 = Favorite(user_id=user1.id, planet_id=pl1.id)
    f3 = Favorite(user_id=user2.id, planet_id=pl2.id)

    db.session.add_all([f1, f2, f3])
    db.session.commit()

    print("✅ Base de datos poblada exitosamente.")
