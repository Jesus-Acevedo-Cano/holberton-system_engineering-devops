# 0x09. Web infrastructure design
System engineering & DevOps ― Web stack

## Contents
* [Purpose](./#Purpose)
* [Files](./#Files)
* [Author](./#author)
---
## Purpose
- To learn Network basics
- To learn What is Server and Web server
- To learn What is DNS
- To learn What is load balancer, monitoring, HTTPS, and firewall
---

## Files
|File| Description
|---|-----
| [0-simple_web_stack](./0-simple_web_stack) | **diagram must includes**:<br />- 1 server <br />- 1 web server (Nginx) <br />- 1 application server <br />- 1 application files (your code base) <br />- 1 database (MySQL) <br />- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
| [1-distributed_web_infrastructure](./1-distributed_web_infrastructure) | **diagram must adds**: <br />- 2 servers<br />- 1 web server (Nginx) <br />- 1 application server <br />- 1 load-balancer (HAproxy)<br />- 1 application files (your code base) <br />- 1 database (MySQL)
| [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure) | **diagram must adds**: <br />- 3 firewalls<br /> - 1 SSL certificate to serve www.foobar.com over HTTPS <br />- 3 monitoring clients (data collector for Sumologic or other monitoring services)

---
## Author
#### Jesus Acevedo
- Github: [Jesus-Acevedo-Cano](https://github.com/Jesus-Acevedo-Cano)
- Twitter: [@JessAcevedoCan1](https://twitter.com/JessAcevedoCan1)

Cohort 10
Colombia - Cali - 2020
