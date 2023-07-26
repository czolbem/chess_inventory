FROM python:3.11

USER root

ADD cloud_services_root_ca.crt /usr/share/ca-certificates/cloud_services_root_ca.crt
RUN echo cloud_services_root_ca.crt >> /etc/ca-certificates.conf
ADD cloud_services_ca_g2.crt /usr/share/ca-certificates/cloud_services_ca_g2.crt
RUN echo cloud_services_ca_g2.crt >> /etc/ca-certificates.conf
ADD ssl_sg1_global.crt /usr/share/ca-certificates/ssl_sg1_global.crt
RUN echo ssl_sg1_global.crt >> /etc/ca-certificates.conf
RUN update-ca-certificates
RUN keytool -import -trustcacerts -cacerts -storepass changeit -noprompt -alias cloud_services_root_ca -file /usr/share/ca-certificates/cloud_services_root_ca.crt
RUN keytool -import -trustcacerts -cacerts -storepass changeit -noprompt -alias cloud_services_ca_g2 -file /usr/share/ca-certificates/cloud_services_ca_g2.crt
RUN keytool -import -trustcacerts -cacerts -storepass changeit -noprompt -alias ssl_sg1_global -file /usr/share/ca-certificates/ssl_sg1_global.crt