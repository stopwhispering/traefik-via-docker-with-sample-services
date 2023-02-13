# traefik via docker with sample services
Traefik sample configuration with Docker containers for FastAPI, Whoami and NGINX 

| service              | dev url                   | auth | restart    | prod url*                    | auth  | restart |
|----------------------|---------------------------|------|------------|------------------------------|-------|---------|
| traefik w/ dashboard | http://traefik.localhost  | -    | always     | https://traefik.example.net  | basic | always  |
| fastapi demo api     | http://demo-api.localhost | -    | on-failure | https://demo-api.example.net | basic | always  |
| nginx demo website   | http://website.localhost  | -    | on-failure | https://website.example.net  | basic | always  |
| whoami service       | http://whoami.localhost   | -    | on-failure | https://whoami.example.net   | basic | always  |

*on Prod, HTTP is redirected globally to HTTPS

## Deployment

### Prerequisites
Generate a username/hashed password combination for basic auth via

    # Linux:
    htpasswd -nbB user password
    # Windows/WSL:
    wsl htpasswd -nbB user password

    # Note: If you enter user/pass directly into the docker-compose file, you need to escape 
    # the $ character with another $ character:
    htpasswd -nbB user password | sed -e s/\\$/\\$\\$/g
    wsl htpasswd -nbB user password | wsl sed -e s/\\$/\\$\\$/g

Create .env file with the following content:

    # your domain name
    HOSTNAME=example.net
    # email used for the let's encrypt certificate service
    LETS_ENCRYPT_EMAIL=admin@example.com
    # copy & paste the generated username/hashed password combination
    BASIC_AUTH_CREDENTIALS=user:$$2y$$05$$Bo.kZTj7WzalN5mEJDO.Oehp0nrzvwz0sa8uMymxuJlJKQ.P524li

Create traefik docker network:

    docker network create traefik-public   

### Start (Dev)

    docker-compose -f ./traefik/docker-compose.base.yml -f ./traefik/docker-compose.dev.yml up --build --detach
    
    # Example Services:
    docker-compose -f ./demo-api/docker-compose.base.yml -f ./demo-api/docker-compose.dev.yml up --build --detach
    docker-compose -f ./whoami/docker-compose.base.yml -f ./whoami/docker-compose.dev.yml up --build --detach
    docker-compose -f ./nginx-website/docker-compose.base.yml -f ./nginx-website/docker-compose.dev.yml up --build --detach

### Start (Prod)

    docker-compose -f ./traefik/docker-compose.base.yml -f ./traefik/docker-compose.prod.yml up --build --detach

    # Example Services:
    docker-compose -f ./demo-api/docker-compose.base.yml -f ./demo-api/docker-compose.prod.yml up --build --detach
    docker-compose -f ./whoami/docker-compose.base.yml -f ./whoami/docker-compose.prod.yml up --build --detach
    docker-compose -f ./nginx-website/docker-compose.base.yml -f ./nginx-website/docker-compose.prod.yml up --build --detach
