import pandas as pd
import numpy as np
import psycopg2
import os

# Database connection parameters
db_user = "postgres"
db_password = "xxxxx"  # Replace with your actual password
db_host = "localhost"  # or your database host
db_port = "5432"       # default PostgreSQL port
db_name = "kpi"

file_path= None
files = os.listdir()

for file in files:
    if file.endswith('xlsx'):
        file_path=file
        

        # File details
        # file_path = 'EZ_Jharkhand_RAN_KPI_Phase_2_daily_30_11_2024.xlsx'
        sheet_name = 'RAN KPI Report Phase2'
        header_column = 'LOCATION'

        # Extract report date
        file_new = file_path.replace('_', '-')
        file_date = file_new.split('daily-')[1].split('.')[0]
        report_date = pd.to_datetime(file_date, format='%d-%m-%Y').date()

        try:
            # Load the data
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            location = df[header_column].nunique()
            # Ensure numeric columns are handled properly
            df['Data Volume - Total (GB)'] = pd.to_numeric(df['Data Volume - Total (GB)'], errors='coerce')
            df['VOLTE Traffic (Erlang)'] = pd.to_numeric(df['VOLTE Traffic (Erlang)'], errors='coerce')

            # Calculate metrics
            unique_values = df[header_column].nunique()
            total_data_volume = df['Data Volume - Total (GB)'].sum()
            total_data_volume = round(total_data_volume,2)

            total_volte_traffic = df['VOLTE Traffic (Erlang)'].sum()
            total_volte_traffic = round(total_volte_traffic, 2)

            avg_data_per_site = total_data_volume / unique_values
            avg_data_per_site = round(avg_data_per_site,2)

            avg_volte_per_site = total_volte_traffic / unique_values
            avg_volte_per_site = round(avg_volte_per_site,2)

            location_sums = df.groupby('LOCATION')['Data Volume - Total (GB)'].sum().reset_index()
            count_50_gb_plus = location_sums[location_sums['Data Volume - Total (GB)'] > 50].count()['LOCATION']
            count_20_to_50_gb = location_sums[(location_sums['Data Volume - Total (GB)'] > 20) & (location_sums['Data Volume - Total (GB)'] <= 50)].count()['LOCATION']
            count_1_to_20_gb = location_sums[(location_sums['Data Volume - Total (GB)'] > 1) & (location_sums['Data Volume - Total (GB)'] <= 20)].count()['LOCATION']
            count_0_to_1_gb = location_sums[(location_sums['Data Volume - Total (GB)'] > 0) & (location_sums['Data Volume - Total (GB)'] <= 1)].count()['LOCATION']
            count_0 = location_sums[location_sums['Data Volume - Total (GB)'] == 0].count()['LOCATION']

            location_volte = df.groupby('LOCATION')['VOLTE Traffic (Erlang)'].sum().reset_index()
            count_volte_less_1 = location_volte[location_volte['VOLTE Traffic (Erlang)'] < 1].count()['LOCATION']

            df['QCI1'] = pd.to_numeric(df['MAX ACTIVE Users (DL) -QCI1'], errors='coerce')
            df['QCI6'] = pd.to_numeric(df['MAX ACTIVE Users (DL) -QCI6'], errors='coerce')
            df['QCI8'] = pd.to_numeric(df['MAX ACTIVE Users (DL) -QCI8'], errors='coerce')
            df['QCI9'] = pd.to_numeric(df['MAX ACTIVE Users (DL) -QCI9'], errors='coerce')
            max_active_users = df['QCI1'].sum() + df['QCI6'].sum() + df['QCI8'].sum() + df['QCI9'].sum()

            df['E-UTRAN Cell availability (%)'] = pd.to_numeric(df['E-UTRAN Cell availability (%)'], errors='coerce')
            enb_nw_av_perc = df['E-UTRAN Cell availability (%)'].mean()
            enb_nw_av_perc = round(enb_nw_av_perc,2)

            rrc_attempt = pd.to_numeric(df['RRC Connection Attempts(All)'], errors='coerce')
            rrc_success = pd.to_numeric(df['Successful RRC connection attempts'], errors='coerce')
            avg_rrc_con_sr = (rrc_attempt.sum()-rrc_success.sum())/rrc_attempt.sum()
            avg_rrc_con_sr = round(100-avg_rrc_con_sr*100,2)
            
            df['CSSR'] = pd.to_numeric(df['CSSR'], errors='coerce')
            avg_cssr_perc = df['CSSR'].mean()
            avg_cssr_perc = round(avg_cssr_perc,2)

            df['CSSR VOLTE'] = pd.to_numeric(df['CSSR VOLTE'], errors='coerce')
            avg_cssr_volte_perc = df['CSSR VOLTE'].mean()
            avg_cssr_volte_perc = round(avg_cssr_volte_perc,2)

            erab_attempt = pd.to_numeric(df['ERAB Setup Attempts'], errors='coerce')
            erab_success = pd.to_numeric(df['Successful ERAB setup attempts'], errors='coerce')
            avg_erab_sr_perc = erab_success.sum()/erab_attempt.sum()
            avg_erab_sr_perc = round(avg_erab_sr_perc*100, 2)

            erab_volte_attempt = pd.to_numeric(df['ERAB Setup Attempts(VOLTE)'], errors='coerce')
            erab_volte_success = pd.to_numeric(df['Successful ERAB Setup Attempts(VOLTE)'], errors='coerce')
            avg_erab_volte_sr_perc = (erab_volte_attempt.sum()-erab_volte_success.sum())/erab_volte_attempt.sum()
            avg_erab_volte_sr_perc = round(100-avg_erab_volte_sr_perc*100, 2)

            csfb_attempt = pd.to_numeric(df['CSFB Preparation attempt'], errors='coerce')
            csfb_success = pd.to_numeric(df['Successful CSFB Preparation'], errors='coerce')
            avg_csfb_sr_perc = (csfb_attempt.sum()-csfb_success.sum())/csfb_attempt.sum()
            avg_csfb_sr_perc = round(100-avg_csfb_sr_perc*100,2)

            ps_ho_attempt = pd.to_numeric(df['PS handover attempts(LTE intra system)'], errors='coerce')
            ps_ho_success = pd.to_numeric(df['Successful PS HO attempts (LTE Intra System)'], errors='coerce')
            avg_ps_ho_perc = ps_ho_success.sum()/ps_ho_attempt.sum()
            avg_ps_ho_perc = round(avg_ps_ho_perc*100, 2)

            geran_ho_attempt = pd.to_numeric(df['Inter RAT HO Out Attempts(GERAN)'], errors='coerce')
            geran_ho_success = pd.to_numeric(df['Successful Inter RAT HO Out Attempts (GERAN)'], errors='coerce')
            avg_irat_ho_sr_perc = (geran_ho_attempt.sum()-geran_ho_success.sum())/geran_ho_attempt.sum()
            avg_irat_ho_sr_perc = round(avg_irat_ho_sr_perc*100,2)

            df['DROP Call Rate'] = np.where(df['DROP Call Rate (Denom)'] != 0, df['DROP Call Rate (Numerator)'] / df['DROP Call Rate (Denom)'],np.nan)  # Replace with NaN where Denom is 0
            avg_drop_call_rate = df['DROP Call Rate'].mean()
            avg_drop_call_rate = round(avg_drop_call_rate*100,2)

            df['DROP ERAB Rate'] = df['ERAB Drop Volte (Numerator)'] / df['ERAB Drop Volte (Denom)']
            avg_erab_drop_perc = df['DROP ERAB Rate'].mean()
            avg_erab_drop_perc = round(avg_erab_drop_perc*100,2)

            # Connect to the database
            conn = psycopg2.connect(
                dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port
            )
            cursor = conn.cursor()

            # Insert data into the database
            insert_query = """
            INSERT INTO tcs_kpi (
                date,location, total_data_volum, total_volte_traffic, avg_data_per_site, avg_volte_per_site,
                count_50_gb_plus, count_20_to_50_gb, count_1_to_20_gb, count_0_to_1_gb,
                count_0, count_volte_less_1, max_active_users, enb_nw_av_perc,avg_rrc_con_sr,
                avg_cssr_perc, avg_cssr_volte_perc,avg_erab_sr_perc,avg_erab_volte_sr_perc,
                avg_csfb_sr_perc,avg_ps_ho_perc,avg_irat_ho_sr_perc,avg_drop_call_rate,avg_erab_drop_perc
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s)

            ON CONFLICT (date) DO UPDATE SET
                location = EXCLUDED.location,
                total_data_volum = EXCLUDED.total_data_volum,
                total_volte_traffic = EXCLUDED.total_volte_traffic,
                avg_data_per_site = EXCLUDED.avg_data_per_site,
                avg_volte_per_site = EXCLUDED.avg_volte_per_site,
                count_50_gb_plus = EXCLUDED.count_50_gb_plus,
                count_20_to_50_gb = EXCLUDED.count_20_to_50_gb,
                count_1_to_20_gb = EXCLUDED.count_1_to_20_gb,
                count_0_to_1_gb = EXCLUDED.count_0_to_1_gb,
                count_0 = EXCLUDED.count_0,
                count_volte_less_1 = EXCLUDED.count_volte_less_1,
                max_active_users = EXCLUDED.max_active_users,
                enb_nw_av_perc = EXCLUDED.enb_nw_av_perc,
                avg_rrc_con_sr = EXCLUDED.avg_rrc_con_sr,
                avg_cssr_perc = EXCLUDED.avg_cssr_perc,
                avg_cssr_volte_perc = EXCLUDED.avg_cssr_volte_perc,

                avg_erab_sr_perc = EXCLUDED.avg_erab_sr_perc,
                avg_erab_volte_sr_perc = EXCLUDED.avg_erab_volte_sr_perc,
                avg_csfb_sr_perc = EXCLUDED.avg_csfb_sr_perc,
                avg_ps_ho_perc = EXCLUDED.avg_ps_ho_perc,
                avg_irat_ho_sr_perc = EXCLUDED.avg_irat_ho_sr_perc,
                avg_drop_call_rate = EXCLUDED.avg_drop_call_rate,
                avg_erab_drop_perc = EXCLUDED.avg_erab_drop_perc;
            """

            cursor.execute(insert_query,(
                report_date, 
                int(location),
                float(total_data_volume), 
                float(total_volte_traffic), 
                float(avg_data_per_site), 
                float(avg_volte_per_site),
                int(count_50_gb_plus), 
                int(count_20_to_50_gb), 
                int(count_1_to_20_gb), 
                int(count_0_to_1_gb),
                int(count_0), 
                int(count_volte_less_1), 
                int(max_active_users), 
                float(enb_nw_av_perc),
                float(avg_rrc_con_sr),
                float(avg_cssr_perc), 
                float(avg_cssr_volte_perc),
                float(avg_erab_sr_perc),
                float(avg_erab_volte_sr_perc),
                float(avg_csfb_sr_perc),
                float(avg_ps_ho_perc),
                float(avg_irat_ho_sr_perc),
                float(avg_drop_call_rate),
                float(avg_erab_drop_perc)
                ))


            conn.commit()
            print(f"{file_date} Data inserted into table.")

        except FileNotFoundError:
            print(f"File with name {file_path} does not exist!")

        except Exception as e:
            print(f"Error occurred: {e}")

        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'conn' in locals() and conn:
                conn.close()
