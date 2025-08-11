from db import connection

def create_table():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS motores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                motor TEXT NOT NULL,
                lado TEXT,
                quantidade INTEGER,
                status TEXT
            )
        '''
    )
    
    conn.commit()

def insert_items(dados):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
            INSERT INTO motores 
            (
                motor,
                lado,
                quantidade,
                status
            )
            VALUES 
            (
                ?,
                ?,
                ?,
                ?
            )
        ''', dados
    )

    conn.commit()

def get_items():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT * FROM motores
        """
    )

    result = cursor.fetchall()

    return [
        { 'motor':row[1], 'lado':row[2], 'quantidade':row[3], 'status':row[4]}
        for row in result
    ]

def update_status():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE motores SET status = ?
        
        """
        
    )

    
