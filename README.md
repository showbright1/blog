## Me Blog ##

This is the repo of my blog powered by [Pelican](http://getpelican.com). I've used a custom theme which you can find in the bootstrap-pelican directory. I am still working out where exactly I want to host this badboy. 

## Building ##

The theme is symlinked to the content via `pelican-themes --symlink ~/blog/bootstrap-pelican`

### Make File ###

The fabric file is a decent example of working with this type of project, but had proved difficult to tame with my limited experience with Fabric. I say that to say ths; The make file combined with [ghp-import](https://github.com/davisp/ghp-import) works flawlessly out of the box. `make publish` ... and BAM! the blog/documentation is up and running.

### Fabric ###

A fabric file is included to help automate as much as possible. The less friction for posting and making pages the better...

So here are the steps:

1. `cd /path/to/blog` (where the fabfile.py lives) 
2. Now its go time and there are three choices (for now...)
  - `fab pelican` simply generates the blog
  - `fab push: "commit message"` pushs the current structure to github
  - `fab publish: "commit message"` generates new content and pushes
