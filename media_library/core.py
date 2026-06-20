class Media:
    """도서와 영화의 공통 속성을 정의하는 부모 클래스입니다."""

    def __init__(self, title, genre, year):
        """
        Media 객체를 초기화합니다.

        :param title: 미디어의 제목
        :param genre: 미디어의 장르
        :param year: 출시(출판) 연도
        
        >>> m = Media("인셉션", "SF", 2010)
        >>> m.title
        '인셉션'
        """
        self.title = title
        self.genre = genre
        self.year = self._validate_year(year)

    def _validate_year(self, year):
        """
        입력된 연도가 유효한지 검사하는 비공개(private) 메서드입니다.
        
        :param year: 검사할 연도
        :return: 유효한 연도
        """
        if type(year) is not int or year < 1000 or year > 3000:
            raise ValueError("유효하지 않은 연도입니다.")
        return year

    def display_info(self):
        """
        미디어의 기본 정보를 보기 좋은 문자열로 반환합니다.

        :return: 장르, 제목, 연도가 포함된 포맷팅 문자열
        
        >>> m = Media("듄", "SF", 2021)
        >>> m.display_info()
        '[SF] 듄 (2021)'
        """
        return f"[{self.genre}] {self.title} ({self.year})"