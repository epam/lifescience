:tocdepth: 2

Indigo ELN Changelog
=====================

Indigo ELN 3.0
--------------------------------------------------------

*25 November 2026*

The major changes are the following:

* Complete rebuild: the application’s backend, frontend and database layers were rebuilt on modern frameworks and components (Quarkus, React, PostgreSQL)
* User interface with a modern look and a streamlined user experience, including Global Search, breadcrumbs and starred experiments
* New capabilities include:

  * Audit log and version history of changes to projects, notebooks and experiments
  * Single Sign-On through AWS Cognito (AWS deployments) or Keycloak (local deployments)
  * Advanced access levels for experiments, including Limited View for users added to a single experiment
  * Conflict detection and resolution when several users edit the same experiment at once
  * PubChem as an additional source of materials for reaction analysis
  * Undo/redo of experiment edits

* Reworked stoichiometry calculations with unit handling and configurable significant figures
* Deployment with a single command via docker-compose (including Keycloak and PostgreSQL), or to AWS with CDK


IMPORTANT NOTE:

Data storage has been completely changed. If you need help with data migration from previous versions, please contact us at indigoeln@epam.com.


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

