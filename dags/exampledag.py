from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_message(**context):
    msg = context['dag_run'].conf.get('message', 'No message provided')
    print(f"Message: {msg}")

with DAG(
    dag_id="external_trigger_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:
    task = PythonOperator(
        task_id="print_message_task",
        python_callable=print_message,
        provide_context=True
    )
