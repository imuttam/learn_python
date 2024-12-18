import psycopg2

# Database connection parameters
db_user = "postgres"
db_password = "xxxxx"  # Replace with your actual password
db_host = "localhost"  # or your database host
db_port = "5432"       # default PostgreSQL port
db_name = "kpi"

# Create table script
create_table_query = """
CREATE TABLE IF NOT EXISTS tcs_kpi (
    date DATE PRIMARY KEY,
    location NUMERIC,
    total_data_volum NUMERIC,
    total_volte_traffic NUMERIC,
    avg_data_per_site NUMERIC,
    avg_volte_per_site NUMERIC,
    count_50_gb_plus NUMERIC,
    count_20_to_50_gb NUMERIC,
    count_1_to_20_gb NUMERIC,
    count_0_to_1_gb NUMERIC,
    count_0 NUMERIC,
    count_volte_less_1 NUMERIC,
    max_active_users NUMERIC,
    enb_nw_av_perc NUMERIC,
    avg_rrc_con_sr NUMERIC,
    avg_cssr_perc NUMERIC,
    avg_cssr_volte_perc NUMERIC,

    avg_erab_sr_perc NUMERIC,
    avg_erab_volte_sr_perc NUMERIC,
    avg_csfb_sr_perc NUMERIC,
    avg_ps_ho_perc NUMERIC,
    avg_irat_ho_sr_perc NUMERIC,
    avg_drop_call_rate NUMERIC,
    avg_erab_drop_perc NUMERIC
);
"""

# Connect to the database and execute the creation script
try:
    # Establish connection
    conn = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port
    )
    cursor = conn.cursor()
    
    # Execute the creation query
    cursor.execute(create_table_query)
    conn.commit()
    print("Table 'tcs_kpi' created successfully.")
    
except Exception as e:
    print(f"Error occurred: {e}")
    
finally:
    # Close the connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
