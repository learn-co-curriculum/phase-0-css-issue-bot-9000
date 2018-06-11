require "pry"

RSpec.describe 'styling' do
  context 'within style.css' do
    it 'corrects the body background declaration' do
      selector = parsed_css.find_by_selector('body')[0]
      expect(selector).to include("background: pink;"), "Missing properly formatted body declaration"
    end
    
    it 'corrects the h1 font size declaration' do
      selector = parsed_css.find_by_selector('h1')[0]
      expect(selector).to include("font-size: 3em;"), "Missing properly formatted h1 font size declaration"
    end
    
    it 'corrects the h2 font weight declaration' do
      selector = parsed_css.find_by_selector('h2')[0]
      expect(selector).to include("font-weight: normal;"), "Missing properly formatted h2 font weight declaration"
    end
    
    it 'corrects the .completed font family declaration' do
      selector = parsed_css.find_by_selector('.completed')[0]
      expect(selector).to include("font-size: 12px;"), "Missing properly formatted .completed font size declaration"
    end
    
    it 'corrects the #tasks .completed background declaration' do
      selector = parsed_css.find_by_selector('#tasks .completed')[0]
      expect(selector).to include("background: #ccc;"), "Missing properly formatted #tasks.completed background declaration"
    end
  
  end
  
end

