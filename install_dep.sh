# install required dependencies for the project
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install elasticsearch -y
sudo apt install openjdk-11-jdk openjdk-11-jre -y
sudo service elasticsearch start
sudo apt install python3.8 python3-venv python3.8-dev build-essential -y
python3.8 -m venv venv
source venv/bin/activate
pip install wheel
pip install -r requirements.txt