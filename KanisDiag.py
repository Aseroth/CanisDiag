import PySimpleGUI as sg
import datetime
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
import Kanis_canvas
from Kanis_canvas import diag_canvas
import os

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

    layout = [
        [sg.Text('Numer zlecenia', size=(20,1)), sg.Input(key='order-no')],
        [sg.Text('Właściciel', size=(20,1)), sg.Input(key='owner')],
        [sg.Text('Gatunek', size=(20,1)), sg.Combo(animal_type, default_value='Pies', key='animal-type',enable_events=True)],
        [sg.Text('Imie zwierzęcia', size=(20,1)), sg.Input(key='pet-name')],
        [sg.HorizontalSeparator()],
        [sg.Text('Wynik badań diagnostycznych', font=('Helvetica',20))],
        [sg.Text('Badania biochemiczne krwi', font=('Helvetica',12),size=(25,1))],
        [sg.Text('\t\t\t\t\tNorma')],
        [sg.Text('Kreatynina',font=('Helvetica',12), size=(10,1)), sg.Input(key='kreatynina-wynik', size=(10,1)),sg.Text('mg/dl\t'), sg.Text(key='normy-kreatynina', size=(10,1))],
        [sg.Text('Mocznik',font=('Helvetica',12), size=(10,1)),sg.Input(key='mocznik-wynik', size=(10,1)),sg.Text('mg/dl\t'), sg.Text(key='normy-mocznik')],
        [sg.Text('Fosfor',font=('Helvetica',12), size=(10,1)),sg.Input(key='fosfor-wynik', size=(10,1)),sg.Text('mg/dl\t'), sg.Text(key='normy-fosfor')],
        [sg.Text('ALAT',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='alat-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='alat-norma')],
        [sg.Text('ASPAT',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='aspat-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='aspat-norma')],
        [sg.Text('Białko',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='bialko-wynik', size=(10,1)), sg.Text('g/dl\t'), sg.Text(key='bialko-norma')],
        [sg.Text('Bilirubina',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='bilirubina-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='bilirubina-norma')],
        [sg.Text('ALP',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='alp-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='alp-norma')],
        [sg.Text('Glukoza',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='glukoza-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='glukoza-norma')],
        [sg.Text('Amylaza',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='amylaza-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='amylaza-norma')],
        [sg.Text('Lipaza',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='lipaza-wynik', size=(10,1)), sg.Text('U/l\t'), sg.Text(key='lipaza-norma')],
        [sg.Text('Sód',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='sod-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='sod-norma')],
        [sg.Text('Potas',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='potas-wynik', size=(10,1)), sg.Text('mg/dl\t'), sg.Text(key='potas-norma')],
        [sg.HorizontalSeparator()],
        [sg.Text('Morfologia krwi', font=('Helvetica',12),size=(25,1))],
        [sg.Text('WBC',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='wbc-wynik', size=(10,1)), sg.Text('tys./µl\t'), sg.Text(key='wbc-norma')],
        [sg.Text('RBC',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='rbc-wynik', size=(10,1)), sg.Text('mln/µl\t'), sg.Text(key='rbc-norma')],
        [sg.Text('HGB',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='hgb-wynik', size=(10,1)), sg.Text('g/dl\t'), sg.Text(key='hgb-norma')],
        [sg.Text('HCT',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='hct-wynik', size=(10,1)), sg.Text('%\t'), sg.Text(key='hct-norma')],
        [sg.Text('PLT',font=('Helvetica', 12), size=(10,1) ), sg.Input(key='plt-wynik', size=(10,1)), sg.Text('tys./µl\t'), sg.Text(key='plt-norma')],
        [sg.Text('Uwagi:',font=('Helvetica', 12), size=(10,1)), sg.Input(key='uwagi', size=(50,1))],
        [sg.Button('Do PDF'), sg.Button('Wyczyść')]

    ]

    okno = sg.Window('Kanis Diagnostyka', layout=layout)


    while True:
        event, values = okno.read()
        if event == sg.WIN_CLOSED or event=='Exit':
            break
        if values['animal-type']=='Pies':
            okno['normy-kreatynina'].update((kreatynina_psa_norma))
            okno['normy-mocznik'].update((mocznik_psa_norma))
            okno['normy-fosfor'].update((fosfor_psa_norma))
            okno['alat-norma'].update((alat_psa_norma))
            okno['aspat-norma'].update((aspat_psa_norma))
            okno['bialko-norma'].update((białko_psa_norma))
            okno['bilirubina-norma'].update((bilirubina_psa_norma))
            okno['alp-norma'].update((alp_psa_norma))
            okno['glukoza-norma'].update((glukoza_psa_norma))
            okno['amylaza-norma'].update((amylaza_psa_norma))
            okno['lipaza-norma'].update(lipaza_psa_norma)
            okno['sod-norma'].update((sod_psa_norma))
            okno['potas-norma'].update((potas_psa_norma))
            okno['wbc-norma'].update((wbc_psa_norma))
            okno['rbc-norma'].update((rbc_psa_norma))
            okno['hgb-norma'].update((hgb_psa_norma))
            okno['hct-norma'].update((hct_psa_norma))
            okno['plt-norma'].update((plt_psa_norma))
        if values['animal-type']=='Kot':
            okno['normy-kreatynina'].update((kreatynina_kot_norma))
            okno['normy-mocznik'].update((mocznik_kot_norma))
            okno['normy-fosfor'].update((fosfor_kot_norma))
            okno['alat-norma'].update((alat_kot_norma))
            okno['aspat-norma'].update((aspat_kot_norma))
            okno['bialko-norma'].update((białko_kot_norma))
            okno['bilirubina-norma'].update((bilirubina_kot_norma))
            okno['alp-norma'].update((alp_kot_norma))
            okno['glukoza-norma'].update((glukoza_kot_norma))
            okno['amylaza-norma'].update((amylaza_kot_norma))
            okno['lipaza-norma'].update((lipaza_kot_norma))
            okno['sod-norma'].update((sod_kot_norma))
            okno['potas-norma'].update((potas_kot_norma))
            okno['wbc-norma'].update((wbc_kot_norma))
            okno['rbc-norma'].update((rbc_kot_norma))
            okno['hgb-norma'].update((hgb_kot_norma))
            okno['hct-norma'].update((hct_kot_norma))
            okno['plt-norma'].update((plt_kot_norma))
        
        if event == 'Do PDF':
            
            file_name = f'{values["owner"]}_{values["pet-name"]}_{cur_date.year}{cur_date.month}{cur_date.day}{cur_date.hour}{cur_date.minute}'
            complete_filename = os.path.join(save_location,file_name)
            report_date = f'{cur_date.year}-{cur_date.month}-{cur_date.day}'
            
            kreatynina_wynik = values['kreatynina-wynik'].replace(',','.')
            if kreatynina_wynik!='' and kreatynina_wynik[0] and kreatynina_wynik[-1] in ('0123456789.'):
                
                kreatynina_wynik = float(kreatynina_wynik)
               
            elif kreatynina_wynik!='' and kreatynina_wynik[0] and kreatynina_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane KREATYNINA', keep_on_top=True)
                okno['kreatynina-wynik'].update('')
            elif kreatynina_wynik=='':
                pass

            mocznik_wynik = values['mocznik-wynik'].replace(',','.')
            if mocznik_wynik!='' and mocznik_wynik[0] and mocznik_wynik[-1] in ('0123456789.'):
                mocznik_wynik = float(mocznik_wynik)
            elif mocznik_wynik!='' and mocznik_wynik[0] and mocznik_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane MOCZNIK', keep_on_top=True)
            elif mocznik_wynik=='':
                pass
            

            fosfor_wynik = values['fosfor-wynik'].replace(',','.')
            if fosfor_wynik!='' and fosfor_wynik[0] and fosfor_wynik[-1] in ('0123456789.'):
                fosfor_wynik = float(fosfor_wynik)
            elif fosfor_wynik!=''and fosfor_wynik[0] and fosfor_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane FOSFOR', keep_on_top=True)
            elif fosfor_wynik=='':
                pass
           

            alat_wynik = values['alat-wynik'].replace(',','.')
            if alat_wynik!='' and alat_wynik[0] and alat_wynik[-1] in ('0123456789.'):
                alat_wynik=float(alat_wynik)
            elif alat_wynik!='' and alat_wynik[0] and alat_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane ALAT', keep_on_top=True)
            elif alat_wynik=='':
                pass
            
            aspat_wynik = values['aspat-wynik'].replace(',','.')
            if aspat_wynik!='' and aspat_wynik[0] and aspat_wynik[-1] in ('0123456789.'):
                aspat_wynik=float(aspat_wynik)
            elif aspat_wynik!='' and aspat_wynik[0] and aspat_wynik[-1] in ('0123456789.'):
                sg.Popup('Błędne dane ASPAT', keep_on_top=True)
            elif aspat_wynik=='':
                pass

            bialko_wynik = values['bialko-wynik'].replace(',','.')
            if bialko_wynik!='' and bialko_wynik[0] and bialko_wynik[-1] in ('0123456789.'):
                bialko_wynik=float(bialko_wynik)
            elif bialko_wynik!='' and bialko_wynik[0] and bialko_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane BIAŁKO', keep_on_top=True)
            elif bialko_wynik=='':
                pass

            bilirubina_wynik = values['bilirubina-wynik'].replace(',','.')
            if bilirubina_wynik!='' and bilirubina_wynik[0] and bilirubina_wynik[-1]in ('0123456789.'):
                bilirubina_wynik=float(bilirubina_wynik)
            elif bilirubina_wynik!='' and bilirubina_wynik[0] and bilirubina_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane BILIRUBINA', keep_on_top=True)
            elif bilirubina_wynik=='':
                pass

            alp_wynik = values['alp-wynik'].replace(',','.')
            if alp_wynik!='' and alp_wynik[0] and alp_wynik[-1] in ('0123456789.'):
                alp_wynik=float(alp_wynik)
            elif alp_wynik!='' and alp_wynik[0] and alp_wynik[-1]not in ('0123456789.'):
                sg.Popup('Błędne dane ALP', keep_on_top=True)
            elif alp_wynik=='':
                pass

            glukoza_wynik = values['glukoza-wynik'].replace(',','.')
            if glukoza_wynik!='' and glukoza_wynik[0] and glukoza_wynik[-1] in ('0123456789.'):
                glukoza_wynik=float(glukoza_wynik)
            elif glukoza_wynik!='' and glukoza_wynik[0] and glukoza_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane GLUKOZY', keep_on_top=True)
            elif glukoza_wynik=='':
                pass

            amylaza_wynik = values['amylaza-wynik'].replace(',','.')
            if amylaza_wynik!='' and amylaza_wynik[0] and amylaza_wynik[-1] in ('0123456789.'):
                amylaza_wynik=float(amylaza_wynik)
            elif amylaza_wynik!='' and amylaza_wynik[0] and amylaza_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane AMYLAZA', keep_on_top=True)
            elif amylaza_wynik=='':
                pass

            lipaza_wynik = values['lipaza-wynik'].replace(',','.')
            if lipaza_wynik!='' and lipaza_wynik[0] and lipaza_wynik[-1] in ('0123456789.'):
                lipaza_wynik=float(lipaza_wynik)
            elif lipaza_wynik!='' and lipaza_wynik[0] and lipaza_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane LIPAZA', keep_on_top=True)
            elif lipaza_wynik=='':
                pass

            sod_wynik = values['sod-wynik'].replace(',','.')
            if sod_wynik!='' and sod_wynik[0] and sod_wynik[-1] in ('0123456789.'):
                sod_wynik=float(sod_wynik)
            elif sod_wynik!='' and sod_wynik[0] and sod_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane SÓD', keep_on_top=True)
            elif sod_wynik=='':
                pass

            potas_wynik = values['potas-wynik'].replace(',','.')
            if potas_wynik!='' and potas_wynik[0] and potas_wynik[-1] in ('0123456789.'):
                potas_wynik=float(potas_wynik)
            elif potas_wynik!='' and potas_wynik[0] and potas_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane POTAS', keep_on_top=True)
            elif potas_wynik=='':
                pass

            wbc_wynik = values['potas-wynik'].replace(',','.')
            if wbc_wynik!='' and wbc_wynik[0] and wbc_wynik[-1] in ('0123456789.'):
                wbc_wynik = float(wbc_wynik)
            elif wbc_wynik!='' and wbc_wynik[0] and wbc_wynik[-1] not in ('0123456789.'):
                sg.Popup('Błędne dane WBC', keep_on_top=True)
            elif wbc_wynik=='':
                pass

            rbc_wynik = values['rbc-wynik'].replace(',','.')
            if rbc_wynik!='' and rbc_wynik[0] and rbc_wynik[-1] in ('0123456789.'):
                rbc_wynik=float(rbc_wynik)
            elif rbc_wynik!='' and rbc_wynik[0] and rbc_wynik[-1] in ('0123456789.'):
                sg.Popup('Błędne dane WBC', keep_on_top=True)
            elif rbc_wynik=='':
                pass

            hgb_wynik = values['hgb-wynik'].replace(',','.')
            if hgb_wynik!='' and hgb_wynik[0] and hgb_wynik[-1] in ('0123456789.'):
                hgb_wynik=float(hgb_wynik)
            elif hgb_wynik!='' and hgb_wynik[0] and hgb_wynik[-1] in ('0123456789.'):
                sg.Popup('Błędne dane WBC', keep_on_top=True)
            elif hgb_wynik=='':
                pass

            hct_wynik = values['hct-wynik'].replace(',','.')
            if hct_wynik!='' and hct_wynik[0] and hct_wynik[-1] in ('0123456789.'):
                hct_wynik=float(hct_wynik)
            elif hct_wynik!='' and hct_wynik[0] and hct_wynik[-1] in ('0123456789.'):
                sg.Popup('Błędne dane WBC', keep_on_top=True)
            elif hct_wynik=='':
                pass

            plt_wynik = values['plt-wynik'].replace(',','.')
            if plt_wynik!='' and plt_wynik[0] and plt_wynik[-1] in ('0123456789.'):
                plt_wynik = float(plt_wynik)
            elif plt_wynik!='' and plt_wynik[0] and plt_wynik[-1] in ('0123456789.'):
                sg.Popup('Błędne dane WBC', keep_on_top=True)
            elif plt_wynik=='':
                pass
            
        
            raport_pdf = diag_canvas(complete_filename,report_date,values['order-no'],values['animal-type'],values['owner'],values['pet-name'],kreatynina_wynik,
            mocznik_wynik, fosfor_wynik, alat_wynik, aspat_wynik, bialko_wynik,bilirubina_wynik, alp_wynik, glukoza_wynik, amylaza_wynik, lipaza_wynik,
            sod_wynik, potas_wynik, wbc_wynik, rbc_wynik, hgb_wynik, hct_wynik, plt_wynik, values['uwagi'])
        elif event=='Wyczyść':
            okno['order-no'].update('')
            okno['owner'].update
            okno['animal-type'].update('Pies')
            okno['pet-name'].update('')
            okno['kreatynina-wynik'].update('')
            okno['mocznik-wynik'].update('')
            okno['fosfor-wynik'].update('')
            okno['alat-wynik'].update('')
            okno['aspat-wynik'].update('')
            okno['bialko-wynik'].update('')
            okno['bilirubina-wynik'].update('')
            okno['alp-wynik'].update('')
            okno['glukoza-wynik'].update('')
            okno['amylaza-wynik'].update('')
            okno['lipaza-wynik'].update('')
            okno['sod-wynik'].update('')
            okno['potas-wynik'].update('')
            okno['wbc-wynik'].update('')
            okno['rbc-wynik'].update('')
            okno['hgb-wynik'].update('')
            okno['hct-wynik'].update('')
            okno['plt-wynik'].update('')


        
    okno.close()



if __name__ == '__main__':
    main()
