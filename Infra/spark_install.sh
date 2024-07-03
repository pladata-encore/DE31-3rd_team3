# Author: sswsoul89s
# Date: 2024-07-02
# Pre-req: hostnames should be set for all the nodes

# install spark
wget https://dlcdn.apache.org/spark/spark-3.4.3/spark-3.4.3-bin-hadoop3.tgz

# in this project, we will use three nodes[node1, node2, node3] for spark 
# send the spark tar file to all the nodes
scp spark-3.4.3-bin-hadoop3.tgz node1:/home/minip3
scp spark-3.4.3-bin-hadoop3.tgz node2:/home/minip3
scp spark-3.4.3-bin-hadoop3.tgz node3:/home/minip3

# ssh to all the nodes and extract the hadoop tar file
ssh node1 "tar -xvzf spark-3.4.3-bin-hadoop3.tgz /home/minip3/spark"
ssh node2 "tar -xvzf spark-3.4.3-bin-hadoop3.tgz /home/minip3/spark"
ssh node3 "tar -xvzf spark-3.4.3-bin-hadoop3.tgz /home/minip3/spark"

# copy conf file 
ssh node1 "sudo cp spark-env.sh.template spark-env.sh"
ssh node2 "sudo cp spark-env.sh.template spark-env.sh"
ssh node3 "sudo cp spark-env.sh.template spark-env.sh"

ssh node1 "sudo cp workers.template workers"
ssh node2 "sudo cp workers.template workers"
ssh node3 "sudo cp workers.template workers"

# node1 add environment variables to spark-env.sh file
echo "export SPARK_MASTER_HOST=node1" >> /opt/spark/conf/spark-env.sh
echo "export SPARK_MASTER_PORT=5055" >> /opt/spark/conf/spark-env.sh
echo "export SPARK_MASTER_WEBUI=8080" >> /opt/spark/conf/spark-env.sh
echo "export SPARK_WORKER_CORES=2" >> /opt/spark/conf/spark-env.sh
echo "export SPARK_WORKER_MEMORY=1g" >> /opt/spark/conf/spark-env.sh
echo "export SPARK_WORKER_INSTANCES=1" >> /opt/spark/conf/spark-env.sh

# add environment variables to workers file
sudo vim /opt/spark/conf/workers

#localhost
node1
node2
node3 

# node1 add environment variables to .bashrc file
echo "export SPARK_HOME=/opt/spark/" >> ~/.basrhc
echo "PATH=$PATH:$SPARK_HOME/bin" >> ~/.basrhc
echo "export PYSPARK_PYTHON=/usr/bin/python3" >> ~/.basrhc

source .bashrc

# push .bashrc file to all the nodes
ssh node1 "scp /home/minip3/.bashrc node1:/home/minip3/"
ssh node2 "scp /home/minip3/.bashrc node2:/home/minip3/"
ssh node3 "scp /home/minip3/.bashrc node3:/home/minip3/"

# push spark conf folder to all the nodes
scp -r /home/minip3/spark/conf node1:/home/minip3/spark
scp -r /home/minip3/spark/conf node2:/home/minip3/spark
scp -r /home/minip3/spark/conf node3:/home/minip3/spark

# copy spark folder to ohter nodes
ssh -t node1 "sudo mv /home/minip3/spark/ /opt/spark/"
ssh -t node2 "sudo mv /home/minip3/spark/ /opt/spark/"
ssh -t node3 "sudo mv /home/minip3/spark/ /opt/spark/"

# user permitions 
ssh node1 "sudo chown -R minip3:minip3 ./spark/"
ssh node2 "sudo chown -R minip3:minip3 ./spark/"
ssh node3 "sudo chown -R minip3:minip3 ./spark/"

# start the spark cluster
ssh node1 "./start-all.sh"
ssh node2 "jps"
ssh node3 "jps"

