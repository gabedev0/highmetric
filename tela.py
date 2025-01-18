menu = """
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
        left_action_items: [["information-outline", lambda x: print("Informações clicadas")]]
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



<AnguloScreen>:
    name: 'angulo'
    MDScreen:
        MDLabel:
            text: 'ANGULO'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'
            

<AreaScreen>:
    name: 'area'
    MDScreen:
        MDLabel:
            text: 'AREA'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'


<ComprimentoScreen>:
    name: 'comprimento'
    MDScreen:
        MDLabel:
            text: 'COMPRIMENTO'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<DensidadeScreen>:
    name: 'densidade'
    MDScreen:
        MDLabel:
            text: 'DENSIDADE'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<DigitalScreen>:
    name: 'digital'
    MDScreen:
        MDLabel:
            text: 'DIGITAL'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<EnergiaScreen>:
    name: 'energia'
    MDScreen:
        MDLabel:
            text: 'ENERGIA'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<ForcaScreen>:
    name: 'forca'
    MDScreen:
        MDLabel:
            text: 'FORÇA'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<MoedaScreen>:
    name: 'moeda'
    MDScreen:
        MDLabel:
            text: 'MOEDA'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<PesoScreen>:
    name: 'peso'
    MDScreen:
        MDLabel:
            text: 'PESO'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<PressaoScreen>:
    name: 'pressao'
    MDScreen:
        MDLabel:
            text: 'PRESSÃO'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<TemperaturaScreen>:
    name: 'temperatura'
    MDScreen:
        MDLabel:
            text: 'TEMPERATURA'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<TempoScreen>:
    name: 'tempo'
    MDScreen:
        MDLabel:
            text: 'TEMPO'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<VelocidadeScreen>:
    name: 'velocidade'
    MDScreen:
        MDLabel:
            text: 'VELOCIDADE'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<VolumeScreen>:
    name: 'volume'
    MDScreen:
        MDLabel:
            text: 'VOLUME'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Voltar'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'
"""