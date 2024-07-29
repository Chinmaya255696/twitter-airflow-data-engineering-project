sudo apt-get update
sudo apt install python3-pip
sudo apt update
sudo apt install python3-venv
python3 -m venv airflow-venv
source airflow-venv/bin/activate
pip install apache-airflow
pip install pandas 
pip install s3fs
pip install ntscraper

# to start airflow server
airflow standalone  
#this is for devlopment purposes only Don't use it in production