Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================
.. include:: ./readme.rst


.. toctree::
   :hidden:
   :glob:

   installation
   usage
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
