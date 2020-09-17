from selenium import webdriver
import time

class GoogleBot(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "https://google.com"
        self.driver.get(self.url)
        time.sleep(2)
        self.terms = []
        self.googled_terms = []
        
    
    def get_terms(self):
        with open("terms_to_google.txt") as file:
            for line in file:
                line = line.replace("\n", "")
                self.terms.append(line)
        #print(self.terms)
                
    def grab_url(self):
        main_div = self.driver.find_element_by_id("rso")
        g_div_tags = main_div.find_elements_by_class_name("g")
        first_tag = g_div_tags[1]
        a_tag = first_tag.find_element_by_tag_name("a")
        link = a_tag.get_attribute("href")
        print(link)
        self.googled_terms.append(link)
        print("**************\n\n")

    def write_result(self):
        with open("terms_googled.txt", "w") as file:
            for term in self.googled_terms:
                file.write(term + "\n")


    def search_for_term(self):
        for term in self.terms:
            print(f"[+] Googling {term} ...")
            search_box = self.driver.find_element_by_name("q")
            search_box.clear()
            search_box.send_keys(term)
            submit_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]")
            submit_button.click()
            time.sleep(5)
            self.grab_url()
            time.sleep(5)
            self.driver.get(self.url)
 
    def close_session(self):
        print("[-] Clossing Session ...")
        self.driver.close()


if __name__ == "__main__":
    google_instance = GoogleBot()
    google_instance.get_terms()
    google_instance.search_for_term()
    google_instance.write_result()
    google_instance.close_session()

