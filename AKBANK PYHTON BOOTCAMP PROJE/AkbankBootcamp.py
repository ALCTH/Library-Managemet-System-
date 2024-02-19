class book :                                                                                 # kitap nesnemizi ve özelliklerini tanımlıyoruz 
    def __init__(self , bookname, author , release_date , numberof_pages):
        self.bookname = bookname
        self.author = author
        self.release_date = release_date
        self.numberof_pages = numberof_pages
        def __str__(self):                                                                   # nesnemizi okuyabilmemiz için özelliklerini içeren fonksiyonur.
         return f"{self.name}, {self.author}, {self.release_date}, {self.num_pages}"
        
class library:                                                                               # Kütüphane nesnemizi tanımlıyoruz
   def __init__(self , database_file):                                                       # Kitap verilerini saklamak için kullandığım dosya 
      self.database_file = database_file
      self.books = []
      def load_books(self):                                                                  #Kitap verilerini dosyadan kütüphane listesine yüklemek için kullandığım fonskiyon , eğer dosyayı bulamazsa hata oluşturmaması da sağlandı 
         try:
           with open(self.database_file, "+a") as  file:
            for line in file:
               book_info = line.strip().split(",")                                           #Webinarda bahsedildiği üzere aynı kitabın verileri arasında virgül olmasına ve daha düzenli gözükmesine yarar. 
               book = book(*book_info)
               self.books.append(book)

         except FileNotFoundError:
                 pass
         def save_books(self):                                                                # Kütüphandeki kitapları dosyaya kaydeder 
            with open(self.database_file , "+a") as file:
             for book in self.books:
                file.write(str(book) + '\n')
         def add_book(self, book):                                                            # Kütüphaneye kitap eklemek için kullandığım fonksiyon
            self.books.append(book)
            self.save_books()
      
         def remove_book(self, author, book_name):                                            # Yazar ve kitap adı girildiğinde kütüphane listesini kontrol ederek girilen kitap listede varsa o kitabı siler yok ise hata verir.
            removed_books = [book for book in self.books if book.author == author and book.name == book_name]

            if removed_books:
               self. books = [book for book in self.books if book not in removed_books]
               self.save_books()
               print(f"Books by {author} with the name '{book_name}' removed successfully.")
            else:
              print(f"No books found by {author} with the name '{book_name}'.")
           
         def display_book(self,book):                                                          # Kütüphane listesini ekrana basmaya yarayan fonksiyon 
            for i , book in enumerate(self.books , 1):
               print(f"{i}. {book}")

def main():
   library = library("books.txt")                                                               # books.txt dosyasına kitaplar aktarılıyor.
   library.load_books()
           
   while True : 
                print("**** Library Management Menu**** \n")                                    # Ana menü ve seçenekleri ekrana bastırıyoruz.
                print(" Press 1 to add a book...")
                print(" Press 2 to display all books")
                print(" Press 3 to remavo a book from the library")
                print("Press 4  to Exit")
                process = input("Which aciton do you want to take")                             # Hangi işlemi yapmak istediğini kullanıdan alıyoruz 
                if process == "1":                                                              # Kullanıcının 1 girmesi halinde yeni kitap ekleme işlemi karşımıza çıkıyor ve eklenecek kitabın yukarıda tanımladığımız özelliklerini kullanıcıdan alıyor 
                   name = input("Enter book name: ")
                   author = input("Enter author name: ")
                   release_date = input("Enter release date: ")
                   num_pages = input("Enter number of pages: ")
                   new_book = book(name,author,release_date,num_pages)
                   library.add_book(new_book)
                   print("...Book added succsesfully...")
                elif process == "2":                                                            # Kullanıcının 2 girmesi durumunda kütüphane listesindeki kitapları ekrana basıyor 
                   if not library.book:
                      print("No books in the library.")
                   else:
                      print("List of Books:")
                      library.display_books()
                elif process == "3":                                                            # Kullanıcının 3 girmesi halinde kullanıcıdan kitap adı ve yazarı alarak alınan bilgileri içeren kitap listede bulunuyorsa onu siler yoksa kitabın listede olmadığını söyler
                    if not library.books:
                     print("No books in the library to remove.")
                    else:
                     author_to_remove = input("Enter the author's name of the book to remove: ")
                     book_name_to_remove = input("Enter the name of the book to remove: ")
                     library.remove_book(author_to_remove, book_name_to_remove)
                elif process == '4':                                                            # Kütüphane yönetim sisteminden çıakr
                     print("Exiting the Library Management System.")
                     break
                else:                                                                           # Geçersiz bir giriş olduğunda uyarı verir
                      print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
   main()                                                                                       # main fonksiyonunun çağırıldığı yer 



         


