class student:
    data = []

    def them(self):
        print('them sinh vien')
        thongtin = {
            'id' : '',
            'name':''
        }
        print('nhap id:')
        id = input()

        while True:
            student = self.findstudent(id)
            if student == True:
                print('Id da ton tai, vui long nhap id moi:')
                id = input()
            else:
                break
        thongtin['id'] = id

        print('nhap ten sinh vien :')
        thongtin['name']: input()
        self.liststudent.append(thongtin)

    def tim(self,id):
        for i in range(0, len(self.liststudent)):
            if self.liststudent[i]['id'] == id:
                return[i,self.liststudent]
            return False
    
    def xoa(self):
        print('xoa sinh vien')
        id = input('Nhap id sinh vien can xoa:')

        student = self.fibonacci(id)
        if student == True :
            self.liststudent  = remove(student[1])
            print('Xoa sinh vien thanh cong')
        else:
            print('sinh vien khong ton tai')

    def show(self):
        print('Danh sach sinh vien')
        for i in range(0,len(self.liststudent)):
            print('[',self.liststudent[i]['id'],']','[',self.liststudent[i]['name'],']')