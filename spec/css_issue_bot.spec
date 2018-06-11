require "pry"

RSpec.describe 'styling' do
  context 'within style.css' do
    it 'fixes the body declaration' do
      selector = parsed_css.find_by_selector('body')[0]
      expect(selector).to include("background: pink;"), "Missing properly formatted body declaration"
    end
    # 
    # it 'sets div width to 700px' do
    #   selector = parsed_css.find_by_selector('div')[0]
    #   expect(selector).to include("width: 700px;"), "Missing properly formatted width declaration"
    # end
    # it 'sets div margin to auto' do
    #   selector = parsed_css.find_by_selector('div')[0]
    #   expect(selector).to include("margin: auto;"), "Missing properly formatted margin declaration"
    # end
    # it 'sets div font-family to Helvetica Neue' do
    #   selector = parsed_css.find_by_selector('div')[0]
    #   expect(selector).to include('font-family: "Helvetica Neue";'), "Missing properly formatted font-family declaration"
    # end
    # it 'sets div background to white' do
    #   selector = parsed_css.find_by_selector('div')[0]
    #   expect(selector).to include('background: white;'), "Missing properly formatted background declaration"
    # end
    # it 'sets div padding to 30px' do
    #   selector = parsed_css.find_by_selector('div')[0]
    #   expect(selector).to include('padding: 30px;'), "Missing properly formatted padding declaration"
    # end
    # # 
    # it 'sets #main-header font size to 22px' do
    #   selector = parsed_css.find_by_selector('#main-header')[0]
    #   expect(selector).to include("font-size: 22px;"), "Missing properly formatted font-size declaration"
    # end
    # 
    # it 'sets .perspective-questions font style to italic' do
    #   selector = parsed_css.find_by_selector('.perspective-questions')[0]
    #   expect(selector).to include("font-style: italic"), "Missing properly formatted font-style declaration"
    # end
  
  end
  
end

