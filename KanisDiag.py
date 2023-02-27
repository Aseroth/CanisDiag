
import PySimpleGUI as sg
import datetime
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
import Kanis_canvas
from Kanis_canvas import diag_canvas
import os
import subprocess

rel_dir = os.path.dirname(os.path.abspath(__file__))

#------- wymiary A4 w mm
pdf_w,pdf_h = A4
#----- LOGO CANIS
canis_logo = '{}\\canis_logo.png'.format(rel_dir)


raport  = canvas.Canvas('Hello.pdf', pagesize=A4)

save_location = f'{rel_dir}\\wyniki'

cur_date = datetime.now()



def main():

    animal_type = ['Pies', 'Kot']
    #normy PSA
    ast_kot_norma = [6.0,44.0]          #U/l
    alt_kot_norma = [20.0,107.0]        #U/l
    alp_kot_norma = [23.0,107.0]        #U/l
    bilirubina_kot_norma = [0.5,1.2]    #mg/dl
    ggt_kot_norma = [0.0,10.0]          #U/l
    ldh_kot_norma = [161.0,1051.0]      #U/l
    cholesterol_kot_norma = [77.4,201.2] #mg/dl
    triglicerydy_kot_norma = [17.7,159.4] ##mg/dl
    kw_zolt_kot_norma = [0.0,25.0] #umol/l
    białko_kot_norma = [60.0,80.0] #g/l
    albuminy_kot_norma = [27.0,39.0] #g/l
    glukoza_kot_norma = [100.0,130.0]#mg/dl
    fruktozamina_kot_norma = [0.0,400.0] #umol/l
    mocznik_kot_norma = [25.0,70.0]#mg/dl
    kreatynina_kot_norma = [1.0,1.8]#mg/dl
    kinaza_kot_norma = [49.0,688.0] #U/l
    amylaza_kot_norma = [433.0,1248.0] #U/l
    lipaza_kot_norma = [157.0,1715.0] #U/l
    wapn_kot_norma = [8.0,11.1] #mg/dl
    fosfor_kot_norma = [3.0,6.8]        #mg/dl
    magnez_kot_norma =[2.1,3.2] #mg/dl
    zelazo_kot_norma =[68.0,215.0] #ug/dl
    potas_kot_norma = [4.1,5.6] #mg/dl
    sod_kot_norma = [143.6,156.5] #mg/dl
    chlorki_kot_norma = [360.0,420.0] #mg/dl



        #normy badań psa
        # biochemia krwi
    ast_psa_norma = [1.0,45.0]          #U/l
    alt_psa_norma = [30.0,60.0]        #U/l
    alp_psa_norma = [20.0,155.0]        #U/l
    bilirubina_psa_norma = [0.3,0.9]    #mg/dl
    ggt_psa_norma = [5.0,25.0]          #U/l
    ldh_psa_norma = [105.0,1683.0]      #U/l
    cholesterol_psa_norma = [127.7,360.0] #mg/dl
    triglicerydy_psa_norma = [17.7,115.1] ##mg/dl
    kw_zolt_psa_norma = [0.0,30.0] #umol/l
    białko_psa_norma = [50.0,75.0] #g/l
    albuminy_psa_norma = [33.0,56.0] #g/l
    glukoza_psa_norma = [70.0,120.0]#mg/dl
    fruktozamina_psa_norma = [0.0,320.0] #umol/l
    mocznik_psa_norma = [20.0,50.0]#mg/dl
    kreatynina_psa_norma = [0.9,1.7]#mg/dl
    kinaza_psa_norma = [25.0,467.0] #U/l
    amylaza_psa_norma = [300.0,1850.0] #U/l
    lipaza_psa_norma = [268.0,1769.0] #U/l
    wapn_psa_norma = [8.4,11.5] #mg/dl
    fosfor_psa_norma = [2.5,6.3]        #mg/dl
    magnez_psa_norma =[1.7,2.9] #mg/dl
    zelazo_psa_norma =[94.0,122.0] #ug/dl
    potas_psa_norma = [4.1,5.4] #mg/dl
    sod_psa_norma = [320.0,360.0] #mg/dl
    chlorki_psa_norma = [350.0,410.0] #mg/dl

    badania_odw = ['AST', 'ALT', 'ALP', 'BILIRUBINA','GGT','LDH','CHOLESTEROL','TRIGLICERYDY','KW-ZOLT','BIALKO','ALBUMINY','GLUKOZA','FRUKTOZAMINA','MOCZNIK','KREATYNINA','KINAZA','AMYLAZA','LIPAZA','WAPN','FOSFOR','MAGNEZ','ZELAZO','POTAS','SOD','MAGNEZ','CHLORKI']
    badania = []
    for x in range(len(badania_odw)):
        badania.append(0)

    layout = [
        [sg.Text('Numer zlecenia', size=(20,1)), sg.Input(key='order-no')],
        [sg.Text('Właściciel', size=(20,1)), sg.Input(key='owner')],
        [sg.Text('Gatunek', size=(20,1)), sg.Combo(animal_type, default_value='Pies', key='animal-type',enable_events=True)],
        [sg.Text('Imie zwierzęcia', size=(20,1)), sg.Input(key='pet-name')],
        [sg.HorizontalSeparator()],
        [sg.Text('Wynik badań diagnostycznych', font=('Helvetica',20))],
        [sg.Text('Badania biochemiczne krwi', font=('Helvetica',12),size=(25,1))],
        [sg.Text('\t\t\t\t\tNorma\t\t\t\t\t\t\tNorma')],
        [sg.Text('AST',font=('Helvetica',12), size=(10,1)), sg.Input(key='ast-wynik', size=(10,1)),sg.Text('U/l\t'), sg.Text(key='ast-norma', size=(15,1)),                                  sg.Text('ALT',font=('Helvetica',12), size=(10,1)),sg.Input(key='alt-wynik', size=(10,1)),sg.Text('U/l\t'), sg.Text(key='alt-norma', size=(15,1))],
        
        [sg.Text('ALP',font=('Helvetica',12), size=(10,1)),sg.Input(key='alp-wynik', size=(10,1)),sg.Text('U/l\t'), sg.Text(key='alp-norma', size=(15,1)),                                   sg.Text('Bilirubina',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='bilirubina-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='bilirubina-norma', size=(15,1))],
        
        [sg.Text('GGT',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='ggt-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='ggt-norma', size=(15,1)),                               sg.Text('LDH',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='ldh-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='ldh-norma', size=(15,1))],
        
        [sg.Text('Cholesterol',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='cholesterol-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='cholesterol-norma', size=(15,1)),     sg.Text('Triglicerydy',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='triglicerydy-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='triglicerydy-norma', size=(15,1))],
        
        [sg.Text('Kwasy żół.',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='kw-zolt-wynik', size=(10,1)), sg.Text('umol/l\t'), sg.Text(key='kw-zolt-norma', size=(15,1)),             sg.Text('Białko całk.',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='bialko-wynik', size=(10,1)), sg.Text('g/l\t'), sg.Text(key='bialko-norma', size=(15,1))],
        
        [sg.Text('Albuminy',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='albuminy-wynik', size=(10,1)), sg.Text('g/l\t'), sg.Text(key='albuminy-norma', size=(15,1)),                sg.Text('Glukoza',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='glukoza-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='glukoza-norma', size=(15,1))],
        
        [sg.Text('Fruktozamina',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='fruktozamina-wynik', size=(10,1)), sg.Text('umol/l\t'), sg.Text(key='fruktozamina-norma', size=(15,1)), sg.Text('Mocznik',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='mocznik-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='mocznik-norma', size=(15,1))],
       
        [sg.Text('Kreatynina',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='kreatynina-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='kreatynina-norma', size=(15,1)),        sg.Text('Kinaza',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='kinaza-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='kinaza-norma', size=(15,1))],
        
        [sg.Text('Amylaza',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='amylaza-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='amylaza-norma', size=(15,1)),                   sg.Text('Lipaza',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='lipaza-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='lipaza-norma', size=(15,1))],
        
        [sg.Text('Wapń',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='wapn-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='wapn-norma', size=(15,1)),                          sg.Text('Fosfor',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='fosfor-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='fosfor-norma', size=(15,1))],
        
        [sg.Text('Magnez',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='magnez-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='magnez-norma', size=(15,1)),                    sg.Text('Żelazo',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='zelazo-wynik', size=(10,1)), sg.Text('ug/dl\t'), sg.Text(key='zelazo-norma', size=(15,1))],
        
        [sg.Text('Potas',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='potas-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='potas-norma', size=(15,1)),                       sg.Text('Sód',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='sod-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='sod-norma', size=(15,1))],
        
        [sg.Text('Chlorki',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='chlorki-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='chlorki-norma', size=(15,1))],
        [sg.Text('Uwagi:',font=('Helvetica', 12), size=(10,1)), sg.Input(key='uwagi', size=(50,1))],
        [sg.Button('Do PDF'), sg.Button('Wyczyść')]

    ]

    okno = sg.Window('Kanis Diagnostyka', layout=layout)


    while True:
        event, values = okno.read()
        if event == sg.WIN_CLOSED or event=='Exit':
            break
        if values['animal-type']=='Pies':
            okno['ast-norma'].update((ast_psa_norma))
            okno['alt-norma'].update((alt_psa_norma))
            okno['alp-norma'].update((alp_psa_norma))
            okno['bilirubina-norma'].update((bilirubina_psa_norma))
            okno['ggt-norma'].update((ggt_psa_norma))
            okno['ldh-norma'].update((ldh_psa_norma))
            okno['cholesterol-norma'].update((cholesterol_psa_norma))
            okno['triglicerydy-norma'].update((triglicerydy_psa_norma))
            okno['kw-zolt-norma'].update((kw_zolt_psa_norma))
            okno['bialko-norma'].update((białko_psa_norma))
            okno['albuminy-norma'].update(albuminy_psa_norma)
            okno['glukoza-norma'].update((glukoza_psa_norma))
            okno['fruktozamina-norma'].update((fruktozamina_psa_norma))
            okno['mocznik-norma'].update((mocznik_psa_norma))
            okno['kreatynina-norma'].update((kreatynina_psa_norma))
            okno['kinaza-norma'].update((kinaza_psa_norma))
            okno['amylaza-norma'].update((amylaza_psa_norma))
            okno['lipaza-norma'].update((lipaza_psa_norma))
            okno['wapn-norma'].update((wapn_psa_norma))
            okno['fosfor-norma'].update((fosfor_psa_norma))
            okno['magnez-norma'].update((magnez_psa_norma))
            okno['zelazo-norma'].update((zelazo_psa_norma))
            okno['potas-norma'].update((potas_psa_norma))
            okno['sod-norma'].update((sod_psa_norma))
            okno['chlorki-norma'].update((chlorki_psa_norma))
        if values['animal-type']=='Kot':
            okno['ast-norma'].update((ast_kot_norma))
            okno['alt-norma'].update((alt_kot_norma))
            okno['alp-norma'].update((alp_kot_norma))
            okno['bilirubina-norma'].update((bilirubina_kot_norma))
            okno['ggt-norma'].update((ggt_kot_norma))
            okno['ldh-norma'].update((ldh_kot_norma))
            okno['cholesterol-norma'].update((cholesterol_kot_norma))
            okno['triglicerydy-norma'].update((triglicerydy_kot_norma))
            okno['kw-zolt-norma'].update((kw_zolt_kot_norma))
            okno['bialko-norma'].update((białko_kot_norma))
            okno['albuminy-norma'].update(albuminy_kot_norma)
            okno['glukoza-norma'].update((glukoza_kot_norma))
            okno['fruktozamina-norma'].update((fruktozamina_kot_norma))
            okno['mocznik-norma'].update((mocznik_kot_norma))
            okno['kreatynina-norma'].update((kreatynina_kot_norma))
            okno['kinaza-norma'].update((kinaza_kot_norma))
            okno['amylaza-norma'].update((amylaza_kot_norma))
            okno['lipaza-norma'].update((lipaza_kot_norma))
            okno['wapn-norma'].update((wapn_kot_norma))
            okno['fosfor-norma'].update((fosfor_kot_norma))
            okno['magnez-norma'].update((magnez_kot_norma))
            okno['zelazo-norma'].update((zelazo_kot_norma))
            okno['potas-norma'].update((potas_kot_norma))
            okno['sod-norma'].update((sod_kot_norma))
            okno['chlorki-norma'].update((chlorki_kot_norma))
        
        if event == 'Do PDF':
            
            file_name = f'{values["owner"]}_{values["pet-name"]}_{cur_date.year}{cur_date.month}{cur_date.day}{cur_date.hour}{cur_date.minute}'
            complete_filename = os.path.join(save_location,file_name)
            report_date = f'{cur_date.year}-{cur_date.month}-{cur_date.day}'
            to_open = complete_filename+'.pdf'
            
            for x in range(len(badania)):
                badania[x] = values[f'{badania_odw[x].lower()}-wynik'].replace(',','.')
                if badania[x]!='' and badania[x][0] and badania[x][-1] in ('0123456789.'):
                
                    badania[x] = float(badania[x])
               
                elif badania[x]!='' and badania[x][0] and badania[x][-1] not in ('0123456789.'):
                    sg.Popup(f'Błędne dane {badania_odw[x]}', keep_on_top=True)
                    okno[f'{badania_odw[x]}-wynik'].update('')
                elif badania[x]=='':
                    pass


            
            
        
            raport_pdf = diag_canvas(complete_filename,report_date,values['order-no'],values['animal-type'],values['owner'],values['pet-name'],
            badania[0], 
            badania[1],
            badania[2], 
            badania[3], 
            badania[4],
            badania[5],
            badania[6],
            badania[7],
            badania[8],
            badania[9],
            badania[10],
            badania[11],
            badania[12],
            badania[13],
            badania[14], 
            badania[15], 
            badania[16],
            badania[17], 
            badania[18],
            badania[19],
            badania[20], 
            badania[21], 
            badania[22], 
            badania[23], 
            badania[24],
            values['uwagi'])

            subprocess.Popen(to_open, shell=True)

        elif event=='Wyczyść':
            okno['order-no'].update('')
            okno['owner'].update('')
            okno['animal-type'].update('Pies')
            okno['pet-name'].update('')
            okno['ast-wynik'].update('')
            okno['alt-wynik'].update('')
            okno['alp-wynik'].update('')
            okno['bilirubina-wynik'].update('')
            okno['ggt-wynik'].update('')
            okno['ldh-wynik'].update('')
            okno['cholesterol-wynik'].update('')
            okno['triglicerydy-wynik'].update('')
            okno['kw-zolt-wynik'].update('')
            okno['bialko-wynik'].update('')
            okno['albuminy-wynik'].update('')
            okno['glukoza-wynik'].update('')
            okno['fruktozamina-wynik'].update('')
            okno['mocznik-wynik'].update('')
            okno['kreatynina-wynik'].update('')
            okno['kinaza-wynik'].update('')
            okno['amylaza-wynik'].update('')
            okno['lipaza-wynik'].update('')
            okno['wapn-wynik'].update('')
            okno['fosfor-wynik'].update('')
            okno['magnez-wynik'].update('')
            okno['zelazo-wynik'].update('')
            okno['potas-wynik'].update('')
            okno['sod-wynik'].update('')
            okno['chlorki-wynik'].update('')
            okno['uwagi'].update('')


        
    okno.close()



if __name__ == '__main__':
    main()
