from sqlalchemy import create_engine

# db_connection_string =  "mysql+pymysql://root:VivekMuski@2024@localhost/db?host=localhost?port=3306"

engine = create_engine(
      "mysql+pymysql://root:VivekMuski@2024@localhost/db?host=localhost?port=3306")

with engine.connect() as conn:
      result = conn.execute(text("select * from register_data"))
      print(result.all())