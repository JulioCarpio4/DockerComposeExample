FROM nginx:stable
COPY ./nginx.conf /etc/nginx/nginx.conf

RUN mkdir /data && mkdir /data/www 
COPY ./index.html /data/www

CMD ["nginx", "-g", "daemon off;"]