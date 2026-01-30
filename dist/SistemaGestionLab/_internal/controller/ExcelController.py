# controller/Excel_controller.py
import pandas as pd

from service.Elemento_service import Elemento_service
from service.Laboratorio_service import Laboratorio_service
from service.Estado_service import Estado_service
from service.Equipo_service import Equipo_service

from view.ExcelDrop_view import ExcelDropView

class ExcelController:
    def __init__(self, view: ExcelDropView, 
                elemento_service: Elemento_service,
                laboratorio_service: Laboratorio_service,
                estado_service: Estado_service,
                equipo_service: Equipo_service
                ):
        self.view = view
        self.view.controller = self # 뷰에 컨트롤러 자신을 연결
        self.elemento_service = elemento_service
        self.laboratorio_service = laboratorio_service
        self.estado_service = estado_service
        self.equipo_service = equipo_service

    def insert_lab(self,df):
        laboratorios = [str(l).strip() for l in df['laboratorio / ubicación'].unique() if pd.notnull(l) and str(l).strip() != ""]

        for i, lab in enumerate(laboratorios):
            self.laboratorio_service.insertar(lab)

    def insert_elemento(self,df):
        elementos = [str(e).strip() for e in df['descripcion del elemento'].unique() if pd.notnull(e) and str(e).strip() != ""]

        for i, el in enumerate(elementos):
            self.elemento_service.insertar(el)
    
    def insert_equipo(self,df):
        lab_map = self.laboratorio_service.mapear_por_nombre()
        el_map = self.elemento_service.mapear_por_nombre()
        # 4. Equipo 데이터 Insert
        for i, row in df.iterrows():
            placa = str(row['placa']).strip()
            if placa == 'nan':
                placa = ""
            lab = None
            el = None
            if 'laboratorio / ubicación' in df.columns:
                lab = lab_map.get(str(row['laboratorio / ubicación']).strip())
            if 'descripcion del elemento' in df.columns:
                el = el_map.get(str(row['descripcion del elemento']).strip())

            lab_id = None
            if lab != None:
                lab_id = lab.get_idLaboratorio()

            el_id = None
            if el != None:
                el_id = el.get_idElemento()
            self.equipo_service.insertar(placa,el_id,lab_id)

    def handle_excel_import(self):
        file_path = self.view.file_path
        if not file_path:
            return

        try:
            df = pd.read_excel(file_path, dtype=str)
            df.columns = [str(col).lower().strip() for col in df.columns]

            if 'laboratorio / ubicación' in df.columns:
                self.insert_lab(df)
            if 'descripcion del elemento' in df.columns:
                self.insert_elemento(df)
            if 'placa' in df.columns:
                self.insert_equipo(df)

        except Exception as e:
            print(f"Error: {e}")