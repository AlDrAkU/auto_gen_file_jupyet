%load_ext autoreload
%autoreload 2
from new_notebook import NotebookCreatorWidget
NotebookCreatorWidget()

from ipywidgets import IntSlider
from ipywidgets.embed import embed_minimal_html

slider = IntSlider(value=40)
embed_minimal_html('export.html', views=[NotebookCreatorWidget()], title='Widgets export')

import ipywidgets.embed