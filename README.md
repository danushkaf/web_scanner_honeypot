# Web Scanner Honeypot
This service will accept all `GET` calls and will emit text streaming messages in each 5 seconds.

## Quick Start
### Setting up
First of all add following host entry.
  * 127.0.0.1	danushkaf.honeypot.com

Make sure both docker and docker compose are installed in your environment.
### Building images and start up using Docker Compose
Run 
* `docker-compose build`
* `docker-compose up`
### Test API
If you want to test using curl
* `curl -v -k https://danushkaf.honeypot.com/`

If you are using https://github.com/sullo/nikto Run
* `./nikto.pl -h https://danushkaf.honeypot.com/`

## Running in Production
* To run this service in production, some container orchestration system such as kubernetes can be used.
* API container can be scaled and can set to auto scale based on service metrics to handle higher loads.
* Real SSL certs needs to be generated for the load balancer. SSL can be terminated at LB similar to docker compose setup.
