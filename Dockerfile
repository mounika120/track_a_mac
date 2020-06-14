FROM ubuntu:18.04

# Install essentials
RUN apt-get update -y \
    && apt-get install -y build-essential software-properties-common curl git

# Install Python 3.6
RUN apt-get install -y python3-pip \
    && apt-get clean \
    && python3.6 -m pip install --upgrade pip


RUN apt install -y snmp snmp-mibs-downloader libsnmp-dev
RUN apt-get -y install snmpd
RUN apt-get -y install gcc python-dev
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y php sqlite3 php-sqlite3 sqlitebrowser gcc

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install easysnmp
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN python3.6 -m pip install https://github.com/etingof/snmpsim/archive/master.zip
RUN pip3 install virtualenv
RUN virtualenv venv


RUN useradd -ms /bin/bash testuser


COPY *.php /
COPY *.py /
COPY docker-start.sh /usr/local/bin/
RUN ln -s /usr/local/bin/docker-start.sh /
RUN cd ~/

RUN /bin/bash -c "echo vsftpd : 127.0.0.1 , 0.0.0.0 >> /etc/hosts.allow"
RUN /bin/bash -c "echo snmpd : ALL : ALLOW >> /etc/hosts.allow"
ENTRYPOINT ["docker-start.sh"]