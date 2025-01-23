tela = """
ScreenManager:
    id: screen_manager
    
    MenuScreen:
    AnguloScreen:
    AreaScreen:
    ComprimentoScreen:
    DensidadeScreen:
    DigitalScreen:
    EnergiaScreen:
    ForcaScreen:
    MoedaScreen:
    PesoScreen:
    PressaoScreen:
    TemperaturaScreen:
    TempoScreen:
    VelocidadeScreen:
    VolumeScreen:

<MenuScreen>:
    name: 'menu'
    MDScreen:
        md_bg_color:
        
    MDTopAppBar:
        title: "HighMetric"
        center_title: True
        left_action_items: [["information-outline", lambda x: print("Apertado")]]
        right_action_items: [["lightbulb", lambda x: app.trocar_tema()]]


    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.2, 'center_y': 0.9}

        MDIconButton:
            icon: 'imgs/angulo_icon.png'
            size_hint: None, None
            size: "160dp", "160dp"
            on_press: root.manager.current = 'angulo'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Ângulo'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

        MDIconButton:
            icon: 'imgs/area_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'area'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Área'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.8, 'center_y': 0.9}

        MDIconButton:
            icon: 'imgs/comprimento_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'comprimento'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Tamanho'
            text_size: self.size
            width: self.texture_size[0]
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.2, 'center_y': 0.8}

        MDIconButton:
            icon: 'imgs/densidade_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'densidade'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Densidade'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True


    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

        MDIconButton:
            icon: 'imgs/digital_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'digital'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Digital'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.8, 'center_y': 0.8}

        MDIconButton:
            icon: 'imgs/energia_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'energia'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Energia'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.2, 'center_y': 0.7}

        MDIconButton:
            icon: 'imgs/forca_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'forca'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Força'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}

        MDIconButton:
            icon: 'imgs/moeda_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'moeda'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Moeda'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.8, 'center_y': 0.7}

        MDIconButton:
            icon: 'imgs/peso_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'peso'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Peso'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.2, 'center_y': 0.6}

        MDIconButton:
            icon: 'imgs/pressao_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'pressao'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Pressão'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}

        MDIconButton:
            icon: 'imgs/temperatura_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'temperatura'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Tempérie'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.8, 'center_y': 0.6}

        MDIconButton:
            icon: 'imgs/tempo_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'tempo'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Tempo'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.2, 'center_y': 0.5}

        MDIconButton:
            icon: 'imgs/velocidade_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'velocidade'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Velocidade'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: self.minimum_size
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDIconButton:
            icon: 'imgs/volume_icon.png'
            size_hint: None, None
            size: "128dp", "128dp"
            on_press: root.manager.current = 'volume'
            canvas.before:
                Color:
                    rgba: 0.66, 0.66, 0.66, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [12]

        MDLabel:
            text: 'Volume'
            halign: 'center'
            font_size: '10dp'
            size_hint_y: None
            height: self.texture_size[1]
            max_lines: 1
            bold: True


<VoltarMenu@MDRectangleFlatButton>:
    text: "Voltar"
    size_hint_x: 0.8
    pos_hint: {"center_x": 0.5, "center_y": 0.1}
    on_release: app.root.current = 'menu'

<AnguloScreen>:
    name: 'angulo'
    MDScreen:
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: "Conversor de Ângulos"
                halign: 'center'
                font_style: 'H5'

            MDTextField:
                id: valor_input
                hint_text: "Digite o valor"
                input_filter: 'float'
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                
            MDLabel:
                id: resultado
                text: "Resultado:"
                halign: 'center'
                font_style: 'H6'

            MDRectangleFlatButton:
                text: "Graus para Radianos"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter("graus_para_radianos")

            MDRectangleFlatButton:
                text: "Radianos para Graus"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter("radianos_para_graus")

            Widget:
                size_hint_y: None
                height: "20dp"

            VoltarMenu:
            

<AreaScreen>:
    name: 'area'
    MDScreen:
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: "Conversor de Área"
                halign: 'center'
                font_style: 'H5'

            MDTextField:
                id: valor_input
                hint_text: "Digite o valor"
                input_filter: 'float'
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                
            MDLabel:
                id: resultado
                text: "Resultado:"
                halign: 'center'
                font_style: 'H6'
                height: self.texture_size[1]

            MDRectangleFlatButton:
                text: "Metros² para Hectares"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter("m2_para_ha")

            MDRectangleFlatButton:
                text: "Hectares para Metros²"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter("ha_para_m2")

            MDRectangleFlatButton:
                text: "Metros² para Acres"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter("m2_para_acres")

            MDRectangleFlatButton:
                text: "Acres para Metros²"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter("acres_para_m2")

            MDRectangleFlatButton:
                text: "Pés² para Metros²"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter("pes2_para_m2")

            MDRectangleFlatButton:
                text: "Metros² para Pés²"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter("m2_para_pes2")
            
            Widget:
                size_hint_y: None
                height: "20dp"
                
            VoltarMenu:

<ComprimentoScreen>:
    name: 'comprimento'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5} 

                MDLabel:
                    text: "Conversor de Comprimento"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Metros para Quilômetros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("m_para_km")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Quilômetros para Metros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("km_para_m")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Metros para Milhas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("m_para_milhas")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Milhas para Metros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("milhas_para_m")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Polegadas para Centímetros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("pol_para_cm")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Centímetros para Polegadas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("cm_para_pol")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Pés para Metros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("pes_para_m")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Metros para Pés"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("m_para_pes")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Jardas para Metros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("jardas_para_m")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Metros para Jardas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("m_para_jardas")
                    size_hint_y: None
                    height: "48dp"
                    
                MDRectangleFlatButton:
                    text: "Cicero para Milimetros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("cicero_para_milimetros")
                    size_hint_y: None
                    height: "48dp"
                    
                MDRectangleFlatButton:
                    text: "Milimetros para Cicero"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("milimetros_para_cicero")
                    size_hint_y: None
                    height: "48dp"
                    
                MDRectangleFlatButton:
                    text: "Cicero para Pontos"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("cicero_para_pontos")
                    size_hint_y: None
                    height: "48dp"
                    
                MDRectangleFlatButton:
                    text: "Pontos para Cicero"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("pontos_para_cicero")
                    size_hint_y: None
                    height: "48dp"
                    
                MDRectangleFlatButton:
                    text: "Pontos para Milimetros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("pontos_para_milimetros")
                    size_hint_y: None
                    height: "48dp"
                    
                MDRectangleFlatButton:
                    text: "Milimetros para Pontos"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("milimetros_para_pontos")
                    size_hint_y: None
                    height: "48dp"

                Widget:
                    size_hint_y: None
                    height: "20dp"

                VoltarMenu:

<DensidadeScreen>:
    name: 'densidade'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

                MDLabel:
                    text: "Conversor de Densidade"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "kg/m³ para g/cm³"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kg_m3_para_g_cm3")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "g/cm³ para kg/m³"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("g_cm3_para_kg_m3")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "255dp"

                VoltarMenu:

<DigitalScreen>:
    name: 'digital'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

                MDLabel:
                    text: "Conversor de Unidades Digitais"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Bytes para Kilobytes"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("bytes_para_kb")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Kilobytes para Bytes"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kb_para_bytes")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Megabytes para Gigabytes"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("mb_para_gb")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Gigabytes para Megabytes"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("gb_para_mb")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Terabytes para Petabytes"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("tb_para_pb")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Petabytes para Terabytes"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("pb_para_tb")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "20dp"

                VoltarMenu:

<EnergiaScreen>:
    name: 'energia'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                
                MDLabel:
                    text: "Conversor de Energia"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Joules para Quilocalorias"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("joules_para_kcal")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Quilocalorias para Joules"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kcal_para_joules")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Joules para Quilowatt-horas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("joules_para_kwh")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Quilowatt-horas para Joules"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kwh_para_joules")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "150dp"

                VoltarMenu:

<ForcaScreen>:
    name: 'forca'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

                MDLabel:
                    text: "Conversor de Força"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: ""
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Newtons para kgf"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("newtons_para_kgf")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "kgf para Newtons"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kgf_para_newtons")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Newtons para lbf"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("newtons_para_lbf")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "lbf para Newtons"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("lbf_para_newtons")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "165dp"

                VoltarMenu:

<MoedaScreen>:
    name: 'moeda'
    MDScreen:
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "20dp"
            size_hint_y: None
            height: self.minimum_height 
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
            Widget:
                size_hint_y: None
                height: "10dp"

            MDLabel:
                text: "Conversor de Moedas"
                halign: 'center'
                font_style: 'H5'
                
            Widget:
                size_hint_y: None
                height: "10dp"

            MDTextField:
                id: valor_input
                hint_text: "Digite o valor"
                input_filter: 'float'
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                
            MDLabel:
                id: resultado
                text: ""
                halign: 'center'
                font_style: 'H6'
                size_hint_y: None
                height: self.texture_size[1]
                
            Widget:
                size_hint_y: None
                height: "20dp"

            MDRectangleFlatButton:
                id: moeda_origem
                text: "Selecione a moeda de origem"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.abrir_menu_moedas(self, "origem")

            MDRectangleFlatButton:
                id: moeda_destino
                text: "Selecione a moeda de destino"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.abrir_menu_moedas(self, "destino")

            MDRectangleFlatButton:
                text: "Converter"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}
                on_release: root.converter()
                
            Widget:
                size_hint_y: None
                height: "160dp"

            VoltarMenu:


<PesoScreen>:
    name: 'peso'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5} 

                MDLabel:
                    text: "Conversor de Peso"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Quilogramas para Gramas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kg_para_g")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Gramas para Quilogramas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("g_para_kg")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Quilogramas para Libras"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kg_para_lb")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Libras para Quilogramas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("lb_para_kg")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Toneladas para Quilogramas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("t_para_kg")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Quilogramas para Toneladas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kg_para_t")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Onças para Gramas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("oz_para_g")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Gramas para Onças"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("g_para_oz")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "20dp"

                VoltarMenu:

<PressaoScreen>:
    name: 'pressao'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5}  

                MDLabel:
                    text: "Conversor de Pressão"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Pascal para Bar"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("pascal_para_bar")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Bar para Pascal"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("bar_para_pascal")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Pascal para PSI"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("pascal_para_psi")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "PSI para Pascal"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("psi_para_pascal")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "150dp"

                VoltarMenu:

<TemperaturaScreen>:
    name: 'temperatura'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5}  

                MDLabel:
                    text: "Conversor de Temperatura"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Celsius para Fahrenheit"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("celsius_para_fahrenheit")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Fahrenheit para Celsius"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("fahrenheit_para_celsius")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Celsius para Kelvin"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("celsius_para_kelvin")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Kelvin para Celsius"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kelvin_para_celsius")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Fahrenheit para Kelvin"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("fahrenheit_para_kelvin")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Kelvin para Fahrenheit"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kelvin_para_fahrenheit")
                    size_hint_y: None
                    height: "48dp"

               
                    
                Widget:
                    size_hint_y: None
                    height: "20dp"

                VoltarMenu:

<TempoScreen>:
    name: 'tempo'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5}  

                MDLabel:
                    text: "Conversor de Tempo"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Segundos para Minutos"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("segundos_para_minutos")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Minutos para Segundos"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("minutos_para_segundos")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Minutos para Horas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("minutos_para_horas")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Horas para Minutos"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("horas_para_minutos")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Horas para Dias"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("horas_para_dias")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Dias para Horas"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("dias_para_horas")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "20dp"

                VoltarMenu:

<VelocidadeScreen>:
    name: 'velocidade'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height 
                pos_hint: {"center_x": 0.5, "center_y": 0.5} 

                MDLabel:
                    text: "Conversor de Velocidade"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "km/h para mph"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kmh_para_mph")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "mph para km/h"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("mph_para_kmh")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "m/s para km/h"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("mps_para_kmh")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "km/h para m/s"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kmh_para_mps")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "nós para km/h"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("nos_para_kmh")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "km/h para nós"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("kmh_para_nos")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "30dp"

                VoltarMenu:

<VolumeScreen>:
    name: 'volume'
    MDScreen:
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

                MDLabel:
                    text: "Conversor de Volume"
                    halign: 'center'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDTextField:
                    id: valor_input
                    hint_text: "Digite o valor"
                    input_filter: 'float'
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "48dp"
                    
                MDLabel:
                    id: resultado
                    text: "Resultado:"
                    halign: 'center'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDRectangleFlatButton:
                    text: "Litros para Mililitros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("litros_para_ml")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Mililitros para Litros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("ml_para_litros")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Litros para Galões"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("litros_para_galoes")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Galões para Litros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("galoes_para_litros")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Xícaras para Mililitros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("xicaras_para_ml")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Mililitros para Xícaras"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("ml_para_xicaras")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Onças para Litros"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("oncas_para_litros")
                    size_hint_y: None
                    height: "48dp"

                MDRectangleFlatButton:
                    text: "Litros para Onças"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: root.converter("litros_para_oncas")
                    size_hint_y: None
                    height: "48dp"
                    
                Widget:
                    size_hint_y: None
                    height: "20dp"

                VoltarMenu:
"""