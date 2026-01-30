import tkinter as tk
from tkinter import ttk

class Prestamo_view:
    def __init__(self, root):
        self.root = root
        self.root.title("Préstamo de equipo")
        
        width, height = 1000, 600
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw // 2) - (width // 2)
        y = (sh // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(True, True)
        
        # 메인 레이아웃 설정 (좌측 입력 / 우측 버튼)
        self.root.columnconfigure(0, weight=3)  # 입력 영역 비중 확대
        self.root.columnconfigure(1, weight=1)

        # ─────────────── 왼쪽 영역: 입력 폼 ───────────────
        # grid를 사용하여 라벨과 입력창의 세로 줄을 맞춤
        self.frame_inputs = tk.Frame(self.root)
        self.frame_inputs.grid(row=0, column=0, padx=50, pady=30, sticky="nsew")

        # 1. Estudiante (줄바꿈 라벨 적용 예시)
        tk.Label(self.frame_inputs, text="Código o cédula\nestudiante:", font=('calibre', 10, 'bold'), justify="left").grid(row=0, column=0, sticky="w", pady=10)
        self.inputEstudiante = tk.Entry(self.frame_inputs, width=40, font=('calibre', 10))
        self.inputEstudiante.grid(row=0, column=1, padx=10, sticky="w")

        # 2. Placa
        tk.Label(self.frame_inputs, text="Placa:", font=('calibre', 10, 'bold')).grid(row=1, column=0, sticky="w", pady=10)
        self.inputPlaca = tk.Entry(self.frame_inputs, width=40, font=('calibre', 10))
        self.inputPlaca.grid(row=1, column=1, padx=10, sticky="w")

        # 3. Multa
        tk.Label(self.frame_inputs, text="Multa:", font=('calibre', 10, 'bold')).grid(row=2, column=0, sticky="w", pady=10)
        self.inputMulta = tk.Entry(self.frame_inputs, width=40, font=('calibre', 10))
        self.inputMulta.grid(row=2, column=1, padx=10, sticky="w")

        # 4. Consumibles (스크롤 가능)
        tk.Label(self.frame_inputs, text="Consumibles:", font=('calibre', 10, 'bold')).grid(
            row=3, column=0, sticky="nw", pady=10
        )

        # 컨테이너 (Canvas + Scrollbar)
        cons_container = tk.Frame(self.frame_inputs)
        cons_container.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.cons_canvas = tk.Canvas(cons_container, width=360, height=170, highlightthickness=1)
        self.cons_canvas.pack(side="left", fill="both", expand=True)

        self.cons_scrollbar = tk.Scrollbar(cons_container, orient="vertical", command=self.cons_canvas.yview)
        self.cons_scrollbar.pack(side="right", fill="y")

        self.cons_canvas.configure(yscrollcommand=self.cons_scrollbar.set)

        # Canvas 안에 실제로 Entry들이 들어갈 프레임
        self.frame_ipConsumibles = tk.Frame(self.cons_canvas)
        self.cons_window = self.cons_canvas.create_window((0, 0), window=self.frame_ipConsumibles, anchor="nw")

        # 스크롤 영역 자동 갱신
        def _update_scrollregion(event=None):
            self.cons_canvas.configure(scrollregion=self.cons_canvas.bbox("all"))

        self.frame_ipConsumibles.bind("<Configure>", _update_scrollregion)

        # Canvas 크기 변경 시 inner frame 폭 맞추기
        def _resize_inner(event):
            self.cons_canvas.itemconfigure(self.cons_window, width=event.width)

        self.cons_canvas.bind("<Configure>", _resize_inner)

        # 마우스휠 스크롤 (Windows)
        self.cons_canvas.bind_all(
            "<MouseWheel>",
            lambda e: self.cons_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        )

        self.consumibles = []
        # ─────────────── 오른쪽 영역: 액션 버튼 ───────────────
        self.frame_botones = tk.LabelFrame(self.root, text="Acciones", padx=20, pady=20) # 시각적 구분을 위해 LabelFrame 사용
        self.frame_botones.grid(row=0, column=1, padx=30, pady=30, sticky="ne")

        # 버튼들을 세로로 예쁘게 배치
        btn_config = {'width': 15, 'pady': 5}
        
        self.btn_add = tk.Button(self.frame_botones, text="+ Consumible", command=self.add_consumible, **btn_config)
        self.btn_add.pack(pady=5)

        self.btn_registrar = tk.Button(self.frame_botones, text="Registrar", bg="#e1f5fe", **btn_config)
        self.btn_registrar.pack(pady=5)

        self.btn_entregar = tk.Button(self.frame_botones, text="Entregar", bg="#e8f5e9", **btn_config)
        self.btn_entregar.pack(pady=5)

        self.btn_clear = tk.Button(self.frame_botones, text="Limpiar datos", **btn_config)
        self.btn_clear.pack(pady=20) # 하단에 조금 떨어뜨려 배치

    # ─────────────── 기능 메서드 ───────────────
    def add_consumible(self):
        var = tk.StringVar()
        # 삭제 버튼이 포함된 프레임을 추가하면 더 좋습니다 (선택 사항)
        entry = tk.Entry(self.frame_ipConsumibles, width=35, textvariable=var)
        entry.pack(pady=2, anchor="w")
        self.consumibles.append(var)

    def get_placa(self): return self.inputPlaca.get()
    def get_inf_Estudiante(self): return self.inputEstudiante.get()
    def get_multa(self): return self.inputMulta.get()
    def get_consumibles(self): return [c.get() for c in self.consumibles]
    
    def set_placa(self, placa):
        self.inputPlaca.delete(0, tk.END)
        self.inputPlaca.insert(0, placa)

    def clear(self):
        self.inputEstudiante.delete(0, tk.END)
        self.inputPlaca.delete(0, tk.END)
        self.inputMulta.delete(0, tk.END)
        for widget in self.frame_ipConsumibles.winfo_children():
            widget.destroy()
        self.consumibles.clear()