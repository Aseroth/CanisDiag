from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

rel_dir = os.path.dirname(os.path.abspath(__file__))


wynik_ok = 'OK'
wynik_niski = 'ZA NISKI'
wyniki_wysoki = 'ZA WYSOKI'
brak_badania = 'NIE BADANO'

#------- wymiary A4 w mm
pdf_w,pdf_h = A4
#----- LOGO CANIS
canis_logo = '{}\\canis_logo.png'.format(rel_dir)
font_path = '{}\\FreeSans.ttf'.format(rel_dir)
fontBold_path = '{}\\FreeSansBold.ttf'.format(rel_dir)
#raport  = canvas.Canvas('Hello.pdf', pagesize=A4)
pdfmetrics.registerFont(TTFont('FreeSans', font_path))
pdfmetrics.registerFont(TTFont('FreeSansBold', fontBold_path))

class diag_canvas():
    def __init__(self, docname: str, raport_date: str, nr_zlecenia='', gatunek='', wlasciciel='', nazwa='', 
                kreatynina_wynik='', mocznik_wynik='', fosfor_wynik='',alat_wynik='',aspat_wynik='',bialko_wynik='',bilirubina_wynik='',alp_wynik='',
                glukoza_wynik='',amylaza_wynik='',lipaza_wynik='',sod_wynik='', potas_wynik='', wbc_wynik='', rbc_wynik='', hgb_wynik='', hct_wynik='',
                plt_wynik='', uwagi='brak'):
        self.docname = docname
        self.raport_date = raport_date
        self.nr_zlecenia = nr_zlecenia
        self.gatunek = gatunek
        self.wlasciciel = wlasciciel
        self.nazwa = nazwa

        self.kreatynina_wynik = kreatynina_wynik
        self.mocznik_wynik = mocznik_wynik
        self.fosfor_wynik = fosfor_wynik
        self.alat_wynik = alat_wynik
        self.aspat_wynik = aspat_wynik
        self.bialko_wynik = bialko_wynik
        self.bilirubina_wynik = bilirubina_wynik
        self.alp_wynik = alp_wynik
        self.glukoza_wynik = glukoza_wynik
        self.amylaza_wynik = amylaza_wynik
        self.lipaza_wynik = lipaza_wynik
        self.sod_wynik = sod_wynik
        self.potas_wynik = potas_wynik
        self.wbc_wynik = wbc_wynik
        self.rbc_wynik = rbc_wynik
        self.hgb_wynik = hgb_wynik
        self.hct_wynik = hct_wynik
        self.plt_wynik = plt_wynik

        self.uwagi=uwagi
        #normy badań kota
        # biochemia krwi
        kreatynina_kot_norma = [1.0,2.0]
        mocznik_kot_norma = [25.0,70.0]
        fosfor_kot_norma = [3.0,6.8] #mg/dl
        alat_kot_norma =[20.0,107.0] #U/l
        aspat_kot_norma = [6.0,44.0] #U/l
        białko_kot_norma = [6.0,8.0] #g/dl
        bilirubina_kot_norma = [0.5,1.2] #mg/dl
        alp_kot_norma = [23.0,107.0] #U/l
        glukoza_kot_norma = [100.0,130.0]#mg/dl
        amylaza_kot_norma = [433.0,1248.0] #U/l
        lipaza_kot_norma = [0.0,250.0] #U/l
        sod_kot_norma = [143.6,156.5] #mg/dl
        potas_kot_norma = [4.1,5.6] #mg/dl
        #morfologia
        wbc_kot_norma = [6.0,19.0] #tys/ul
        rbc_kot_norma = [6.6,10.0] #mln/ul
        hgb_kot_norma = [6.2,9.3] #mmol/l
        hct_kot_norma = [30.0,45.0] #%
        plt_kot_norma = [300.0,800.0] #tys/ul



        #normy badań psa
        # biochemia krwi
        kreatynina_psa_norma = [0.9,1.7] #mg/dl
        mocznik_psa_norma = [20.0,50.0] #mg/dl
        fosfor_psa_norma = [2.5,6.3] #mg/dl
        alat_psa_norma =[30.0,60.0] #U/l
        aspat_psa_norma = [1.0,45.0] #U/l
        białko_psa_norma = [5.5,7.5] #g/dl
        bilirubina_psa_norma = [0.3,0.9] #mg/dl
        alp_psa_norma = [20.0,155.0] #U/l
        glukoza_psa_norma = [70.0,120.0]#mg/dl
        amylaza_psa_norma = [300.0,1850.0] #U/l
        lipaza_psa_norma = [268.0,1769.0] #U/l
        sod_psa_norma = [320.0,360.0] #mg/dl
        potas_psa_norma = [16.0,21.0] #mg/dl
        #morfologia
        wbc_psa_norma = [6.0,16.5] #tys/ul
        rbc_psa_norma = [5.5,8.5] #mln/ul
        hgb_psa_norma = [12.0,18.0] #mmol/l
        hct_psa_norma = [37.0,55.0] #%
        plt_psa_norma = [200.0,500.0] #tys/ul

        normy=[]

        if self.gatunek=='Kot':
            #biochemia
            normy.append(kreatynina_kot_norma)
            normy.append(mocznik_kot_norma)
            normy.append(fosfor_kot_norma)
            normy.append(alat_kot_norma)
            normy.append(aspat_kot_norma)
            normy.append(białko_kot_norma)
            normy.append(bilirubina_kot_norma)
            normy.append(alp_kot_norma)
            normy.append(glukoza_kot_norma)
            normy.append(amylaza_kot_norma)
            normy.append(lipaza_kot_norma)
            normy.append(sod_kot_norma)
            normy.append(potas_kot_norma)
            #morfologia
            normy.append(wbc_kot_norma)
            normy.append(rbc_kot_norma)
            normy.append(hgb_kot_norma)
            normy.append(hct_kot_norma)
            normy.append(plt_kot_norma)
        elif self.gatunek=='Pies':
            #biochemia
            normy.append(kreatynina_psa_norma)
            normy.append(mocznik_psa_norma)
            normy.append(fosfor_psa_norma)
            normy.append(alat_psa_norma)
            normy.append(aspat_psa_norma)
            normy.append(białko_psa_norma)
            normy.append(bilirubina_psa_norma)
            normy.append(alp_psa_norma)
            normy.append(glukoza_psa_norma)
            normy.append(amylaza_psa_norma)
            normy.append(lipaza_psa_norma)
            normy.append(sod_psa_norma)
            normy.append(potas_psa_norma)
            #morfologia
            normy.append(wbc_psa_norma)
            normy.append(rbc_psa_norma)
            normy.append(hgb_psa_norma)
            normy.append(hct_psa_norma)
            normy.append(plt_psa_norma)

        #print(normy)
        #print(normy[4])
        #print(normy[4][1])

        self.raport  = canvas.Canvas(f'{docname}.pdf', pagesize=A4)
        
        
        self.raport.setLineWidth(.3)
        self.raport.setFont('FreeSans',12)

        self.raport.drawString(30,780,'Gabinet Weterynaryjny CANIS')
        self.raport.drawString(30,765,'ul. Krajobrazowa 2')
        self.raport.drawString(30,750,'35-119 Rzeszów')
        self.raport.drawString(30,735,'tel. 17 859 03 79, Email: kontakt@canisrzeszow.pl')
        self.raport.drawString(30,720,'http://canisrzeszow.pl/')
        self.raport.drawString(480,780, f'{raport_date}')
        self.raport.line(480,777,580,777)
        self.raport.line(5,715,580,715)

        self.raport.drawString(30,700, f'Nr zlecenia: {self.nr_zlecenia}')
        self.raport.drawString(300,700,f'Gatunek: {self.gatunek}')
        self.raport.drawString(30,685, f'Właściciel: {self.wlasciciel}')
        self.raport.drawString(300,685, f'Imie zw.: {self.nazwa}')
        self.raport.line(5,680,580,680)

        self.raport.drawString(30,665,'Badanie')
        self.raport.drawString(200,665,'Wynik')
        self.raport.drawString(320,665,'Jedn.')
        self.raport.drawString(420,665,'Norma')
        self.raport.line(30,655,550,655)
        self.raport.setFont('FreeSansBold',12)
        self.raport.drawString(30,640,'OZNACZENIA BIOCHEMICZNE')
        self.raport.setFont('FreeSans',12)
        self.raport.line(30,635,550,635)

        self.raport.setFont('FreeSans',10)
        self.raport.drawString(30,625,'Kreatynina')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,625,f'{self.kreatynina_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,625,'mg/dl')
        self.raport.drawString(420,625,f'{normy[0]}')
        if kreatynina_wynik!='' and kreatynina_wynik < normy[0][0]:
            self.raport.drawString(500,625,wynik_niski)
        elif kreatynina_wynik!='' and kreatynina_wynik > normy[0][1]:
            self.raport.drawString(500,625,wyniki_wysoki)
        elif self.kreatynina_wynik=='':
            self.raport.drawString(500,625,brak_badania)
        else:
            self.raport.drawString(500,625, wynik_ok)
        
        self.raport.line(30,622,550,622)

        self.raport.drawString(30,610,'Mocznik')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,610,f'{self.mocznik_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,610,'mg/dl')
        self.raport.drawString(420,610,f'{normy[1]}')
        if mocznik_wynik!='' and mocznik_wynik < normy[1][0]:
            self.raport.drawString(500,610,wynik_niski)
        elif mocznik_wynik!='' and mocznik_wynik > normy[1][1]:
            self.raport.drawString(500,610,wynik_niski)
        elif mocznik_wynik=='':
            self.raport.drawString(500,610,brak_badania)
        else:
            self.raport.drawString(500,610,wynik_ok)
        self.raport.line(30,607,550,607)


        self.raport.drawString(30,595,'Fosfor')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,595,f'{self.fosfor_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,595,'mg/dl')
        self.raport.drawString(420,595,f'{normy[2]}')
        if self.fosfor_wynik!='' and self.fosfor_wynik < normy[2][0]:
            self.raport.drawString(500,595,wynik_niski)
        elif self.fosfor_wynik!='' and self.fosfor_wynik> normy[2][1]:
            self.raport.drawString(500,595,wyniki_wysoki)
        elif self.fosfor_wynik=='':
            self.raport.drawString(500,595,brak_badania)
        else:
            self.raport.drawString(500,595,wynik_ok)
        self.raport.line(30,592,550,592)

        self.raport.drawString(30,580,'ALAT')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,580,f'{self.alat_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,580,'U/l')
        self.raport.drawString(420,580,f'{normy[3]}')
        if self.alat_wynik!='' and self.alat_wynik < normy[3][0]:
            self.raport.drawString(500,580, wynik_niski)
        elif self.alat_wynik!='' and self.alat_wynik > normy[3][1]:
            self.raport.drawString(500,580,wyniki_wysoki)
        elif self.alat_wynik =='':
            self.raport.drawString(500,580,brak_badania)
        else:
            self.raport.drawString(500,580,wynik_ok)
        self.raport.line(30,577,550,577)

        self.raport.drawString(30,565,'ASPAT')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,565,f'{aspat_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,565,'U/l')
        self.raport.drawString(420,565,f'{normy[4]}')
        if aspat_wynik!='' and aspat_wynik<normy[4][0]:
            self.raport.drawString(500,565,wynik_niski)
        elif  aspat_wynik!='' and aspat_wynik>normy[4][1]:
            self.raport.drawString(500,565,wynik_niski)
        elif aspat_wynik=='':
            self.raport.drawString(500,565,brak_badania)
        else:
            self.raport.drawString(500,565,wynik_ok)
        self.raport.line(30,562,550,562)

        self.raport.drawString(30,550,'Białko')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,550,f'{bialko_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,550,'g/dl')
        self.raport.drawString(420,550,f'{normy[5]}')
        if self.bialko_wynik!='' and self.bialko_wynik < normy[5][0]:
            self.raport.drawString(500,550,wynik_niski)
        elif self.bialko_wynik!='' and self.bialko_wynik > normy[5][1]:
            self.raport.drawString(500,550,wyniki_wysoki)
        elif self.bialko_wynik=='':
            self.raport.drawString(500,550,brak_badania)
        else:
            self.raport.drawString(500,550,wynik_ok)
        self.raport.line(30,547,550,547)

        self.raport.drawString(30,535,'Bilirubina')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,535,f'{bilirubina_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,535,'mg/dl')
        self.raport.drawString(420,535,f'{normy[6]}')
        if self.bilirubina_wynik!='' and self.bilirubina_wynik <normy[6][0]:
            self.raport.drawString(500,535,wynik_niski)
        elif self.bilirubina_wynik!='' and self.bilirubina_wynik > normy[6][1]:
            self.raport.drawString(500,535,wyniki_wysoki)
        elif self.bilirubina_wynik=='':
            self.raport.drawString(500,535,brak_badania)
        else:
            self.raport.drawString(500,535,wynik_ok)
        self.raport.line(30,532,550,532)

        self.raport.drawString(30,520,'ALP')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,520,f'{alp_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,520,'U/l')
        self.raport.drawString(420,520,f'{normy[7]}')
        if self.alp_wynik!='' and self.alp_wynik <normy[7][0]:
            self.raport.drawString(500,520,wynik_niski)
        elif self.alp_wynik!='' and self.alp_wynik>normy[7][1]:
            self.raport.drawString(500,520,wyniki_wysoki)
        elif self.alp_wynik=='':
            self.raport.drawString(500,520,brak_badania)
        else:
            self.raport.drawString(500,520,wynik_ok)
        self.raport.line(30,517,550,517)

        self.raport.drawString(30,505,'Glukoza') 
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,505,f'{glukoza_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,505,'mg/dl')
        self.raport.drawString(420,505,f'{normy[8]}')
        if self.glukoza_wynik!='' and self.glukoza_wynik < normy[8][0]:
            self.raport.drawString(500,505,wynik_niski)
        elif self.glukoza_wynik!='' and self.glukoza_wynik > normy[8][1]:
            self.raport.drawString(500,505, wyniki_wysoki)
        elif self.glukoza_wynik=='':
            self.raport.drawString(500,505,brak_badania)
        else:
            self.raport.drawString(500,505,wynik_ok)
        self.raport.line(30,502,550,502)

        self.raport.drawString(30,490, 'Amylaza')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,490,f'{amylaza_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,490,'U/l')
        self.raport.drawString(420,490,f'{normy[9]}')
        if self.amylaza_wynik!='' and self.amylaza_wynik < normy[9][0]:
            self.raport.drawString(500,490,wynik_niski)
        elif self.amylaza_wynik!='' and self.amylaza_wynik > normy[9][1]:
            self.raport.drawString(500,490,wyniki_wysoki)
        elif self.amylaza_wynik=='':
            self.raport.drawString(500,490, brak_badania)
        else:
            self.raport.drawString(500,490,wynik_ok)
        self.raport.line(30,487,550,487)

        self.raport.drawString(30,475,'Lipaza')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,475,f'{lipaza_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,475,'U/l')
        self.raport.drawString(420,475,f'{normy[10]}')
        if self.lipaza_wynik!='' and self.lipaza_wynik < normy[10][0]:
            self.raport.drawString(500,475,wynik_niski)
        elif self.lipaza_wynik!='' and self.lipaza_wynik > normy[10][1]:
            self.raport.drawString(500,475,wyniki_wysoki)
        elif self.lipaza_wynik=='':
            self.raport.drawString(500,475, brak_badania)
        else:
             self.raport.drawString(500,475,wynik_ok)
        self.raport.line(30,472,550,472)

        self.raport.drawString(30,460,'Sód')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,460,f'{sod_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,460,'mg/dl')
        self.raport.drawString(420,460,f'{normy[11]}')
        if self.sod_wynik!='' and self.sod_wynik < normy[11][0]:
            self.raport.drawString(500,460,wynik_niski)
        elif self.sod_wynik!='' and self.sod_wynik > normy[11][1]:
            self.raport.drawString(500,460,wyniki_wysoki)
        elif self.sod_wynik=='':
            self.raport.drawString(500,460, brak_badania)
        else:
            self.raport.drawString(500,460,wynik_ok)
        self.raport.line(30,457,550,457)

        self.raport.drawString(30,445,'Potas')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,445,f'{potas_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,445,'mg/dl')
        self.raport.drawString(420,445,f'{normy[12]}')
        if self.potas_wynik!='' and self.potas_wynik < normy[12][0]:
            self.raport.drawString(500,445, wynik_niski)
        elif self.potas_wynik!='' and self.potas_wynik > normy[12][1]:
            self.raport.drawString(500,445), wyniki_wysoki
        elif self.potas_wynik=='':
            self.raport.drawString(500,445,brak_badania)
        else: 
            self.raport.drawString(500,445,wynik_ok)
        self.raport.line(30,442,550,442)

        self.raport.setFont('FreeSansBold',12)
        self.raport.drawString(30,430,'MORFOLOGIA KRWI')
        self.raport.line(30,427,550,427)

        self.raport.setFont('FreeSans',10)
        self.raport.drawString(30,415, 'WBC')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,415,f'{wbc_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,415,'tys./µl')
        self.raport.drawString(420,415,f'{normy[13]}')
        if self.wbc_wynik!='' and self.wbc_wynik < normy[13][0]:
            self.raport.drawString(500,415,wynik_niski)
        elif self.wbc_wynik!='' and self.wbc_wynik > normy[13][1]:
            self.raport.drawString(500,415, wyniki_wysoki)
        elif self.wbc_wynik=='':
            self.raport.drawString(500,415,brak_badania)
        else: 
            self.raport.drawString(500,415, wynik_ok)
        self.raport.line(30,412,550,412)

        self.raport.drawString(30,400, 'RBC')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,400,f'{rbc_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,400,'mln/µl')
        self.raport.drawString(420,400,f'{normy[14]}')
        if self.rbc_wynik!='' and self.rbc_wynik < normy[14][0]:
            self.raport.drawString(500,400,wynik_niski)
        elif self.rbc_wynik!='' and self.rbc_wynik > normy[14][1]:
            self.raport.drawString(500,400,wyniki_wysoki)
        elif self.rbc_wynik=='':
            self.raport.drawString(500,400,brak_badania)
        else:
            self.raport.drawString(500,400,wynik_ok)
        self.raport.line(30,397,550,397)

        self.raport.drawString(30,385, 'HGB')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,385,f'{hgb_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,385,'g/dl')
        self.raport.drawString(420,385,f'{normy[15]}')
        if self.hgb_wynik!='' and self.hgb_wynik < normy[15][0]:
            self.raport.drawString(500,385,wynik_niski)
        elif self.hgb_wynik!='' and self.hgb_wynik > normy[15][1]:
            self.raport.drawString(500,385,wyniki_wysoki)
        elif self.hgb_wynik=='':
            self.raport.drawString(500,385, brak_badania)
        else:
            self.raport.drawString(500,385,wynik_ok)
        self.raport.line(30,382,550,382)

        self.raport.drawString(30,370, 'HCT')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,370,f'{hct_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,370,'%')
        self.raport.drawString(420,370,f'{normy[16]}')
        if hct_wynik!='' and hct_wynik < normy[16][0]:
            self.raport.drawString(500,370,wynik_niski)
        elif hct_wynik!='' and hct_wynik > normy[16][1]:
            self.raport.drawString(500,370,wyniki_wysoki)
        elif hct_wynik=='':
            self.raport.drawString(500,370,brak_badania)
        else:
            self.raport.drawString(500,370,wynik_ok)
        self.raport.line(30,367,550,367)

        self.raport.drawString(30,355,'PLT')
        self.raport.setFont('FreeSansBold',10)
        self.raport.drawString(200,355,f'{plt_wynik}')
        self.raport.setFont('FreeSans',10)
        self.raport.drawString(320,355,'tys./µl')
        self.raport.drawString(420,355,f'{normy[17]}')
        if plt_wynik!='' and plt_wynik < normy[17][0]:
            self.raport.drawString(500,355,wynik_niski)
        elif plt_wynik!='' and plt_wynik > normy[17][1]:
            self.raport.drawString(500,355,wyniki_wysoki)
        elif plt_wynik=='':
            self.raport.drawString(500,355,brak_badania)
        else:
            self.raport.drawString(500,355,wynik_ok)
        self.raport.line(30,352,550,352)


        self.raport.drawString(30,340,'Uwagi: ')
        self.raport.drawString(65,340,f'{self.uwagi}')
        
        self.raport.save()




test = diag_canvas('test','2022-10-10','22222','Pies','Bartłomiej Nowak','Bella','',6,6,6,6,'',6,6,6,6,6,6,6,6,6,6,6,6,)
