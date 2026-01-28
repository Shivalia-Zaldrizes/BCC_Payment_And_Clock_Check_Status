#from openpyxl import load_workbook
#from app.logging import logger
#from app.utils.week_detection import find_week_blocks
#from app.services.data_import import PaymentUpdate


     #  PAYMENT_ROW_LABEL = "Payment Status"


     #  def update_payment_status_rows_local(
       #    excel_path: str,
       #    payments: list[PaymentUpdate]
     #  ):
     #      wb = load_workbook(excel_path)
        #   ws = wb.active

    # Map employee names to column index
      #     header_row = ws[1]
      #     employee_cols = {
        #       cell.value.strip(): cell.column
      #         for cell in header_row
       #        if cell.value and cell.column > 1
       #    }

       #    week_blocks = find_week_blocks(ws)
       #    logger.info(f"Found {len(week_blocks)} week blocks")

        #   for start_row, end_row, week_ending in week_blocks:
        # Find or insert Payment Status row
       #        payment_row = None

      #         for r in range(start_row, end_row + 1):
       #            if ws.cell(row=r, column=1).value == PAYMENT_ROW_LABEL:
       #                payment_row = r
       #                break

       #        if not payment_row:
       #            payment_row = end_row + 1
       #            ws.insert_rows(payment_row)
      #             ws.cell(row=payment_row, column=1).value = PAYMENT_ROW_LABEL
       #            logger.info(f"Inserted Payment Status row for week {week_ending}")

        # Apply payments
            #   for p in payments:
          #         if p.week_ending != week_ending:
     #                  continue

     #       col = employee_cols.get(p.employee)
    #        if not col:
   #             logger.warning(
  #                  f"Employee '{p.employee}' not found in sheet"
 #               )
#                continue

   #         ws.cell(
  #              row=payment_row,
 #               column=col
#            ).value = "PAID" if p.paid else "NOT PAID"

 #   wb.save(excel_path)
#    logger.info("Payment status update completed")


# app/services/excel_local.py

import pandas as pd

def update_excel_local(file_path, df: pd.DataFrame):
    """Writes cleaned DataFrame to Excel locally for testing."""
    try:
        df.to_excel(file_path, index=False)
        print(f"Successfully wrote {len(df)} rows to {file_path}")
    except Exception as e:
        print(f"Error writing to Excel: {e}")
