# GiellaLT unimorph support

[Unimorph](https://unimorph.github.io) is a project for "universal" encoding of
morphology and collection of full-form annotated inflection lists.

There are the following python modules with CLI interface for converting stuff:

* `giellaltconversiontools.giella2unimorph` converts pairstrings from
  `hfst-fst2strings` into unimorph
* `giellaltconversiontools.unimorph2fstlookup` converts from unimorph data to
  `hfst-lookup` output style
* `giellaltconversiontools.unimorph2yamltest` converts from unimorph data to
  YAML format used for testing in [morphtest]()
* `giellaltconversiontools.unimorphevalanalyser` takes a GiellaLT analyser and
  unimorph data and counts precision, recall and some F score

You can execute them by running `python -m MODULNAVN` where MODULNAVN is one of
the abovementioned.

There are some helper bash scripts for unimoprh generation in `scripts/`

* `generate.bash` can take unimorph data and generate giellalt version in same
  order; can be used to send updates to unimorph
* `generate-from-lexicons.bash` takes `stems/*.lexc` files and generates
  unimorph database from all lemmas it finds and can tag somehow

Also a data file to hack around some FSA problems:

* `excluded.tags` is list of tags that FSA ignores when generating or analysing
  for unimorph, e.g. compounding and derivation

