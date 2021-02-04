# How to build a migration project

A specific entrypoint has been developed to allow us to launch
the migration of the database:
> odoo/bin/rundatabasemigration

This script launch the marabunta migration to the new version.

In this case, the `marabunta_version` table is removed to clean
the old version installed on previous odoo version.

The marabunta migration is launched only if:
- we have the environment variable: `MARABUNTA_MODE=migration`
- the new version has never been built on the database

This entry point can be launch like this:

> docker-compose run --rm -e MARABUNTA_MODE=migration -e DB_NAME=odoodb odoo rundatabasemigration`

N.B: About the database migration on integration/production environment,
we have a dedicated service to launch it.

See: https://github.com/camptocamp/business-cloud-template
