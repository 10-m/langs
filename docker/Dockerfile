FROM centos:centos7
MAINTAINER test_user test_user@abc.com

RUN echo "This is shell format"
RUN ["/bin/bash", "-c", "echo 'This is exec format'"]

RUN yum -y install httpd

ONBUILD ADD website.tar /var/www/html

CMD /usr/sbin/httpd -D FOREGROUND
