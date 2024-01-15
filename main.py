import psycopg2
import requests
import random


BASE_URL = 'https://randoomuser.me/api/?nat=gb'
PARTIES = ["Management_Party", "Saviour Party", ]

random.seed(21)

def create_tables (conn, cur):

    cur.execute(
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
    
    cur.execute("""
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
    cur.execute("""
        CREATE TABLE IF NOT EXISTS votes(
                 voter_id VARCHAR(255) UNIQUE,
                 candidate_id VARCHAR(255),
                 voting_time TIMESTAMP,
                 vote INT DEFAULT 1,
                 primary key (vote_id, candiate_id)
       
        """)
    
def generate_candidate_data(candiate_number, total_parties):
    response = requests.get(BASE_URL+'&gender=' + ('female' if candidate_number %2 == 1 else 'male')):
    if response.status_code == 200:
        user_data = response.json()['results'][0]


        return {
            'candiate_id':user_data['login']['uuid'],
            'candidate_name': f"user_data['name']['first]"
        }


    

if __name__ == '__main__':

    try:
        conn = psycopg2.connect(
            "host=localhost dbname=voting user=postgres password=postgres"        )

        cur = conn.cursor()

        create_tables(conn,cur)

        cur.execute("""
            SELECT * FROM candidates        
                    """)
        
        candidates = cur.fetchall()
        print(candidates)

        if len(candidates) ==0:
            for i in range(3):
                candidate = generate_candidate_data(i, total_parties=3)

    except Exception as e:
        print(e)

