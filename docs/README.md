LiIonsDen Electrochemistry Database
-----------------------------------------

Liionsden is a Web application comprising a database of electrochemical (Lithium Battery) experimental test data, ie Cyclic Voltammetry. Users (scientists) may upload data files from Battery Cycler machines via either the Web interface, or via an automated tool/API. Supported cycler formats include Biologic and Maccor.
Users can then view data as a graph via the web interface, whereby multiple data sets (e.g. cycles of the same cell, different cells, different tests) can be displayed on the graph. 

Code, documentation and agile issues board can be found at https://gitlab.com/towen/faraday-liionsden (private project - account & authorisation required for access)
A log of changes and ideas can be found in (django-battdb/README.md)


Ideas drawn from:
* 'Galvanalyser' by Luke Pitt and Prof. David Howey
* [liionsden by Ivan Kotegov at Imperial College](https://github.com/FaradayInstitution/liionsden)
* [Universal Battery Database by Samuel Buteau](https://github.com/Samuel-Buteau/universal-battery-database)
* [dfndb](https://github.com/ndrewwang/dfndb) by @ndrewwang
* Inspiration from commerical products such as [Voltaiq](http://www.voltaiq.com)
* Cycler machines software e.g. Biologic BT-Lab

Screenshots:
![upload data via REST API](doc/screenshots/uploadFile.png)
![configure parameters via Web interface](doc/screenshots/change_parameter.png)
![Add academic paper cia Web interface](doc/screenshots/add_paper.png)