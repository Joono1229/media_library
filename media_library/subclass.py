from .core import Media


class Book(Media):
    """도서 정보를 관리하는 자식 클래스입니다."""

    def __init__(self, title, genre, year, pages):
        """
        Book 객체를 초기화합니다. 페이지 수는 400쪽을 초과할 수 없습니다.

        :param title: 책 제목
        :param genre: 책 장르
        :param year: 출판 연도
        :param pages: 페이지 수 (최대 400)

        >>> b = Book("파이썬 기초", "교육", 2023, 300)
        >>> b.pages
        300
        """
        super().__init__(title, genre, year)
        self.pages = self._validate_pages(pages)

    def _validate_pages(self, pages):
        """
        페이지 수가 400을 넘는지 검사하는 비공개 메서드입니다.

        :param pages: 검사할 페이지 수
        :return: 유효한 페이지 수
        """
        if pages > 400:
            raise ValueError("페이지 수는 400쪽을 초과할 수 없습니다.")
        return pages

    def display_info(self):
        """
        책의 상세 정보를 반환합니다. 부모 클래스의 메서드를 오버라이딩합니다.

        >>> b = Book("파이썬 기초", "교육", 2023, 300)
        >>> b.display_info()
        '[교육] 파이썬 기초 (2023) - 300쪽'
        """
        base_info = super().display_info()
        return f"{base_info} - {self.pages}쪽"


class Movie(Media):
    """영화 정보를 관리하는 자식 클래스입니다."""

    def __init__(self, title, genre, year, director, running_time):
        """
        Movie 객체를 초기화합니다.

        :param title: 영화 제목
        :param genre: 영화 장르
        :param year: 개봉 연도
        :param director: 감독 이름
        :param running_time: 상영 시간(분)

        >>> m = Movie("인터스텔라", "SF", 2014, "크리스토퍼 놀란", 169)
        >>> m.director
        '크리스토퍼 놀란'
        """
        super().__init__(title, genre, year)
        self.director = director
        self.running_time = running_time

    def play(self):
        """
        영화를 재생하는 가상의 동작을 수행합니다.

        >>> m = Movie("인터스텔라", "SF", 2014, "크리스토퍼 놀란", 169)
        >>> m.play()
        '인터스텔라 재생을 시작합니다. (169분)'
        """
        return f"{self.title} 재생을 시작합니다. ({self.running_time}분)"

    def display_info(self):
        """
        영화의 상세 정보를 반환합니다. 부모 클래스의 메서드를 오버라이딩합니다.

        >>> m = Movie("인터스텔라", "SF", 2014, "크리스토퍼 놀란", 169)
        >>> m.display_info()
        '[SF] 인터스텔라 (2014) - 크리스토퍼 놀란 감독'
        """
        base_info = super().display_info()
        return f"{base_info} - {self.director} 감독"
