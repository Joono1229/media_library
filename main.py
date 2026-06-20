from media_library import Book, Movie


def main():
    print("=== Media Library 관리 시스템 작동 시작 ===\n")

    # 1. 도서 객체 생성 및 출력 테스트 (정상 케이스)
    print("[1] 도서 추가 테스트")
    try:
        book1 = Book("파이썬 프로그래밍", "IT/교육", 2024, 350)
        print(f"성공: {book1.display_info()}")
    except ValueError as e:
        print(f"실패: {e}")

    # 2. 도서 페이지 초과 제한 테스트 (에러 케이스)
    print("\n[2] 도서 페이지 제한(400쪽 초과) 테스트")
    try:
        book2 = Book("해리포터와 마법사의 돌", "소설", 2001, 500)
        print(f"성공: {book2.display_info()}")
    except ValueError as e:
        print(f"예외 처리 성공: {e} (예상된 오류)")

    # 3. 영화 객체 생성 및 재생 테스트
    print("\n[3] 영화 추가 및 재생 테스트")
    movie1 = Movie("인셉션", "SF", 2010, "크리스토퍼 놀란", 148)
    print(f"정보: {movie1.display_info()}")
    print(f"동작: {movie1.play()}")

    print("\n=============================================")
    print("모든 시스템이 정상적으로 작동합니다.")


if __name__ == "__main__":
    main()