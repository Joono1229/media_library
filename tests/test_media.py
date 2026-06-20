import pytest
from media_library import Media, Book, Movie

# [정상 케이스 1] Media 객체가 올바르게 생성되고 정보를 출력하는지 테스트
def test_media_creation():
    m = Media("인셉션", "SF", 2010)
    assert m.title == "인셉션"
    assert m.genre == "SF"
    assert m.year == 2010
    assert m.display_info() == "[SF] 인셉션 (2010)"

# [엣지 케이스 2] Media 연도에 문자열 등 잘못된 타입이 들어왔을 때 에러 처리 테스트
def test_media_invalid_year_type():
    with pytest.raises(ValueError):
        Media("오류 영화", "액션", "이천이십육년")

# [엣지 케이스 3] Media 연도가 허용 범위(1000~3000)를 벗어났을 때 에러 처리 테스트
def test_media_invalid_year_boundary():
    with pytest.raises(ValueError):
        Media("과거 책", "역사", 999)
    with pytest.raises(ValueError):
        Media("미래 영화", "SF", 3001)

# [경계값 케이스 4] Media 연도의 최소/최대 경계값(1000, 3000)이 정상 작동하는지 테스트
def test_media_year_exact_bounds():
    m1 = Media("고려사", "역사", 1000)
    m2 = Media("서기3000년", "SF", 3000)
    assert m1.year == 1000
    assert m2.year == 3000

# [정상 케이스 5] Book 객체의 정보 출력(오버라이딩)이 정상 작동하는지 테스트
def test_book_creation():
    b = Book("파이썬 마스터", "IT", 2025, 350)
    assert b.display_info() == "[IT] 파이썬 마스터 (2025) - 350쪽"

# [엣지 케이스 6] Book의 페이지 수가 제한 조건(400쪽)을 초과했을 때 에러 처리 테스트
def test_book_pages_overflow():
    with pytest.raises(ValueError):
        Book("너무 두꺼운 책", "소설", 2026, 401)

# [경계값 케이스 7] Book의 페이지 수가 정확히 400쪽(경계값)일 때 정상 작동하는지 테스트
def test_book_pages_exact_bound():
    b = Book("딱 맞춘 책", "소설", 2026, 400)
    assert b.pages == 400

# [정상 케이스 8] Movie 객체의 정보 출력(오버라이딩)이 정상 작동하는지 테스트
def test_movie_creation():
    m = Movie("기생충", "드라마", 2019, "봉준호", 132)
    assert m.display_info() == "[드라마] 기생충 (2019) - 봉준호 감독"

# [정상 케이스 9] Movie 고유 메서드인 play()가 정상 문자열을 반환하는지 테스트
def test_movie_play():
    m = Movie("아바타", "SF", 2009, "제임스 카메론", 162)
    assert m.play() == "아바타 재생을 시작합니다. (162분)"