from selenium import webdriver
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
        self.fail('Finish the test!') #6 강제로 테스트 실패 발생?

if __name__ == '__main__': #7
    unittest.main(warnings='ignore') #8

    # 작업 추가

    # 텍스트 상자에 입력
    # (취미는 날치 잡이용 그물 만들기)

    # 엔터키를 치면 페이지가 갱신되고, 작업 목록에
    # 1. 블라블라

    # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자 존재
    # 다시 "그물만들기" 입력

    # 페이지 리로딩, 아이템 2개 목록에 출력
