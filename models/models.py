from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, MetaData, Table

# Определяем метаданные
metadata = MetaData()

# Таблица владельцев (owners)
owners = Table(
    'owners', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('phone_number', String(20), nullable=False),
    Column('email', String(100), nullable=False),
    Column('address', String(255), nullable=False)
)

# Таблица животных (animals)
animals = Table(
    'animals', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('species', String(100), nullable=False),
    Column('breed', String(100), nullable=False),
    Column('age', Integer, nullable=False),
    Column('owner_id', Integer, ForeignKey('owners.id'), nullable=False)
)

# Таблица устройств GPS-трекеров (devices)
devices = Table(
    'devices', metadata,
    Column('id', Integer, primary_key=True),
    Column('serial_number', String(100), nullable=False),
    Column('animal_id', Integer, ForeignKey('animals.id'), nullable=False)
)

# Таблица GPS-данных (gps_data)
gps_data = Table(
    'gps_data', metadata,
    Column('id', Integer, primary_key=True),
    Column('animal_id', Integer, ForeignKey('animals.id'), nullable=False),
    Column('latitude', Float, nullable=False),
    Column('longitude', Float, nullable=False),
    Column('timestamp', DateTime, nullable=False)
)

# Таблица оповещений (alerts)
alerts = Table(
    'alerts', metadata,
    Column('id', Integer, primary_key=True),
    Column('animal_id', Integer, ForeignKey('animals.id'), nullable=False),
    Column('message', String(255), nullable=False),
    Column('created_at', DateTime, nullable=False)
)


