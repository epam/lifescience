# Ketcher 2.6.2
## What's Changed
Release 2.6.2 is live!
In this release we have implemented some minor improvements for development process and fixed bugs.
Please be aware Ketcher 2.6.2 has been tested with Indigo version 1.8.1 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.8.1) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.8.1/images/sha256-ed7b48b5814390cece0af1dd393796dd68324bdfa071bc7552cb439e5501e818?context=explore)).
**New features and improvements**
* #1839 – removed lightweight tag from page title. Now, only the version of Ketcher is shown in page title without any additional information 
* #1843 – added possibility to enable/disable redux-logger. New environment variable was introduced – `KETCHER_ENABLE_REDUX_LOGGER`, which is set to `false` by default.

**Bug fixes**
* #1795 added `render-coloring: true` to add colors when saving. Ketcher is able to properly export PNG and SVG images with colours.
* #1785 SMILES import fails if dearomotize-on-load is true.
* #427 'Calculated values' - Error messages are different in 'Remote' and 'Standalone' modes.