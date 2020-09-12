from selenium import webdriver
import time

class GoogleBot(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "https://google.com"
        self.driver.get(self.url)
        time.sleep(2)
        self.terms = []
        
    
    def get_terms(self):
        with open("terms_to_google.txt") as file:
            for line in file:
                line = line.replace("\n", "")
                self.terms.append(line)
        #print(self.terms)
                
    
    def search_for_term(self):
        for term in self.terms:
            search_box = self.driver.find_element_by_name("q")
            search_box.clear()
            search_box.send_keys(term)
            submit_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]")
            submit_button.click()
            time.sleep(10)
            self.driver.get(self.url)



        
    def close_session(self):
        self.driver.close()


if __name__ == "__main__":
    google_instance = GoogleBot()
    google_instance.get_terms()
    google_instance.search_for_term()
    google_instance.close_session()

