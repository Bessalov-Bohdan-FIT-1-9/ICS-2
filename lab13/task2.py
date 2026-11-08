import reader

r1 = reader.Reader("Коваленко О.П.", "12345", "01.03.2003")
r2 = reader.Reader("Петренко І.М.", "67890", "15.07.2004")
r3 = reader.Reader("Сидорук А.В.", "11223", "22.11.2002")

r1.add_book("Кобзар")
r1.add_book("Тіні забутих предків")
r1.show_current_books()
r1.return_book("Кобзар")
r1.show_current_books()
r1.show_read_books()

r2.add_book("Захар Беркут")
r2.show_current_books()

r3.add_book("Місто")
r3.return_book("Місто")
r3.show_read_books()