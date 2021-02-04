XYZ-1234

### Context
> _Description ..._

### Result
* _screenshot(s) may help :camera_flash: ..._

----


- [ ] Dev clean section not needed :broom:
    - [ ] Generalities :warning:
    - [ ] Code changes :woman_technologist:
    - [ ] Inclusion of external code :handshake:
    - [ ] Migrations :boat:
    - [ ] Odoo pitfalls to watch out for :factory:
    - [ ] Python pitfalls to watch out for :snake:
    - [ ] Performance pitfalls :chart_with_upwards_trend:


<details>
<summary>Generalities :warning:</summary>
<p>

- [ ] Scope: Is the change at the right place, should it be in an OCA addon, standalone local addon or a "catchall" local addon? Read Structure of local addons in a project
- [ ] Specification: follow the specification
    - [ ] Multi-company: make sure the feat/fix works in a multi-company env if this is there

</p>
</details>

<details>
<summary>Code changes :woman_technologist:</summary>
<p>

- [ ] Dependencies: if we inherit something in XML or Python, check the dependency is added
- [ ] Complexity: if you don't understand the code, maybe it needs a rewrite (pay attention to variables names) or comments
- [ ] Input and outputs: method input and outputs look correct
- [ ] Commit messages: follow the [conventions](https://confluence.camptocamp.com/confluence/display/BS/Code+reviews+handbook#Codereviewshandbook-Commitmessage)
- [ ] History file: filed and follow the conventions (write for humans!), include the JIRA card number if any (todo)
- [ ] Tests updated, added?
- [ ] Style and layout of modified code
- [ ] If added/updated a submodule with pending-merges, is the gitaggregate have been pushed?
- [ ] If updated fields or xml files: is the module included in next upgrade step?
</p>
</details>

<details>
<summary>Inclusion of external code :handshake:</summary>
<p>

- [ ] Python library: check if the library is maintained and of good quality
- [ ] External addons: if a non-OCA addons submodule is added, audit the code comprising the addons we don't install (library import or monkey patches can break the rest).
</p>
</details>

<details>
<summary>Migrations :boat:</summary>
<p>

- [ ] All modified addons are upgraded
- [ ] Any migration song can be run idempotently, if you run it twice it should not fail
- [ ] Be protective about unknowns, check the state of the db before doing actions
</p>
</details>

<details>
<summary>Odoo pitfalls to watch out for :factory:</summary>
<p>

- [ ] New model without security rules
- [ ] button callbacks (typically "def action_xxx") which change a state, but don't check the current state of the record (rationale: you can hide the button depending on the state in the view, but it is easy tocall the method by mistake in a migration script for instance and make a mess in the database)
- [ ] views or reports removing a field / element (to put it somewhere else) without defining a low priority (high value in the field) (this can break other view using that field if they use it as an anchor)
- [ ] api.multi methods without a loop on self or without self.ensure_one() (and if self.ensure_one is used, check that the method cannot be called on a recordset of size != 1 (and by this I mean both >1 and 0))
- [ ] api.constrains using dotted path (this does not work and only generates a warning)
- [ ] computed fields using fields in the computation which are not part of the list in api.depends
- [ ] computed fields depending on non stored fields
- [ ] related fields which are not readonly=True (not an error, but if it is not intended, it allows editing the related record which is often not what you want)
- [ ] model with a state, and the fields definition do not include states dependent readonly value
- [ ] this is also true for inherited models which add new fields
- [ ] this is also something to check on 'lines' models (e.g. sale.order / sale.order.line) : the readonly state of the line generally depend on the state of the parent record
- [ ] methods which can be called through onchange methods (and therefore on a NewId record) which have side effects on the database (calls to write / create / unlink)
- [ ] views : do the action button need to be available only for some groups ?
- [ ] methods callable by RPC which can return None (implicitly  or explicitly) => this will break external XMLRPC clients
- [ ] strings not flagged for translation
- [ ] new models with a company_id field and no record rules
- [ ] magic numbers and hard coded constants (should they be configurable? could they be company dependent?)
- [ ] use of now() and today() : these make testing a method difficult and scripting the method to fix stuff in the past difficult. Prefer having a parameter date or datetime on the function, defaulting to None,and using today() / now() if no explicit value was passed.
- [ ] model with fields like start and end without a constraint that end > start. Bonus if there is a smart onchange_start which moves end to a later date if necessary.
- [ ] timezone handling when dates and hours are combined to generate a datetime (this is a difficult topic)
</p>
</details>

<details>
<summary>Python pitfalls to watch out for :snake:</summary>
<p>

- [ ] mutable method arguments
- [ ] unprotected access to a dictionary by key if you are not sure the key is in
- [ ] division by 0
- [ ] leftover print, pdb...
- [ ] calls to logging method with explicit parameter substitutions (e.g. `_logger.debug('Frobing the baz of %s' % self.name`))
- [ ] call to tempfile.mkstemp() which do nothing with the file descriptor returned (will create a resource leak, and eventually a process crash... See https://twitter.com/gurneyalex/status/1214207595713576966
</p>
<details>
<summary>Python 2.7</summary>
<p>

- [ ] in Python 2.7, integer division yielding an integer (maybe unintended)
- [ ] in Python 2.7, use of non unicode strings in concatenations / calls to join(list) format()
</p>
</details>
</details>

<details>
<summary>Performance pitfalls :chart_with_upwards_trend:</summary>
<p>

- [ ] design of the code, splitting a recordset and processing individual records rather than keeping the code together
- [ ] try to get a feeling about the number of records being processed : 1 at a time from the UI, or potentially 100ds from a cron...
- [ ] beware of the use of filtered(), sometimes a search with the proper domain is way more efficient
- [ ] non stored computed fields displayed in a list view, check the computation method implementation
- [ ] missing indexes on computed fields / fields used by frequent search (this can be dramatic on calls to search_count, typically used with "smart buttons" to display the number of related records andthe access to o2m fields, and the use of mapped())
</p>
</details>
