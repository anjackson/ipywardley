# ipywardley
Bringing Wardley Map magic to Jupyter notebooks

[![PyPI version](https://badge.fury.io/py/ipywardley.svg)](https://badge.fury.io/py/ipywardley)

## Introduction

This plugin makes it easy to generate [Wardley Maps](https://wardley-maps-community.github.io/awesome-wardley-maps/) using [Jupyter Notebooks](https://jupyter.org/).

It supports a subset of the syntax defined by the [Online Wardley Maps](https://onlinewardleymaps.com/) service. This simple language can be use to specify the map via the `%%wardley` cell magic. 

## Try it out!

Run on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/anjackson/ipywardley/main?filepath=test%2Fwardley-maps.ipynb) or [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anjackson/ipywardley/blob/main/test/wardley-maps.ipynb)

## Installation

First, [install Jupyter](https://jupyter.org/install). Then before running it, install `ipywardley`. e.g. if you are using pip:

    pip install ipywardley
    
Then, run Jupyter:

    jupyter-lab
    
## Usage

Open up a new Python 3 notebook, and use this command to enable the module:

    %load_ext ipywardley
    
Now you can use the `%%wardley` directive and create maps. [See this example notebook for a detailed example of how to do this](https://github.com/anjackson/ipywardley/blob/main/test/wardley-maps.ipynb).

## Screenshot

![example-map](https://github.com/anjackson/ipywardley/blob/main/doc/example.png)

## To Do

- Support more of [the OWM syntax and features](https://onlinewardleymaps.com/#usage) (?=maybe?):
  - [ ] `evolution Novel->Emerging->Good->Best` and `evolution X` offering the [different sets of x-axis labels](https://twitter.com/swardley/status/1326583279139627008/photo/1). 
  - [ ] `y-axis Value Chain->Invisible->Visible` or `y-axis none` to make 'Visibility' axis optional.
  - [ ] `evolve`
  - [ ] `annotation` & `annotations`?
  - [x] `note`?
  - [ ] `market` nodes?
  - [ ] `pipeline` nodes?
  - [ ] node `inertia`?
  - [x] `+<>` links to indicate flow.
  - [ ] `+>` links to indicate flow.
  - [ ] `+<` links to indicate flow.
  - [ ] `Hot Water+'$0.10'>Kettle` flow labels?
  - [ ] `build`, `buy`, `outsource` node augmentation?
  - [ ] `submap` and related syntax?
  - [ ] `pioneer`, `settler`, `townplanner` areas/boxes?
- [ ] Add 'Uncharted' and 'Industrialised' labels
- [ ] Support rendering from a file, via e.g. `%wardley file=example.owm style=plain`
- [ ] Make it easier to download the SVG/rendered version?

## Development

1. Clone this directory.
2. Set up a `virtualenv` and activate it.
3. Modify the code.
4. Run `flit install`
5. Run `jupyter-lab` and test your changes.
6. Repeat 3-5 _ad infinitum_.
7. Turn your changes into a pull request.


## Change Log

- 0.0.6:
  - [Added support for the bluelines +<> within Wardley Maps code.](https://github.com/anjackson/ipywardley/pull/7)
  - [Updated to support additional characters within nodes and evolve code lines](https://github.com/anjackson/ipywardley/pull/8)
  - [Default to 'wardley' style if no style provided.](https://github.com/anjackson/ipywardley/pull/9)
  - [Draw evolve lines within the map.](https://github.com/anjackson/ipywardley/pull/10)
  - [Add the red evolve nodes to the map.](https://github.com/anjackson/ipywardley/pull/11)
- 0.0.5:
  - [Updated the 'b' parameter to 'visibility' as 'b' now depreciated.](https://github.com/anjackson/ipywardley/pull/6)

