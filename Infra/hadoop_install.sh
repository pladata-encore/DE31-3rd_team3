# Author: Clyde0909
# Date: 2024-07-02
# Pre-req: hostnames should be set for all the nodes

# install hadoop
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

# in this project, we will use three nodes[node1, node2, node3] for hadoop cluster
# send the hadoop tar file to all the nodes
scp hadoop-3.3.6.tar.gz node1:/home/minip3
scp hadoop-3.3.6.tar.gz node2:/home/minip3
scp hadoop-3.3.6.tar.gz node3:/home/minip3

# ssh to all the nodes and extract the hadoop tar file
ssh node1 "tar -xvzf hadoop-3.3.6.tar.gz /home/minip3/hadoop"
ssh node2 "tar -xvzf hadoop-3.3.6.tar.gz /home/minip3/hadoop"
ssh node3 "tar -xvzf hadoop-3.3.6.tar.gz /home/minip3/hadoop"

# install openjdk 11 on all the nodes
ssh node1 "sudo apt install openjdk-11-jdk -y"
ssh node2 "sudo apt install openjdk-11-jdk -y"
ssh node3 "sudo apt install openjdk-11-jdk -y"

# add environment variables to .bashrc file
echo "####### hadoop setttings" >> ~/.bashrc
echo "export HADOOP_HOME=/home/minip3/hadoop" >> ~/.bashrc
echo "export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop" >> ~/.bashrc
echo "export HADOOP_INSTALL=$HADOOP_HOME" >> ~/.bashrc
echo "export HADOOP_MAPRED_HOME=$HADOOP_HOME" >> ~/.bashrc
echo "export HADOOP_COMMON_HOME=$HADOOP_HOME" >> ~/.bashrc
echo "export HADOOP_HDFS_HOME=$HADOOP_HOME" >> ~/.bashrc
echo "export HADOOP_YARN_HOME=$HADOOP_HOME" >> ~/.bashrc
echo "export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native" >> ~/.bashrc
echo "export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"" >> ~/.bashrc
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/" >> ~/.bashrc
echo "export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin" >> ~/.bashrc

# source the .bashrc file
source ~/.bashrc

# push .bashrc file to all the nodes
scp ~/.bashrc node1:/home/minip3
scp ~/.bashrc node2:/home/minip3
scp ~/.bashrc node3:/home/minip3

# copy all settings file to hadoop conf directory
cp ./hadoop_settings/* $HADOOP_HOME/etc/hadoop/

# copy current user's hadoop settings to all the nodes
scp $HADOOP_HOME/etc/hadoop/* node1:$HADOOP_HOME/etc/hadoop/
scp $HADOOP_HOME/etc/hadoop/* node2:$HADOOP_HOME/etc/hadoop/
scp $HADOOP_HOME/etc/hadoop/* node3:$HADOOP_HOME/etc/hadoop/

# create a directory for hadoop data for all the nodes
ssh node1 "mkdir -p /home/minip3/data"
ssh node2 "mkdir -p /home/minip3/data"
ssh node3 "mkdir -p /home/minip3/data"

# format the namenode
ssh node1 "cd ~/data && hadoop namenode -format"

# start the hadoop cluster
ssh node1 "start-dfs.sh"
ssh node2 "start-yarn.sh"
ssh node1 "mr-jobhistory-daemon.sh start historyserver"
