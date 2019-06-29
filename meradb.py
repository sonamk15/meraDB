import json

# fileName = "hello.db"
# Default argument dena ek acchi coding practice hai.
# Isse agar user koi argument nahi bhi de, toh bhi code sahi chalega
def load(fileName='hello.db'):
    # ```
    # Yeh ek fileName leta hai, jiska content yeh load karta hai
    # By default yeh hello.json file ko load karta hai
    # Content load kar ne ke liye, yeh ek MeraDB class ka object
    # create karta hai. Ussi object ko yeh return kar deta hai
    # jisse ki hum uss object par set, get, aur dump jaise
    # functions call kar sakein.
    # ```
    meraDB = MeraDB(fileName)
    meraDB.load_file()
    return meraDB

class MeraDB():
    # ```
    # Yeh main class hai, jaha saara magic hoga!

    # Humne yeh class isliye banayi jisse ki hum meradb object bana kar
    # uss par koi bhi functions call karp sake

    # Jaise list_a = [1,2,4] kar kar aap list_a naam ki list create karte ho
    # Phir aap list_a object par functions call kar sakte ho, jaise
    # list_a.append(another_list), list_a.pop()

    # aise hi jab aap meradb ka object declare karoge, toh class use karne ke
    # vajah se, hum meradb object par functions call kar payenge, jaise:

    # mdb = MeraDB("dbfile.json")
    # mdb.load()
    # mdb.dump()
    
    # class ke ander variable ko property bolte hai aur function ko method.

    # ```
    fileName = ""
    jObject = {}

    def __init__(self, fileName):
        # ```
        # Yeh constructor function hai, jo object declare karne par
        # call hoga. Jo bhi fileName isse milega, yeh woh apni 
        # fileName property mei store kar lega. Isse yeh property
        # object mei kahi bhi self.fileName kar kar, available hogi.
        # Isliye jab hum dump_file function aage call karenge
        # toh apne aap iss code ko pata hoga, ki kis file mei content
        # dump karne hai. Woh bas self.fileName file mei jakar contents
        # save/dump kar dega. Aise hi aap aur bhi properties bana sakte
        # hai. Jaise humne jObject kar kar ek property banayi hai. Iss
        # property mei, jab bhi database load karte hai, woh dictionary
        # hum jObject store kar lete hai. Jab bhi koi value set ya get karni
        # hoti hai, toh hum jObject se hi karte hai. Aakhir mei, dump karte 
        # hue hum jObject ko dump kar dete hai, jab bhi dump function call
        # hota hai.
        # ```
        self.fileName = fileName

    def load_file(self):
        # ```
        # Yeh file ko load karne ke liye function hai
        # ```
        print "Loading Database from ", self.fileName, " !"
        content = open(self.fileName).read()

        if content == "": 
            content= json.dumps({})
            # print (content,"content")
            self.jObject = json.loads(content)
            # print (self.jObject,"selgjobj")
            print "DB loaded successfully!"
            return self.jObject

    def dump(self):
        # ```
        # Iss function ko use kar kar, aap content ko dump kar satke hai
        # ```
        print "Dumping database to ", self.fileName, " !"
        
        open(self.fileName, 'w').write(json.dumps(self.jObject))
        # ```
        # You can also write the above line as:
        # file_handler = open(self.fileName, 'w')
        # json_dump = json.dumps(self.jObject)
        # file_handler.write(json_dump)
        # file_handler.close()
        # ```

        print "DB dumped successfully!"
        return "OK"
    def set(self,key,value):
        self.jObject[key]=value
        return True
    
    
    def get(self,key):
        try:
            print (self.jObject[key])
            return (self.jObject[key])
        except:
            print("This key doesn't exist")
            return "This key doesn't exist"

    def get_all(self):
        all_key=[]
        for i in self.jObject:
            all_key.append(i)
            if all_key=="":
                print ("database me koi key nahi hai")
                return "ok"
            print (all_key,"all_key")
            return "fdhgj"
        
    def rem(self,key):
        self.jObject.pop('key', None)
        print (self.jObject,"del key")
        return "DONE"

    def exists(self,key):
        if "key" in self.jObject:
            print "TRUE"
            return True
        else:
            print "FALSE"
            return False

    def total_keys(self):
        total_key =(len(self.jObject))
        print total_key,"total_key"
        return "Done"



    def del_db(self,key):
        for key in self.jObject:
             del self.jObject[key]
             print (self.jObject,"all_key_del") 
             return "Done"