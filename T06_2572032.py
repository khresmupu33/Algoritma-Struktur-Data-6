## Definisi Kelas ##
## Definisi Kelas MyListElement
## Nama: Khresna Mulia Putra (Khresmupu)
## NRP: 2572032

## Definisi Atribut:
# info  : atribut yang menyimpan nilai (integer)
# next  : atribut reference elemen berikutnya
#         (Node)
class MyListElement:
    def __init__(self,value):
        self.info=value
        self.next=None

## Definisi Atribut:
# first : elemen pertama dalam array(integer)
class MyList:
    def __init__(self):
        self.first=None
    # Q : Nilai yang diinput(MyListElement)
    def InsertFirst(self, Q):
        Q.next = self.first
        self.first = Q
    def traversal(self):
        if self.first==None:
            print("List kosong")
        else:
            p=self.first
            print("Linked list:",end=" ")
            while p!=None:
                print(f"|{p.info}| ",end="")
                p=p.next
            print() 
    # prev : Nilai yang akan dihapus(string)
    def removeLast(self):
        if self.first==None:
            return
        else:
            if self.first.next==None:
                Q = self.first
                self.first = None
            else:
                prev=self.first
                while prev.next.next!=None:
                    prev=prev.next
                Q=prev.next
                prev.next=None
            print("Hapus element: ",Q.info)
    # p     : sebuah pembantu pencari(string)
    # count : Alat cek posisi(int)
    def switchPosition(self):
        if self.first==None:
            return
        else:
            if self.first.next==None:
                print("Maaf, data masih kurang")
            else:
                pos1=int(input("Posisi-1: "))
                pos2=int(input("Posisi-2: "))
                P=self.first
                count=0
                while P != None:
                    count = count + 1
                    P = P.next
                if pos1 < 0 or pos2 < 0:
                    print("Posisi invalid")
                elif pos1 >= count or pos2 >= count:
                    print("Posisi tidak dapat lebih dari jumlah Node dalam list")
                elif pos1 == pos2:
                    print("Posisi tidak bisa sama")
                else:  
                    prev1=None
                    P1=self.first
                    for i in range(pos1):
                        prev1=P1
                        P1=P1.next
                    prev2=None
                    P2=self.first
                    for i in range(pos2):
                        prev2=P2
                        P2=P2.next
                    if prev1==None:
                        self.first=P2
                    else:
                        prev1.next=P2
                    if prev2==None:
                        self.first=P1
                    else:
                        prev2.next=P1
                    temp=P1.next
                    P1.next=P2.next
                    P2.next=temp

# Kamus Data (Main Program):
# p             : Gambaran objek list lagu
# tanyaObjek    : sebagai input(integer)
# pilih         : pilih menu (integer)
def main():
    p=MyList()
    while True:
        print("===================")
        print("Menu:")
        print("1. Insert First")
        print("2. Delete Last")
        print("3. Switch Position")
        print("0. Exit")
        pilih=int(input("Pilih menu: "))
        if pilih<0 or pilih>3:
            print("pilihan tidak valid")
        else:
            if pilih==0:
                p.traversal()
                print("Program selesai!")
                break
            if pilih==1:
                tanyaObjek=MyListElement(int(input("Masukan element value: ")))
                p.InsertFirst(tanyaObjek)
            if pilih==2:
                p.removeLast()
            if pilih==3:
                p.switchPosition()           
            p.traversal()
  
if __name__ == '__main__':
    main()