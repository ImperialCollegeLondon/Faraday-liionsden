Galvanalyser / LiIonsDen project summary
-----------------------------------------

Galvanalyser / LiIonsDen is a Web application comprising a database of electrochemical (Lithium Battery) experimental test data, ie Cyclic Voltammetry. Users (scientists) may upload data files from Battery Cycler machines via either the Web interface, or via an automated tool/API. Supported cycler formats include Biologic and Maccor.
Users can then view data as a graph via the web interface, whereby multiple data sets (e.g. cycles of the same cell, different cells, different tests) can be displayed on the graph. 
The Web App was originally developed by Luke Pitt (Oxford Robotics Institute) and was later refactored by Ivan Kotegov (Imperial College London). Luke continues development on his own branch.
The web app is based on the Dash/Plotly framework, which is aimed at creating data science web apps very quickly, with interactive graphs. 
Ivan's refactoring aimed to improve the flexibility and scalability of the database by switching to a schema-less, cloud-hosted MongoDB backend, Azure CosmosDB. This effort was part-completed, and implemented a very basic feature set.
Luke's efforts aimed at adding more features to the original version, and the two branches diverged significantly.
However, Luke's branch is written in a style which does not make it easy to maintain, extend or deploy to a production environment. For example, using "hard-coded" SQL.

I have been contracted to take over development of this Web App from both Ivan and Luke, and deliver a system that combines features of both branches, while adding new features such as automated data analysis, enhanced metadata, protocol description, and support for additional cycler types.
My approach so far has been to implement the database in a more popular Web framework (Django/PostgreSQL). This has proved very successful - the database and web model/view framework is implemented with minimal code, making it much easier to maintain - and the Django/PostgreSQL stack is proven for scalability. PostgreSQL also allows for high-performance ArayField representation of datasets, instead of storing all data points from all experiments in a single table of billions of rows (which was the approach taken by the first iteration of the app).
I was also able to include the parser code for Cycler data files from the original project, which I have improved to extract more of the metadata provided by the cycler.
However, mostly due to my relative lack of experience in frontend web technologies, the frontend has proven time-consuming to implement. I am currently investigating using a module called django-plotly-dash which may enable me to run some of Luke's frontend code, by embedding a Plotly/Dash app within Django. However, due to Luke's custom extensions of Dash, this is also proving difficult.

My code, documentation and agile issues board can be found at https://gitlab.com/towen/faraday-liionsden  (private project - account & authorisation required for access)
A log of changes and ideas can be found in (djongoTest/README.md)

Ongoing plan:
* Create prototype pre-acceptance documentation e.g. Use Case storyboards.
* Continue following issues board & ideas log.


Ideas drawn from:
* [The original liionsden project by Ivan & Luke at Imperial & Oxford](https://github.com/FaradayInstitution/liionsden)
* [Universal Battery Database by Samuel Buteau](https://github.com/Samuel-Buteau/universal-battery-database)
* Inspiration from commerical products such as [Voltaiq](http://www.voltaiq.com)
* Cycler machines software e.g. Biologic BT-Lab
