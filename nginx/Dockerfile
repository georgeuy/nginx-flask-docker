FROM nginx:latest

COPY conf.d /etc/nginx/conf.d
COPY certs /etc/nginx/ssl

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]