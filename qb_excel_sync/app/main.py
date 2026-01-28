from app.config import (
    EXCEL_MODE,
    LOCAL_EXCEL_PATH,
    CSV_SOURCE_FOLDER,
    EXCEL_SOURCE_FOLDER,
)
from app.services.data_import import collect_all_payments
from app.services.excel_local import update_payment_status_rows_local
from app.logging import logger


def main():
    logger.info("Starting payment sync")

    payments = collect_all_payments(
        csv_folder=CSV_SOURCE_FOLDER,
        excel_folder=EXCEL_SOURCE_FOLDER,
    )

    if not payments:
        logger.warning("No payment data found")
        return

    if EXCEL_MODE == "local":
        update_payment_status_rows_local(
            LOCAL_EXCEL_PATH,
            payments
        )
    else:
        logger.error("Online mode not yet implemented")

    logger.info("Sync complete")


if __name__ == "__main__":
    main()
