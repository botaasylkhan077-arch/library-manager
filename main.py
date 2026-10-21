# Electronic Library Manager - Электрондық кітапхана жүйесі

books = [
    {"id": 1, "title": "Абай жолы", "author": "Мұхтар Әуезов", "available": True},
    {"id": 2, "title": "Қан мен тер", "author": "Әбдіжәміл Нұрпейісов", "available": True},
    {"id": 3, "title": "Көксерек", "author": "Мұхтар Әуезов", "available": False},
    {"id": 4, "title": "Менің Кітабым", "author": "Асылхан Ақбота", "available": True}
]

def show_books():
    print("\n--- Кітаптар тізімі ---")
    if not books:
        print("Кітапхана бос.")
    else:
        for book in books:
            status = "Қолжетімді" if book["available"] else "Берілген (Қолда жоқ)"
            print(f"ID: {book['id']} | Атауы: {book['title']} | Авторы: {book['author']} | Жағдайы: {status}")
    input("\nКері өту үшін Enter пернесін басыңыз...")

def add_book():
    print("\n--- Жаңа кітап қосу ---")
    title = input("Кітаптың атауын енгізіңіз: ")
    author = input("Авторын енгізіңіз: ")
    new_id = len(books) + 1
    books.append({"id": new_id, "title": title, "author": author, "available": True})
    print(f"'{title}' кітабы сәтті қосылды!")
    input("\nҚайту үшін Enter пернесін басыңыз...")

def search_book():
    print("\n--- Кітапты іздеу ---")
    query = input("Кітап атауын немесе авторын енгізіңіз: ").lower()
    found = [b for b in books if query in b['title'].lower() or query in b['author'].lower()]
    
    if found:
        print(f"Табылған кітаптар саны: {len(found)}")
        for book in found:
            status = "Қолжетімді" if book["available"] else "Берілген"
            print(f"- {book['title']} ({book['author']}) - {status}")
    else:
        print("Сәйкес келетін ешқандай кітап табылмады.")
    input("\nҚайту үшін Enter пернесін басыңыз...")

def show_books_quick():
    print("\nҚолдағы кітаптар:")
    for book in books:
        status = "Бар" if book["available"] else "Берілген"
        print(f"ID: {book['id']} | {book['title']} ({status})")

def toggle_availability():
    print("\n--- Кітаптың қолжетімділігін өзгерту ---")
    show_books_quick()
    try:
        book_id = int(input("Күйін өзгерткіңіз келетін кітаптың ID нөмірін енгізіңіз: "))
        for book in books:
            if book["id"] == book_id:
                book["available"] = not book["available"]
                status = "Қолжетімді" if book["available"] else "Қолда жоқ"
                print(f"Кітап күйі өзгертілді. Жаңа күйі: {status}")
                input("\nҚайту үшін Enter пернесін басыңыз...")
                return
        print("Бұл ID бойынша кітап табылмады.")
    except ValueError:
        print("Қате! Дұрыс сан енгізіңіз.")
    input("\nҚайту үшін Enter пернесін басыңыз...")

def main():
    while True:
        print("\n=== Library Manager Мәзірі ===")
        print("1. Кітаптар тізімін көру")
        print("2. Жаңа кітап қосу")
        print("3. Кітап іздеу (атауы/авторы)")
        print("4. Кітаптың қолжетімділігін өзгерту")
        print("5. Шығу")
        
        choice = input("Әрекетті таңдаңыз (1-5): ").strip()
        
        if choice == '1':
            show_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            toggle_availability()
        elif choice == '5':
            print("Бағдарлама жұмысы аяқталды. Сау болыңыз!")
            break
        else:
            print("Қате таңдау! 1 мен 5 аралығындағы сан енгізіңіз.")

if __name__ == "__main__":
    main()