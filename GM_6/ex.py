"""
წინამდებარე დავალებაში წარმოდგენილია მონაცემთა ფაილი ("data.in"), რომელიც შეესაბამება 10 - 12 კლასის 
მოსწავლეების მიერ 1996 – 2018 სასწავლო წლებში მიღებულ შეფასებებს. ფაილში აღებულია მხოლოდ 3 წლის მონაცემები.

იგივე მონაცემები შეგიძლიათ ჩამოტვირთოთ web-გვერდიდან (მაგრამ არაა აუცილებელი):

https://catalogue.data.gov.bc.ca/dataset/bc-schools-examinations-results

ფაილში წარმოდგენილი ველები დაყავით რამდენიმე ჯგუფად და შექმენით ჯგუფის შესაბამისი კლასი. ბოლოს შექმენით
კლასი Result, რომელიც მემკვიდრეობას მიიღებს შესაბამისი კლასებიდან.

კლასს განუსაზღვრეთ სტატიკური მეთოდი, რომელიც ქვემოთ ჩამოთვლილი პირველი ხუთი ველის მნიშვნელობიდან
ნებისმიერი ორის პარამეტრად გადაცემის შემთხვევაში იძლევა მეექვსე პუნქტში ჩამოთვლილი ველების ცალცალკე
გაერთიანებით მიღებულ შედეგის ბეჭდვის საშუალებას.

1. SCHOOL_YEAR     (2016/2017, 2017/2018, 2018/2019)
2. DISTRICT_NAME   (Southeast_Kootenay, Rocky_Mountain, Kootenay_Lake, ...)
3. SCHOOL_NAME     (Mount_Baker_Secondary, Elkford_Elementary_Secondary, ...)
4. FACILITY_TYPE   (STANDARD, ALTERNATE, DISTRICT_DISTANCE_ED)
5. GRADE           (COURSE_MARKS, FINAL_MARKS, EXAM_MARKS)
6. შეფასების ტიპი: PERCENT_OF_A, PERCENT_OF_B, PERCENT_OF_C, PERCENT_OF_D

  შენიშვნა. ფაილში მონაცემები ჩაწერილია მოყვანილი მიმდევრობით. მეექვსე პუნქტში ჩამოთვლილ ველებში უნდა 
          გამოითვალოთ მნიშვნელობების საშუალო არითმეტიკული შეფასების ტიპის მიხედვით.

მოახდინეთ ფაილიდან მონაცემების კითხვა და შესაბამისი ტიპის ობიექტებით სიმრავლის შევსება.

მოახდინეთ მიღებული სიმრავლის მიმართ სტატიკური მეთოდის გამოყენება (გამოძახება) პარამეტრად ორი განსხვავებული
წყვილის შემთხვევაში და შედეგი შეინახეთ ფაილში.
მაგალითად, შეგიძლიათ func ფუნქცია გამოიძახოთ შემდეგი წყვილებისთვის:
   (1) (SCHOOL_YEAR, SCHOOL_NAME)     ==> func(2017/2018, Elkford_Elementary_Secondary)
   (2) (DISTRICT_NAME, FACILITY_TYPE) ==> func(Southeast_Kootenay, ALTERNATE)
"""
import pandas as pd

class stats:
    def __init__(self):
        # ფაილის წაკითხვა
        with open("data-7.in","r") as f:
           data = f.readlines()
           data = [i.replace("\n","") for i in data]
           data = [i.split("#") for i in data]
        # მონაცემების დახარისხება
        years = [i[0] for i in data]
        streets = [i[1] for i in data]
        schools = [i[2] for i in data]
        types = [i[3] for i in data]
        grade = [i[4] for i in data]
        pA = [i[5] for i in data]
        pB = [i[6] for i in data]
        pC = [i[7] for i in data]
        pD = [i[8] for i in data]
        # დატაფრეიმის ფორმატში გაერთიანება ყველა მონაცემის
        df = pd.DataFrame(years, columns = ['SCHOOL_YEAR'])
        df["DISTRICT_NAME"] = streets
        df["SCHOOL_NAME"] = schools
        df["FACILITY_TYPE"] = types
        df["Grade"] = grade
        df["PERCENT_OF_A"] = pA
        df["PERCENT_OF_B"] = pB
        df["PERCENT_OF_C"] = pC
        df["PERCENT_OF_D"] = pD
        self.df = df
        
    def func(self,**kwargs):
        key1 = list(kwargs.keys())[0]
        key2 = list(kwargs.keys())[1]
        # ფილტრი გასაღებისა და მნიშვნელობის მიხედვით (სვეტი1 - მნიშვნელობა1 , სხვეტი2 - მნიშვნელობა2)
        df =  self.df[(self.df[key1]==kwargs[key1]) & (self.df[key2]==kwargs[key2])]
        # პროცენტების გამოტანა ფილტრის მიხედვით
        return df[["PERCENT_OF_A","PERCENT_OF_B","PERCENT_OF_C","PERCENT_OF_D"] ]
        
# სტატისტიკის ობიექტის შექმნა
s1 = stats()
# ობიექტის ფუნქციის გამოძახება
print(s1.func(SCHOOL_YEAR = "2017/2018", SCHOOL_NAME = "Elkford_Elementary_Secondary"))