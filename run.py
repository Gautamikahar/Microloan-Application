# run.py
from app import create_app, db
from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.autodebit import process_auto_debits

# Create the Flask app
app = create_app()

# ------------------ Scheduler Setup ------------------ #
def start_scheduler():
    scheduler = BackgroundScheduler(daemon=True)

    # Auto-debit check every 1 minute (dev mode) / every 24 hours (prod)
    scheduler.add_job(process_auto_debits, 'interval', minutes=1)

    scheduler.start()
    print("✅ Auto-debit scheduler started...")

# ------------------ Run App ---------------------- #
if __name__ == '__main__':
    with app.app_context():
        start_scheduler()   # scheduler runs inside app context
    app.run(debug=True)
