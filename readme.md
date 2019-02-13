### Aderyn Data Search

The Aderyn Data Search plugin allows direct searching of the LERC Wales merged database.
LERC Wales are a consortium of the four Welsh LERCs (Local Environmental Record Centres). 
Assembled serveral years ago - and constantly updated - the database contains almost 12 million wildlife records from accross Wales.
Access to the merged database is restricted due to the sensitive nature of many of the records. However, direct access is available to partner organisations and thsoe with service level agreements with LERC Wales.  

To learn more about LERC Wales, visit https://www.lercwales.org.uk/

The plugin allows a user to enter a UK grid reference and search for categories of species within a buffered distance of that grid reference.
The resuting data is then written to shape files (and CSV if requested) and displayed within QGIS.

### How to Use the Plugin

1.  Access to the merged database is restricted due to the sensitive nature of many of the records. If you are a partner organisation or have an SLA with LERC Wales, contact us to obtain a username and password for the database.
2.  Enter the database settings (username, password and IP address) in the setting window (Database > Aderyn Data Search > Settings). Once saved, use the 'Test Database Connection' button in the main window to ensure a record is returned from the database.
3.  Ensure the map view is in OSGB36 (EPSG:27700) projection.
4.  Enter a grid reference in the location box and click 'Locate' to pan/zoom the map.
5.  Enter a search name (this will be used to name the exported files).
6.  Select the output folder where the shape files will be saved.
7.  Select the required categories. If a category is selected, a buffer distance must be specified.
8.  If you require a CSV (comma separated value) file for each shape file, select the CSV box.
9.  Click OK run the search. The results will be displayed within QGIS. 

### Help & Support

This plugin has been developed by the BIS (Biodiversity Information Service https://www.bis.org.uk/).
Please contact BIS with any questions you may have about the plugin or with suggestons for further development.

The GitHub repository can also be used to log issues and suggest enhancements - https://github.com/stevegoddard/aderyn-qgis-plugin.