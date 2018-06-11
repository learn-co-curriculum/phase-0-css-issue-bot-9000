require 'bundler'
Bundler.require
require 'yaml'

RSpec.configure do |config|
  
end

def html_file_contents
  File.read('./index.html')
end

def parsed_html
  Nokogiri::HTML(html_file_contents) do |config|
    config.strict.dtdload.dtdvalid.noblanks
  end
end

def parsed_css
  parser = CssParser::Parser.new
  parser.load_uri!('./css/style.css')
  parser
end
