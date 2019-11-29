from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase): #1

    def setUp(self): #2 시작전
        self.browser = webdriver.Chrome(executable_path='/Users/ymkim/Downloads/chromedriver')
        self.browser.implicitly_wait(3) # 암묵적 대기? 복잡한곳에서는 명시적인 대기 알고리즘 별도 작성 필요
    
    def tearDown(self): #3 시작후
        self.browser.quit()

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

        # 엔터키를 치면 페이지가 갱신되고, 작업 목록에
        # 1. 공작깃털 사기 추가
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작 깃털 사기' for row in rows),
            "신규 작업이 테이블에 표시되지 않는다" # 사용자 정의 메시지 인수 지정
        )
        
        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자 존재
        # 다시 "그물만들기" 입력
        self.fail('Finish the test!')

        # 페이지 리로딩, 아이템 2개 목록에 출력

if __name__ == '__main__':
    unittest.main(warnings='ignore')
