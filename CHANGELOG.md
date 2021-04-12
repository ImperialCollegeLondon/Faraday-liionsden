Changelog
---------
* 0.2
  * Select columns to import
  * Get data range storage working
  * REST API File Upload
  * DeviceConfig working properly
  * Device specification tree structure (MPTT)
    * Metadata inheritance down the tree
  * experiment devices list
  * column to parameter mapping
* 0.1
  * Ditched DJongo/Mongo - not fit for production IMHO
  * Created basic Django app to upload and view files ( #19)
    * Does not yet make use of Angular.js or any other frontend technology due to my lack of experience with such things. 'Djangular' helper module is no longer developed
  * Added support for "Data Ranges" to align with Luke's software
  * Started frontend development - added "django-plotly-dash' compoonent which promises to run Dash apps from within Django. This may allow re-use of some of the original Galvanalyser UI code.
