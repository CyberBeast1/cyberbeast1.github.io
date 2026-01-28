meta-title:Title Is First Post
meta-desc:This is 1st post desctiption
meta-author:Cyber
meta-tags:markdown, demo, test, parser, first post
meta-random:

## New Features and Implementation Ideas for this site

> Ideas to implement Pagination


- create data.json(contains all page data) from python
    - change code where generating links into index.html
- make script.js which will add all post cards using dom 
- it will help in both search and pagination
- add `draft` meta data to md pages so that pages currently in progress don't get compiled

- Configuration file & extensibility:  
Almost every serious SSG supports a config file (YAML/TOML/JSON). This lets you specify things like site title, permalink patterns, date formats, RSS output, plugins, etc. Right now it’s all probably hard-coded or implicit. A config layer lets users adjust behavior without editing Python code (big UX win).

- No plugin ecosystem:  
By design your generator is minimal. That’s intentional. However, many SSGs support plugins — shortcodes, syntax highlighters, sitemap generators, RSS feeds, search indexing. Without those, you end up reinventing functionality each time.

`pactl list short sinks`  
`ffmpeg -f pulse -i alsa_output.pci-0000_00_1f.3.analog-stereo.monitor output.wav`  
`ffmpeg -f pulse -i @DEFAULT_SINK@.monitor -c:a libopus -b:a 160k output.opus`  

Volume normalization (post-process)  
`ffmpeg -i output.wav -af loudnorm normalized.wav`

