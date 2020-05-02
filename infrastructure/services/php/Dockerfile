FROM php:7.4-fpm-alpine

ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/
RUN chmod uga+x /usr/local/bin/install-php-extensions && sync

RUN apk add --update \
        icu-dev \
        libzip-dev zip unzip \
        nodejs \
        libxslt-dev \
    && apk add --no-cache $PHPIZE_DEPS \
    && pecl install \
        xdebug \
        apcu \
    && docker-php-ext-install \
        opcache \
        intl \
		pdo_mysql \
        xsl \
        zip \
        calendar \
    && docker-php-ext-enable \
        xdebug \
        apcu \
        opcache \
    && install-php-extensions imagick \
    && docker-php-ext-configure \
        calendar

RUN rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
RUN mkdir /.composer && chown -R 1000:1000 /.composer
