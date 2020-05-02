FROM adminer:latest

USER root

RUN echo "upload_max_filesize = 1024M" >> /usr/local/etc/php/conf.d/upload_large_dumps.ini \
    && echo "post_max_size = 1024M"       >> /usr/local/etc/php/conf.d/upload_large_dumps.ini \
    && echo "memory_limit = -1"           >> /usr/local/etc/php/conf.d/upload_large_dumps.ini \
    && echo "max_execution_time = 0"      >> /usr/local/etc/php/conf.d/upload_large_dumps.ini

VOLUME /sessions

USER adminer

EXPOSE 8080