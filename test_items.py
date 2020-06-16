link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_cart_add(browser):
    
    browser.implicitly_wait(10)
    browser.get(link)

    try:
        browser.find_element_by_id("add_to_basket_form")

    except:
        assert False, "There is no button to add goods to the basket"

