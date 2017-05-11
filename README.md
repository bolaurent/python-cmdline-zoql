NAME
====

**zoql** — accepts Zuora object query language queries (both zoql and export zoql are accepted) and displays results in terminal or in excel.

SYNOPSIS
========

| **zoql** \[**-u**|**--user**] [**--excel**] [**--sandbox**]

DESCRIPTION
===========

Presents a prompt ("zoql>"), and waits for valid Zuora zoql queries. 
Queries may be on multiple lines; they are terminated either by a trailing
semicolon or by a blank line of entry.

zoql terminates when it encounters EOF (ctrl-D) or the single character "q" on a line.

zoql supports readline movement commands.

If export zoql is detected, zoql creates, retrieves, deletes, and displays an export file.

See the references below for links to documentation of Zoql at the Zuora knowledge site.

Options
-------

-u, --user

:   the username; if this is supplied, zoql will request the password using getpass()

--sandbox

:   use the Zuora apisandbox, rather than the production instance


--excel

:   use xlwings to transfer the query results to Excel, rather than displaying in the terminal


Credentials
-----------

If the --user option is not given, credentials are obtained from ~/.zuora-production-config.json or (if you add the argument --sandbox) from ~/.zuora-sandbox-config.json.


FILES
=====

*~/.zuora-production-config.json*

:   user name and credentials for Zuora production instance

*~/.zuora-sandbox-config.json*

:   user name and credentials for Zuora sandbox instance

The file format is json:
```
    {
      "user":     "me@here.com",
      "password": "mypassword"
    }
```

INSTALL
=====

pip install  git+git://github.com/bolaurent/python-cmdline-zoql.git

BUGS
====

See GitHub Issues: <https://github.com/bolaurent/python-cmdline-zoql/issues>

AUTHOR
======

Bo Laurent <bo@bolaurent.com>


KUDOS
========

Many thanks to [Distributing a Python command line application](https://gehrcke.de/2014/02/distributing-a-python-command-line-application/)

REFERENCES
==========

* [ZOQL Documentation](https://knowledgecenter.zuora.com/DC_Developers/K_Zuora_Object_Query_Language)
* [Export ZOQL Documentation](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL)
