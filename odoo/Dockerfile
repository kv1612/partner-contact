FROM ghcr.io/camptocamp/odoo-project:14.0-latest
LABEL maintainer="Camptocamp"
LABEL org.opencontainers.image.source https://github.com/camptocamp/cosanum_odoo

# Steps are grouped by dependency
# and ordered by compromizing cost and frequency

## Base requirements (Libs and packages)
# frequency: rarely
# cost:      high

COPY ./*requirements.txt /odoo/
# Install additional debian and python packages if needed
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
        parallel libmagic1 \
        cups \
        # if you need some dev packages for python packages, you need to clean them afterwards
        python3-dev build-essential \
        libcups2-dev \
        && cd /odoo \
        && find . -maxdepth 1 -name "*requirements.txt" ! -name src_requirements.txt ! -name base_requirements.txt | xargs -I{} pip install -r {} \
        # cleaning of dev packages
        && apt-get remove --purge -y build-essential python3-dev libcups2-dev \
        # && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*


## Tools of odoo-template
# frequency: seldom
# cost:      light

# Entrypoints
COPY ./before-migrate-entrypoint.d/* /before-migrate-entrypoint.d/
COPY ./start-entrypoint.d/* /start-entrypoint.d/
RUN chmod +x /before-migrate-entrypoint.d/* \
    && chmod +x /start-entrypoint.d/*
# CSV Loader
# `parallel` + `importer.sh` are needed to load heavy files
COPY ./bin/importer.sh /odoo-bin/
# Migration project
COPY ./bin/rundatabasemigration /odoo-bin/
## Prepare pip install
# frequency: never
# cost     : very light
COPY ./setup.py /odoo/

## Main activity
# frequency: always
# costs:     very high to very light
COPY ./src /odoo/src
COPY ./external-src /odoo/external-src
COPY ./local-src /odoo/local-src
COPY ./data /odoo/data
COPY ./songs /odoo/songs
COPY ./VERSION /odoo/
COPY ./migration.yml /odoo/

# depends on ./setup.py ./src, ./songs and ./VERSION
RUN cd /odoo && pip install -r src_requirements.txt

## Environment
# frequency: sometimes
# cost:      very light
ENV ADDONS_PATH="/odoo/external-src/odoo-cloud-platform, \
  /odoo/external-src/account-closing, \
  /odoo/external-src/account-financial-reporting, \
  /odoo/external-src/account-financial-tools, \
  /odoo/external-src/account-invoice-reporting, \
  /odoo/external-src/account-invoicing, \
  /odoo/external-src/account-reconcile, \
  /odoo/external-src/bank-payment, \
  /odoo/external-src/bank-statement-import, \
  /odoo/external-src/brand, \
  /odoo/external-src/community-data-files, \
  /odoo/external-src/connector, \
  /odoo/external-src/connector-interfaces, \
  /odoo/external-src/contract, \
  /odoo/external-src/delivery-carrier, \
  /odoo/external-src/ddmrp, \
  /odoo/external-src/e-commerce, \
  /odoo/external-src/edi, \
  /odoo/external-src/enterprise, \
  /odoo/external-src/hr-attendance, \
  /odoo/external-src/hr-holidays, \
  /odoo/external-src/intrastat-extrastat, \
  /odoo/external-src/knowledge, \
  /odoo/external-src/l10n-switzerland, \
  /odoo/external-src/management-system, \
  /odoo/external-src/manufacture, \
  /odoo/external-src/mis-builder, \
  /odoo/external-src/odoo-shopinvader, \
  /odoo/external-src/odoo-shopinvader-payment, \
  /odoo/external-src/partner-contact, \
  /odoo/external-src/product-attribute, \
  /odoo/external-src/product-variant, \
  /odoo/external-src/purchase-workflow, \
  /odoo/external-src/queue, \
  /odoo/external-src/rest-framework, \
  /odoo/external-src/report-print-send, \
  /odoo/external-src/reporting-engine, \
  /odoo/external-src/sale-workflow, \
  /odoo/external-src/search-engine, \
  /odoo/external-src/server-auth, \
  /odoo/external-src/server-env, \
  /odoo/external-src/server-tools, \
  /odoo/external-src/server-ux, \
  /odoo/external-src/social, \
  /odoo/external-src/stock-logistics-reporting, \
  /odoo/external-src/stock-logistics-transport, \
  /odoo/external-src/stock-logistics-warehouse, \
  /odoo/external-src/stock-logistics-workflow, \
  /odoo/external-src/storage, \
  /odoo/external-src/web, \
  /odoo/external-src/wms, \
  /odoo/src/addons, \
  /odoo/local-src" \
  LIMIT_TIME_CPU=86400 \
  LIMIT_TIME_REAL=86400 \
  LIMIT_MEMORY_SOFT=1342177280 \
  LIMIT_MEMORY_HARD=1610612736 \
  ODOO_DATA_PATH=/odoo/data
