Indigo ELN Changelog
=====================

Indigo ELN 3.0: Rebuilt for the Way Chemists Work Today
--------------------------------------------------------

*25 November 2026*

Indigo ELN 3.0 is here, and it's a whole new lab notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We didn't just add features to the old system. We rebuilt Indigo ELN from
scratch: new backend, new interface, new database. Every screen and every
workflow was designed again with one question in mind: *how do we make the
scientist's day easier?*

The result is the fastest, most capable and most enjoyable version of
Indigo ELN we've ever released.


🧪 From sketch to registered sample, in one place
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Draw your reaction in the built-in **Ketcher** editor. **Analyze RXN**
matches each structure to real materials from Sample Registration, PubChem
or your own materials. **Stoichiometry** is calculated as you go, with
proper units and the significant figures you choose. When the product is
ready, **record batches, import or export them as SDF, and register them**
without leaving the experiment.


↩️ Work fearlessly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Undo and redo** any edit to an experiment. Mistakes are now just a
  click away from fixed.
- A full **audit log** and **version history** show who changed what, and
  when.
- **Edit together without conflict.** When colleagues work on the same
  experiment, their changes are compared and reconciled, never silently
  overwritten.


✍️ The full lifecycle, built in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete, **e-sign**, approve, reopen or repeat experiments, and produce a
polished **PDF report** with one click.


🔍 Find anything, instantly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Global Search** works across all your projects, notebooks and
experiments. **Starred experiments**, status filters and breadcrumbs keep
your current work close at hand.


👥 Share exactly what you mean to
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Invite a colleague to a single experiment, and **Limited View** gives them
access to that experiment and nothing more. **Admin**, **Can Edit** and
**Can View** roles keep access clear at every level.


🔐 Ready for your organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Single Sign-On** works with **Keycloak** or **AWS Cognito**. A hardened,
modern stack is built on Quarkus, Java 25, React 19 and PostgreSQL. You
can deploy it on **AWS** or run it on your own machine with **a single
command**.


🚀 Try it today
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Run it locally in minutes:**

.. code-block:: bash

   git clone https://github.com/epam/IndigoELN.git
   cd IndigoELN/deployment-compose
   ./deploy.sh

Then open ``http://localhost`` and sign in as ``admin`` / ``admin``.

**Prefer not to install anything?** Try the
`online sandbox <https://indigo-eln.lifescience.opensource.epam.com/>`_.
Email us to request access.

📖 New to Indigo ELN? The **User Manual** in ``documentation/`` walks you
through everything.


Coming from 2.x?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version 3.0 is built on a completely new data store, so existing data
needs to be migrated. We're happy to help: write to
`indigoeln@epam.com <mailto:indigoeln@epam.com>`_.

----

**Indigo ELN is open source.** Give it a try, tell us what you think, and
help us shape what comes next. ⭐ Star the repo, open an issue, or just
say hello at `indigoeln@epam.com <mailto:indigoeln@epam.com>`_.

*Welcome to Indigo ELN 3.0. We can't wait to see what you discover with
it.* 🧬


Indigo ELN 2.1
---------------

*18 February 2025*

The major changes are the following:

- Self-sufficient local deployment by running all services and databases with docker-compose
- Hot-fixes: server-side Ketcher functions fix, refactored back-end queries routing

Indigo ELN 2.0
---------------

*23 July 2018*

The major changes are the following:

- Web-based ELN functionality without using any proprietary services or commercial third-party products
- Support of extended user management system (users and roles, entities sharing)
- Hierarchy of logical and database entities (projects, notebooks, experiments, components)
- Mechanism of templates to create different types of experiments without the need to change the code



Indigo ELN 1.2
---------------

*08 May 2015*

The major changes are the following
 - Tomcat for application deployment instead of JBOSS application server
 - Spring Remoting instead of EJB
 - Maven code structure 
 - Reporting: BIRT 3.7.2 instead of 2.5.2 
 - Basic Application Security
 - One deployment unit for both client and server side
 - (Compound Registration Service) Spring Remoting instead of WebServices

Indigo ELN 1.1.3
-----------------

*15 December 2014*

The major changes are the following

-  Extended list of the database supported: PostgreSQL 9.2; Oracle 11+;
   Oracle 11+ Express. As a result – minor changes in the database
   schema.
-  Application server JBOSS 7.1.1 instead of JBOSS 5.1
-  All EJB 2 components substituted with EJB 3 ones

Indigo ELN 1.1.1
-----------------

*30 April 2013*

The major changes are the following

-  Search experiments via reactions and molecules in local database
-  Configurable reactant search in different databases
-  Indigo ELN now works on Mac OS X and GNU/Linux
-  Bug fixes

Indigo ELN 1.1
---------------

*5 February 2013*

The major changes are the following:

-  Integration with Ketcher product (sketcher)
-  Implementation of and integration with simple registration/search
   services
-  Fixes for the signing procedure and stoichiometry calculations

