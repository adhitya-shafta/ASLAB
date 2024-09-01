print("======SELAMAT DATANG SHAFTA ADHITYA=======")
kata ="BELAJAR PYTHON DARI NOL";
print (kata.center(50, ))
garis_pembatas= "========================================";
print (garis_pembatas.center(50, ))
print("SHAFTA ADHITYA PRATAMA")

episode_1 ="Belajar Casting Data";
print(episode_1.center(45, "-"))

#########################
casting_1 ="\nCONTOH CASTING DATA INTEGER KE DATA LAIN";
print(casting_1.center(50, ))

#data int casting 
data_int =1;
print ("data =",data_int, "type =", type(data_int))

data_float = float(data_int)
print ("data =",data_float, "type =", type(data_float))

data_bool = bool(data_int)
print ("data =",data_bool, "type =", type(data_bool))

#######################
print("\nCONTOH CASTING DATA FLOAT KE DATA LAIN");
#data float casting
data_float ="7";
print ("data =" ,data_float, "type" , type(data_float))

data_int = int(data_float)
print ("data =" ,data_int, "type" , type(data_int))

data_bool = bool(data_float)
print ("data =" ,data_bool, "type" , type(data_bool))

data_float = float (data_float)
print ("data =" ,data_float, "type" , type(data_float))
 
###########################
print("\nCONTOH CASTING DATA BOOL KE DATA LAIN");
#data bool casting
data_bool ="-1"
print ("data =" ,data_bool, "type" , type(data_bool))

data_int =int(data_bool)
print ("data =" ,data_int, "type" , type(data_int))

data_bool =bool(data_bool)
print ("data =" ,data_bool, "type" , type(data_bool))

data_float =float(data_bool)
print ("data =" ,data_float, "type" , type(data_float))

################################
print ("\nCONTOH CASTING DATA STRING KE DATA LAIN");
#data string
data_str ="00001"
#print ("data=" ,data_str, "type" , type(data_str))

data_bool=bool(data_str)
#print ("data=" ,data_bool, "type" , type (data_bool))
data_int=int(data_str)
#print ("data=" ,data_int, "type" , type (data_int))

data_float=float(data_str)
print ("data=" ,data_float, "type" , type (data_float))
print("=============================================");


print("\n========== Ngambil Data Dari User ===========");

#data input
data_nama=input ("Nama: ")
nama_strs=str ( data_nama )
print ("data=" ,data_nama, "type" , type (data_nama))

#ini adalah contoh data input int 
data_pasword=input ("Password: ")
password_int=int(data_pasword)
#print ("data=" ,data_pasword, "type" , type (data_pasword))

alamat_rumah=input ("Tempat Tinggal: ")
print ("data=" , alamat_rumah, "type" , type (alamat_rumah))

data=input("Masukan check mu disini:")
print(data)

#operasi hiung py
operasi_hitung_python= ("\nOPERASI HITUNG DALAM PYTHON DI MULAI\n")
print (operasi_hitung_python.center(60, ))

print ("\npertambahan")
#pertambahan+
a =float (input (""))
b =float (input (""))
tambah=int (a + b)
print( "hasil peetambahan",tambah )

print ("\nperkurangan")
#perkurangan-
a=int (input (""))
b=int (input(""))
perkurangan=int (a - b)
print ("hasil nya",perkurangan)

print("PERKALIAN")
a =int(input(''))
b =int(input(''))
kali = a * b
print("hasilnya",kali,)

print("pembagian")
a =int(input(''))
b =int(input(''))
bagi = a / b
print("hasilnya",bagi,)

print("aljabaar")
x =int(input("nilaix"))
y =int(input("nilai y"))
z =int(input("nilai z"))
jabar = (x * y)+z
print("hasil",jabar,)

print("belajar python if dan else ")