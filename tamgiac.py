# Nhap toa do cac diem
xA = float(input("Nhap xA : "))
yA = float(input("Nhap yA : "))
xB = float(input("Nhap xB : "))
yB = float(input("Nhap yB : "))
xC = float(input("Nhap xC : "))
yC = float(input("Nhap yC : "))
# Xet tam giac bang he so k giua vector AB va AC
def xet_tamgiac(xA,yA,xB,yB,xC,yC):
    # Toa do cac vector
    vt_AB = (xB-xA, yB-yA)
    vt_AC = (xC-xA, yC-yA)
    vt_BC = (xC-xB, yC-yB)
    vt_CB = (-vt_BC[0],-vt_BC[1])
    try:
        k1 = vt_AB[0]/vt_AC[0]
        k2 = vt_AB[1]/vt_AC[1]
        if k1 != k2: return True
        else: return False
    except:
        return False

# Do dai cac canh
import math
def goccanh_tamgiac(xA,yA,xB,yB,xC,yC):
    #Tinh toan do dai cac canh
    AB = round(math.sqrt((xB-xA)**2+(yB-yA)**2),2)
    AC = round(math.sqrt((xC-xA)**2+(yC-yA)**2),2)
    BC = round(math.sqrt((xB-xC)**2+(yB-yC)**2),2)
    #tinh cac goc tam giac
    cos_goc_A = ((xB-xA)*(xC-xA)+(yB-yA)*(yC-yA))/(math.sqrt((xB-xA)**2+(yB-yA)**2)*math.sqrt((xC-xA)**2+(yC-yA)**2))
    cos_goc_B = ((xA-xB)*(xC-xB)+(yA-yB)*(yC-yB))/(math.sqrt((xA-xB)**2+(yA-yC)**2)*math.sqrt((xC-xB)**2+(yC-yB)**2))
    cos_goc_C = ((xA-xC)*(xB-xC)+(yA-yC)*(yB-yC))/(math.sqrt((xA-xC)**2+(yA-yC)**2)*math.sqrt((xB-xC)**2+(yB-yC)**2))
    goc_A = round(math.acos(cos_goc_A)*180/math.pi,2)
    goc_B = round(math.acos(cos_goc_B)*180/math.pi,2)
    goc_C = round(math.acos(cos_goc_C)*180/math.pi,2)
    return [AB,AC,BC,goc_A,goc_B,goc_C]

# xet loai tam giac
def xetloai_tamgiac(xA,yA,xB,yB,xC,yC):
    AB = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[0]
    AC = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[1]
    BC = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[2]
    goc_A = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[3]
    goc_B = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[4]
    goc_C = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[5]
    #xet tam giac vuong can
    if goc_A == 90 and AB == AC:
        l ="ABC la tam giac Vuong can tai A"
    elif goc_B == 90 and AB == BC:
        l ="ABC la tam giac Vuong can tai B"
    elif goc_C == 90 and BC == AC:
        l="ABC la tam giac Vuong can tai C"
    #xet tam giac Vuong
    elif goc_A == 90:
        l="ABC la tam giac Vuong tai A"
    elif goc_B == 90:
        l="ABC la tam giac Vuong tai B"
    elif goc_C == 90:
        l="ABC la tam giac Vuong tai C"
    #tam giac tu can
    elif goc_A > 90 and AB == AC:
        l="ABC la tam giac tu can tai A"
    elif goc_B > 90 and AB == BC:
        l="ABC la tam giac tu can tai B"
    elif goc_C > 90 and BC == AC:
        l="ABC la tam giac tu can tai C"
    #xet tam giac tu
    elif goc_A > 90:
        l="ABC la tam giac tu tai A"
    elif goc_B > 90:
        l="ABC la tam giac tu tai B"
    elif goc_C > 90:
        l="ABC la tam giac tu tai C"
    #xet tam giac deu
    elif AB == AC and AB == BC and AB != 0 == AC and AB != 0:
        l="ABC can tai A"
    elif AB == BC and AB !=0:
        l="ABC can tai B"
    elif BC == AC and BC != 0:
        l="ABC can tai C"
    else:
        l="ABC la tam giac thuong"
    return l

# Tinh dien tich tam giac bang cong thuc heron
def dientich_tamgiac(xA,yA,xB,yB,xC,yC):
    AB = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[0]
    AC = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[1]
    BC = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[2]
    p = (AB + AC + BC)/2
    S = round(float(math.sqrt(p*(p-AB)*(p-AC)*(p-BC))),2)
    return S

#tinh duong cao tam giac
def duongcao_tamgiac(xA,yA,xB,yB,xC,yC):
    AB = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[0]
    AC = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[1]
    BC = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[2]
    S = dientich_tamgiac(xA,yA,xB,yB,xC,yC)
    h_A = round(float(2*S/BC),2)
    h_B = round(float(2*S/AC),2)
    h_C = round(float(2*S/AB),2)
    return [h_A,h_B,h_C]

#Ham tra ve toa do trong tam G va truc tam H
def tam_tamgiac(xA,yA,xB,yB,xC,yC):
    #Trong tam G
    xG = (xA+xB+xC)/3
    yG = (yA+yB+yC)/3
    goc_A = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[3]
    goc_B = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[4]
    goc_C = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[5]
    #Truc tam H
    xH = (xA * math.tan(goc_A) + xB * math.tan(goc_B) + xC * math.tan(goc_C)) / (math.tan(goc_A) + math.tan(goc_B) + math.tan(goc_C))
    yH = (yA * math.tan(goc_A) + yB * math.tan(goc_B) + yC * math.tan(goc_C)) / (math.tan(goc_A) + math.tan(goc_B) + math.tan(goc_C))
    return [xG,yG,xH,yH]
# Khoang cach tu dinh den trong tam G
def d_G(xA,yA,xB,yB,xC,yC):
    xG = tam_tamgiac(xA,yA,xB,yB,xC,yC)[0]
    yG = tam_tamgiac(xA,yA,xB,yB,xC,yC)[1]
    AG = round(math.sqrt((xG-xA)**2+(yG-yA)**2),2)
    BG = round(math.sqrt((xG-xB)**2+(yG-yB)**2),2)
    CG = round(math.sqrt((xG-xC)**2+(yG-yC)**2),2)
    return [xG,yG,AG,BG,CG]

def giaima_tamgiac(xA,yA,xB,yB,xC,yC):
    try:
        if xet_tamgiac(xA,yA,xB,yB,xC,yC) == False:
            raise Exception
    except:
        print('ABC khong phai tam giac')
        return
    print('ABC hop thanh 1 tam giac')
    #1. so do co ban 
    AB = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[0]
    AC = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[1]
    BC = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[2]
    goc_A = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[3]
    goc_B = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[4]
    goc_C = goccanh_tamgiac(xA,yA,xB,yB,xC,yC)[5]
    print("ABC hop thanh mot tam giac")
    print("Chieu dai canh AB: {}".format(AB))
    print("Chieu dai canh AC: {}".format(AC))
    print("Chieu dai canh BC: {}".format(BC))
    print("Goc A: {}".format(goc_A))
    print("Goc B: {}".format(goc_B))
    print("Goc C: {}".format(goc_C))
    print(xetloai_tamgiac(xA,yA,xB,yB,xC,yC))
    #2. dien tich tam giac
    S = dientich_tamgiac(xA,yA,xB,yB,xC,yC)
    print('Dien tich tam giac ABC: {}'.format(S))
    #3. so do nang cao 
    h_A = duongcao_tamgiac(xA,yA,xB,yB,xC,yC)[0]
    h_B = duongcao_tamgiac(xA,yA,xB,yB,xC,yC)[1]
    h_C = duongcao_tamgiac(xA,yA,xB,yB,xC,yC)[2]
    print('Do dai duong cao tu dinh A: {}'.format(h_A))
    print('Do dai duong cao tu dinh B: {}'.format(h_B))
    print('Do dai duong cao tu dinh C: {}'.format(h_C))
    print('Do dai duong cao tu dinh C: {}'.format(h_C))
    xG = d_G(xA,yA,xB,yB,xC,yC)[0]
    yG = d_G(xA,yA,xB,yB,xC,yC)[1]
    AG = d_G(xA,yA,xB,yB,xC,yC)[2]
    BG = d_G(xA,yA,xB,yB,xC,yC)[3]
    CG = d_G(xA,yA,xB,yB,xC,yC)[4]
    print('Khoang cach den trong tam tu dinh A: {}'.format(AG))
    print('Khoang cach den trong tam tu dinh B: {}'.format(BG))
    print('Khoang cach den trong tam tu dinh C: {}'.format(CG))
    xH = tam_tamgiac(xA,yA,xB,yB,xC,yC)[2]
    yH = tam_tamgiac(xA,yA,xB,yB,xC,yC)[3]
    print('Toa do trong tam: ',[xG,yG])
    print('Toa do truc tam: ',[xH,yH])
   
# Do dai duong trung tuyen
def trungtuyen_tamgiac(xA,yA,xB,yB,xC,yC):
    AG = d_G(xA,yA,xB,yB,xC,yC)[2]
    BG = d_G(xA,yA,xB,yB,xC,yC)[3]
    CG = d_G(xA,yA,xB,yB,xC,yC)[4]
    ttA = round((3/2)*AG,2)
    ttB = round((3/2)*BG,2)
    ttC = round((3/2)*CG,2)
    return [ttA, ttB, ttC]

print(xet_tamgiac(xA,yA,xB,yB,xC,yC))
print(goccanh_tamgiac(xA,yA,xB,yB,xC,yC))
print(xetloai_tamgiac(xA,yA,xB,yB,xC,yC))
print(dientich_tamgiac(xA,yA,xB,yB,xC,yC))
print(duongcao_tamgiac(xA,yA,xB,yB,xC,yC))
print(tam_tamgiac(xA,yA,xB,yB,xC,yC))
print(d_G(xA,yA,xB,yB,xC,yC))
print(giaima_tamgiac(xA,yA,xB,yB,xC,yC))
print(trungtuyen_tamgiac(xA,yA,xB,yB,xC,yC))