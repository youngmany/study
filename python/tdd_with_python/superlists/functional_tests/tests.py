from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase): #1

    def setUp(self): #2 시작전
        self.browser = webdriver.Chrome(executable_path='/Users/ymkim/Downloads/chromedriver')
        self.browser.implicitly_wait(3) # 암묵적 대기? 복잡한곳에서는 명시적인 대기 알고리즘 별도 작성 필요
    
    def tearDown(self): #3 시작후
        self.browser.quit()

    # Helper Method
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self): #4
        # Web Site 확인
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고있다.
        self.assertIn('To-Do', self.browser.title) #5 aseertEqul, True, False도 있음
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 작업 추가
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        # "공작깃털 사기"라고 텍스트 상자에 입력
        # (취미는 날치 잡이용 그물 만들기)
        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: 공작깃털 사기')
        
        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자 존재
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        # 페이지 리로딩, 아이템 2개 목록에 출력
        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        self.fail('Finish the test!')

        # 페이지 리로딩, 아이템 2개 목록에 출력

if __name__ == '__main__':
    unittest.main(warnings='ignore')
