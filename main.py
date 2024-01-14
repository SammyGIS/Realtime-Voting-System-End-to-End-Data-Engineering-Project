import psycopg2


def create_tables (conn, cur):

    curr.execute(
        """
        CREATE TABLE IF  NOT EXISTS candidates(
        candidate_id VARCHAR(255) PRIMARY KEY,
        candidtae_name VARCHAR (255),
        party_affliation VARCHAR(255),
        biography TEXT,
        cmapaign_platform TEXT,
        photo_url TEXT
        )
""")
    
    
if __name__ == '__main__':

    try:
        conn = psycopg2.connect(
            "host=localhost dbname=voting ucer=postgres password=postgres"
        )

        curr = conn.cursor()

        cur= conn.cursor()


    except Exception as e:
        print(e)

