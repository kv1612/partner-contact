# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import os

from invoke import exceptions, task

from .common import check_git_diff, exit_msg
from .database import _get_list_of_dumps, download_dump
from .submodule import init, update


@task
def test(
    ctx,
    pr_link,
    get_production_db=None,
    get_integration_db=None,
    template_db=None,
    create_template=None,
    keep_alive=None,
    base_branch='master',
):
    """
    This task will start a project build with requested PR and database
    datebase can be loaded from production/integration or reused previous
    created database template
    """
    _check_arguments(
        get_production_db, get_integration_db, template_db, create_template
    )
    docker_yml_name = 'docker-compose.override-{}.yml'.format(pr_link)
    if not keep_alive:
        restart(ctx)
    handle_git_repository(ctx, pr_link, base_branch)
    generate_docker_yml(pr_link, docker_yml_name)

    database = get_integration_db or get_integration_db
    if database:
        database_dumb = _load_database(ctx, pr_link, database)

    if create_template:
        _handle_database_template(ctx, pr_link, database_dumb)

    if template_db:
        _restore_database_from_template(ctx, pr_link, template_db)

    print('Starting container')
    print('Database migration started you can reach database on port 8069')
    ctx.run(
        'docker-compose -f docker-compose.yml -f {} up'.format(
            docker_yml_name
        ),
        hide=True,
    )


def _check_arguments(
    get_production_db=None,
    get_integration_db=None,
    template_db=None,
    create_template=None,
):
    # check if all arguments correctly send
    if get_production_db and get_integration_db:
        print(
            'You cannot initialize production and integration in the same time'
        )
        raise exceptions.Exit(1)

    if create_template and not (get_production_db or get_integration_db):
        print('For template option database argument is required')
        raise exceptions.Exit(1)


def _restore_database_from_template(ctx, pr_link, template):
    _drop_db(ctx, 'odoodb-{}'.format(pr_link))
    ctx.run(
        'docker-compose run --rm odoo createdb -T {} odoodb-{}'.format(
            template, pr_link
        )
    )


def _handle_database_template(ctx, pr_link, database_dumb):
    # at this point we should have the database loaded under proper name
    _drop_db(ctx, 'odoodb{}-template'.format(pr_link))
    _create_db(ctx, 'odoodb{}-template'.format(pr_link))

    try:
        print('Creating template')
        ctx.run(
            'docker-compose run --rm odoo pg_restore -p 5432 -d odoodb{}-template < {}'.format(
                pr_link, database_dumb
            ),
            hide=True,
        )
    except Exception:
        # to ignore warnings on db restore
        pass


def _load_database(ctx, pr_link, database):

    dump_path = _get_list_of_dumps(ctx, database)[-1]
    gpg_fname = os.path.basename(dump_path)
    fname = os.path.splitext(gpg_fname)[0]

    download_dump(ctx, database)
    _drop_db(ctx, 'odoodb-{}'.format(pr_link))
    _create_db(ctx, 'odoodb-{}'.format(pr_link))

    if os.path.isfile(fname):
        try:
            print('Restoring database')
            ctx.run(
                'docker-compose run --rm odoo pg_restore -p 5432 -d odoodb-{} < {} -O'.format(
                    pr_link, fname
                ),
                hide=True,
            )
        except Exception:
            # to ignore warnings on db restore
            pass
    else:
        msg = "** Database file for restore is not found**"
        exit_msg(msg)
        return
    return fname


def _drop_db(ctx, database_name):
    try:
        print('Cleanup database {}'.format(database_name))
        ctx.run('docker-compose run --rm odoo dropdb {}'.format(database_name))
    except Exception:
        pass


def _create_db(ctx, database_name):
    try:
        print('Create database {}'.format(database_name))
        ctx.run(
            'docker-compose run --rm odoo createdb -O odoo {}'.format(
                database_name
            )
        )
    except Exception:
        pass


def handle_git_repository(ctx, pr_number, branch):

    check_git_diff(ctx)
    master = 'remotes/origin/{}'.format(branch)

    try:
        print('Restoring database')
        ctx.run('git checkout -b {}'.format(pr_number))
    except Exception:
        ctx.run('git checkout {}'.format(pr_number))
    ctx.run('git fetch origin +refs/pull/{}/merge'.format(pr_number))
    ctx.run('git reset --hard FETCH_HEAD')

    # rebuild image if there was changes
    docker_diff = ctx.run(
        'git diff {} {} odoo/Dockerfile'.format(pr_number, master), hide=True
    )
    req_diff = ctx.run(
        'git diff {} {} odoo/requirements.txt'.format(pr_number, master),
        hide=True,
    )

    init(ctx)
    update(ctx)
    if docker_diff.stdout or req_diff.stdout:
        print('Rebuilding docker image')
        ctx.run('docker-compose build odoo', hide=True)


def generate_docker_yml(PR, file_name):
    # generate additional docker-compose file
    with open(file_name, "w+") as f:
        data = """
version: '2'
services:
  odoo:
    environment:
        DB_NAME: odoodb-{}
  nginx:
    ports:
      - 8069:80
        """.format(
            PR
        )
        f.write(data)


print('Restoring database')


def restart(ctx):
    ctx.run('docker-compose down')
