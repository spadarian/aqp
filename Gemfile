source "https://rubygems.org"

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

# gem "jekyll", "3.3.1"
gem "jekyll", versions['jekyll']
gem "jekyll-sitemap"
gem "pygments.rb"

gem 'github-pages', versions['github-pages']
