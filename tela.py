menu = """
ScreenManager:
    MenuScreen:
    AnguloScreen:
    AreaScreen:
    ComprimentoScreen:

<MenuScreen>:
    name: 'menu'
    MDScreen:
        md_bg_color: self.theme_cls.bg_light

    MDTopAppBar:
        title: "HighMetric"
        center_title: True
        left_action_items: [["menu", lambda x: app.toggle_theme()]]

    MDIconButton:
        icon: 'imgs/angulo_icon.png'
        size_hint: None, None
        size: "128dp", "128dp"
        pos_hint: {'center_x':0.2,'center_y':0.9}
        on_press: root.manager.current = 'angulo'
        canvas.before:
            Color:

            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [12]

    MDIconButton:
        icon: 'imgs/area_icon.png'
        size_hint: None, None
        size: "128dp", "128dp"
        pos_hint: {'center_x':0.5,'center_y':0.9}
        on_press: root.manager.current = 'comprimento'
        canvas.before:
            Color:

            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [12]

    MDIconButton:
        icon: 'imgs/comprimento_icon.png'
        size_hint: None, None
        size: "128dp", "128dp"
        pos_hint: {'center_x':0.8,'center_y':0.9}
        on_press: root.manager.current = 'area'
        canvas.before:
            Color:

            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [12]

<AnguloScreen>:
    name: 'angulo'
    MDScreen:
        MDLabel:
            text: 'Tengolengotengo'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

<AreaScreen>:
    name: 'area'
    MDScreen:
        MDLabel:
            text: 'Tengolengotengo'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'


<ComprimentoScreen>:
    name: 'comprimento'
    MDScreen:
        MDLabel:
            text: 'Tengolengotengo'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_press: root.manager.current = 'menu'

"""