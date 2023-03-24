apt-get update -y
apt-get install software-properties-common -y

add-apt-repository ppa:deadsnakes/ppa -y
apt-get update -y

apt-get install python3 -y
apt-get install python3 distutils -y
apt-get install pip -y

#apt-get install default-jdk -y
apt-get install openjdk-8-jdk -y

python3 -m pip install flask
python3 -m pip install pyspark==3.3.2
python3 -m pip install papermill
python3 -m pip install --upgrade pip ipython ipykernel
ipython kernel install --name "python3" --user
export PYSPARK_PYTHON=/usr/bin/python3
export PYSPARK_DRIVER_PYTHON=/usr/bin/python3
python3 /home/mainv1.py