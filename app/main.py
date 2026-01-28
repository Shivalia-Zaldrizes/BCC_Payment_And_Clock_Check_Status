
#from app.config import (
 #   EXCEL_MODE,
  #  LOCAL_EXCEL_PATH,
   # CSV_SOURCE_FOLDER,
    #EXCEL_SOURCE_FOLDER,
#)
#from app.services.data_import import collect_all_payments
#from app.services.excel_local import update_payment_status_rows_local
#from app.logging import logger


#def main():
 #   logger.info("Starting payment sync")

  #  payments = collect_all_payments(
   #     csv_folder=CSV_SOURCE_FOLDER,
    #    excel_folder=EXCEL_SOURCE_FOLDER,
    #)

    #if not payments:
     #   logger.warning("No payment data found")
      #  return

    #if EXCEL_MODE == "local":
     #   update_payment_status_rows_local(
      #      LOCAL_EXCEL_PATH,
       #     payments
        #)
    #else:
     #   logger.error("Online mode not yet implemented")

    #logger.info("Sync complete")


#if __name__ == "__main__":
 #   main()


#LOCAL FILES TEST


# app/main.py

import pandas as pd
from datetime import datetime

from app.services.data_cleaning import clean_qb_payroll
from app.services.excel_local import update_excel_local
from app.config import (
    QB_EXPORT_PATH,
    HOURS_EXCEL_PATH,
    OUTPUT_EXCEL_PATH,
    USE_GRAPH
)

def main():
    # --- Read QuickBooks CSV ---
    print(f"Reading QuickBooks CSV from {QB_EXPORT_PATH}")
    qb_df = pd.read_csv(QB_EXPORT_PATH)

    qb_clean = clean_qb_payroll(qb_df)

    # --- Read Employee Hours Excel ---
    print(f"Reading Hours Excel from {HOURS_EXCEL_PATH}")
    hours_df = pd.read_excel(HOURS_EXCEL_PATH)

    hours_clean = clean_qb_payroll(hours_df)

    # --- Merge datasets ---
    print("Merging payroll and hours data...")
    merged_df = pd.merge(
        qb_clean,
        hours_clean,
        on="merge_name",
        how="left",
        suffixes=("_qb", "_hours")
    )

    # --- Add audit metadata ---
    merged_df["last_synced_at"] = datetime.utcnow()
    merged_df["source_system"] = "QuickBooks"

    # --- Output ---
    if USE_GRAPH:
        print("Graph mode enabled (not implemented yet)")
    else:
        print(f"Writing output to {OUTPUT_EXCEL_PATH}")
        update_excel_local(OUTPUT_EXCEL_PATH, merged_df)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
