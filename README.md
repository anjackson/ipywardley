# ipywardley
Bringing Wardley Map magic to Jupyter notebooks

[![PyPI version](https://badge.fury.io/py/ipywardley.svg)](https://badge.fury.io/py/ipywardley)

## Introduction

This plugin makes it easy to generate [Wardley Maps](https://wardley-maps-community.github.io/awesome-wardley-maps/) using [Jupyter Notebooks](https://jupyter.org/).

It supports a subset of the syntax defined by the [Online Wardley Maps](https://onlinewardleymaps.com/) service. This simple language can be use to specify the map via the `%%wardley` cell magic. [See this example notebook to see how it works](https://github.com/anjackson/ipywardley/blob/main/test/wardley-maps.ipynb).

![example-map](https://github.com/anjackson/ipywardley/blob/main/doc/example.png)

## To Do

- [ ] Support most/all of the OWM syntax and features.
- [ ] Support rendering from a file, via e.g. `%wardley file=example.owm style=plain`
- [ ] Make it easier to download the SVG/rendered version?