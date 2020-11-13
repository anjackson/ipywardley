# ipywardley
Bringing Wardley Map magic to Jupyter notebooks

[![PyPI version](https://badge.fury.io/py/ipywardley.svg)](https://badge.fury.io/py/ipywardley)

## Introduction

This plugin makes it easy to generate [Wardley Maps](https://wardley-maps-community.github.io/awesome-wardley-maps/) using [Jupyter Notebooks](https://jupyter.org/).

It supports a subset of the syntax defined by the [Online Wardley Maps](https://onlinewardleymaps.com/) service. This simple language can be use to specify the map via the `%%wardley` cell magic. [See this example notebook for a detailed introduction](https://github.com/anjackson/ipywardley/blob/main/test/wardley-maps.ipynb).

## Screenshot

![example-map](https://github.com/anjackson/ipywardley/blob/main/doc/example.png)

## To Do

- Support more of [the OWM syntax and features](https://onlinewardleymaps.com/#usage) (?=maybe?):
  - [ ] `evolution Novel->Emerging->Good->Best` and `evolution X` offering the [different sets of x-axis labels](https://twitter.com/swardley/status/1326583279139627008/photo/1). 
  - [ ] `y-axis Value Chain->Invisible->Visible` or `y-axis none` to make 'Visibility' axis optional.
  - [ ] `evolve`
  - [ ] `annotation` & `annotations`?
  - [ ] `note`?
  - [ ] `market` nodes?
  - [ ] `pipeline` nodes?
  - [ ] node `inertia`?
  - [ ] `+<>`, `+>`, `+<` links to indicate flow?
  - [ ] `Hot Water+'$0.10'>Kettle` flow labels?
  - [ ] `build`, `buy`, `outsource` node augmentation?
  - [ ] `submap` and related syntax?
  - [ ] `pioneer`, `settler`, `townplanner` areas/boxes?
- [ ] Add 'Uncharted' and 'Industrialised' labels
- [ ] Support rendering from a file, via e.g. `%wardley file=example.owm style=plain`
- [ ] Make it easier to download the SVG/rendered version?