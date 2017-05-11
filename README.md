python-cmdline-zoql
========================

This is a command line interpreter for Zuora's object query language, zoql.

Usage
-----

Invoke zoql from the prompt of your command interpreter as follows:

```
        shell> zoql
```
    Or:

```
        shell> zoql --excel
```

    Or:

```
        shell> zoql --sandbox
```

Then enter a valid soql query (one or more lines) followed by a semicolon.

The output will either be displayed in your terminal, or sent to Excel.


Credentials
-----------

Credentials are obtained from ~/.zuora-production-config.json or from ~/.zuora-sandbox-config.json (if you add the argument --sandbox).


Commands
--------

    q: quit

