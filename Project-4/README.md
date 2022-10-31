## Part 2 Notes:
1. I created a file in the `/etc/hosts/` directory formatted like below (for webserv2):

> 10.0.1.10 www.mysite.com webserv1

2. To SSH into between the systems, we first need to connect to the proxy like so:

> ssh -i [KEYNAME].pem ubuntu@18.214.80.208 (ip created for this instance)

After connecting to the proxy, we can ssh into each system using its private ip:

> ssh ubuntu@10.0.1.10

> ssh ubuntu@10.0.1.20

3. HAProxy Config
The config file is available at `/etc/haproxy/haproxy.cfg`
- 
Resources used:
- [HA Proxy](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)

4. Setting up the webserver
