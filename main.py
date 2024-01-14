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
    
    curr.execute("""
        CREATE TBALE IF NOT EXISTS voters(
                 voter_id VARCHAR(255) PRIMAR KEY,
                 voter_name VARCHAR (255),
                 date_of_birth DATE,
                 gender VARCHAR(255),
                 nationality VARCHAR (255),
                 registration_number VARCHAR(255),
                 address_street VARCHAR(255),
                 address_city VARCHAR(255),
                 address_state VARCHAR (255),
                 address_country VARCHAR(255),
                 address_postcode VARCHAR(255),
                 email VARCHAR (255),
                 phone_number VARCHAR(255),
                 picture TEXT,
                 registered_age INTEGER

                )
        """)
    curr.execute("""
        CREATE TABLE IF NOT EXISTS votes(
                 voter_id VARCHAR(255) UNIQUE,
                 candidate_id VARCHAR(255),
                 voting_time TIMESTAMP,
                 vote INT DEFAULT 1,
                 primary key (vote_id, candiate_id)
       
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

