from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

def print_message(**context):
    # Use Airflow's logging instead of print
    dag_run_conf = context.get('dag_run').conf if context.get('dag_run') else {}
    message = dag_run_conf.get('message', 'No message provided')
    logging.info(f"Received message from trigger: {message}")

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id="external_trigger_dag",
    default_args=default_args,
    description="A DAG triggered externally to print a message",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # Only triggered manually or externally
    catchup=False,
    tags=["external", "example"]
) as dag:

    print_task = PythonOperator(
        task_id="print_message_task",
        python_callable=print_message,
        provide_context=True
    )
