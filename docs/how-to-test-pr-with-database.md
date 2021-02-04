# Test a PR

## How to run code with database

To test code from PR with integration or production database first of all you need to enable features from other invoke scripts.
After success run of this task you should have a new database in volume with name of given pull request
See invoke.md

Available arguments:

1. pr_link - first argument is a link on open PR in the repository
2. --get_production_db, --get_integration_db - name of database to use 
4. --create-template - True - will create a template in database which you can reuse later instead of restoring database from dump
3. --template-db - name of template to use as base to restore database, name is generated like odoodb<prnumber>-template
5. --keep_alive (by default True) - as containers started on background they may conflict on next run, by default we stop them every time, if you need to change behavior set it to False
6. --base-branch - sometimes development can be done for different branch then master


## Examples

Create a build based on PR number 530, use database from integration, create during start a template for postgres
  ```
  invoke pr.test 530 --get-integration-db=database_name --create-template=True 
  ```

Create a build based on PR number 540, use database from previous run
  ```
  invoke pr.test 540 --template-db=odoodb530-template 
  ```

## Common problems and recommendations

In case of local changes you will be asked to for erasing them.
This script may not work when you switching between odoo versions like odoo 12 and 13, in this case is better to have two repos cloned for each version.
It is better to configure git-autoshare before running this script, to save some space on your machine.

## Roadmap

1. add respecting all docker.compose.override.yaml files to have settings for external hard drive
