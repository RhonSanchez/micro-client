from entities.model import Client
from datasource.db_session import orm_session

def insert(client:Client)->bool:
    with orm_session() as orm:
        if Client:
            orm.add(client)
            orm.commit()
            return True
        
def select_all()->list:
    with orm_session() as orm:
        result=orm.query(Client).all()
        return result
    
def select_by_id(id:int)->Client:
    with orm_session() as orm:
        search = orm.query(Client).filter(Client.id == id).first()
        return search
    
def delete_by_id(id:int)->bool:
    with orm_session() as orm:
        result = orm.query(Client).filter(Client.id == id).delete()
        orm.commit()
        return result>0
    
def update(client:Client)->bool:
    with orm_session() as orm:
        result=orm.query(Client).filter(Client.id==client.id).update({
            Client.name:client.name,
            Client.address:client.address,
            Client.email:client.email,
        })
        orm.commit()
        return result>0