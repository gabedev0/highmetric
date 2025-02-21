from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, SlideTransition, NoTransition
from kivymd.uix.menu import MDDropdownMenu
from tipos import *
from kivy.core.window import Window
import webbrowser, json, os


class MenuScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = NoTransition()


class AnguloScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "graus_para_radianos":
                        resultado = graus_para_radianos(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} radianos"
                    case "radianos_para_graus":
                        resultado = radianos_para_graus(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} graus"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class AreaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "m2_para_ha":
                        resultado = metros_quadrados_para_hectares(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} hectares"
                    case "ha_para_m2":
                        resultado = hectares_para_metros_quadrados(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} m²"
                    case "m2_para_acres":
                        resultado = metros_quadrados_para_acres(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} acres"
                    case "acres_para_m2":
                        resultado = acres_para_metros_quadrados(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} m²"
                    case "pes2_para_m2":
                        resultado = pes_quadrados_para_metros_quadrados(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} m²"
                    case "m2_para_pes2":
                        resultado = metros_quadrados_para_pes_quadrados(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} pés²"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class ComprimentoScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "m_para_km":
                        resultado = metros_para_quilometros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} km"
                    case "km_para_m":
                        resultado = quilometros_para_metros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} m"
                    case "m_para_milhas":
                        resultado = metros_para_milhas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} milhas"
                    case "milhas_para_m":
                        resultado = milhas_para_metros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} m"
                    case "pol_para_cm":
                        resultado = polegadas_para_centimetros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} cm"
                    case "cm_para_pol":
                        resultado = centimetros_para_polegadas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} polegadas"
                    case "pes_para_m":
                        resultado = pes_para_metros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} m"
                    case "m_para_pes":
                        resultado = metros_para_pes(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} pés"
                    case "jardas_para_m":
                        resultado = jardas_para_metros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} m"
                    case "m_para_jardas":
                        resultado = metros_para_jardas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} jardas"
                    case "cicero_para_milimetros":
                        resultado = cicero_para_milimetros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} mm"
                    case "milimetros_para_cicero":
                        resultado = milimetros_para_cicero(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} cicero"
                    case "cicero_para_pontos":
                        resultado = cicero_para_pontos(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} pontos"
                    case "pontos_para_cicero":
                        resultado = pontos_para_cicero(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} cicero"
                    case "pontos_para_milimetros":
                        resultado = pontos_para_milimetros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} mm"
                    case "milimetros_para_pontos":
                        resultado = milimetros_para_pontos(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} pontos"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class DensidadeScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "kg_m3_para_g_cm3":
                        resultado = kg_por_metro_cubico_para_g_por_cm_cubico(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.6f} g/cm³"
                    case "g_cm3_para_kg_m3":
                        resultado = g_por_cm_cubico_para_kg_por_metro_cubico(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} kg/m³"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class DigitalScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "bytes_para_kb":
                        resultado = bytes_para_kilobytes(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} KB"
                    case "kb_para_bytes":
                        resultado = kilobytes_para_bytes(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} bytes"
                    case "mb_para_gb":
                        resultado = megabytes_para_gigabytes(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} GB"
                    case "gb_para_mb":
                        resultado = gigabytes_para_megabytes(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} MB"
                    case "tb_para_pb":
                        resultado = terabytes_para_petabytes(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} PB"
                    case "pb_para_tb":
                        resultado = petabytes_para_terabytes(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} TB"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class EnergiaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "joules_para_kcal":
                        resultado = joules_para_quilocalorias(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.6f} kcal"
                    case "kcal_para_joules":
                        resultado = quilocalorias_para_joules(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} J"
                    case "joules_para_kwh":
                        resultado = joules_para_quilowatt_horas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.6f} kWh"
                    case "kwh_para_joules":
                        resultado = quilowatt_horas_para_joules(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} J"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class ForcaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "newtons_para_kgf":
                        resultado = newtons_para_kgf(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} kgf"
                    case "kgf_para_newtons":
                        resultado = kgf_para_newtons(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} N"
                    case "newtons_para_lbf":
                        resultado = newtons_para_lbf(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} lbf"
                    case "lbf_para_newtons":
                        resultado = lbf_para_newtons(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} N"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class ImcScreen(Screen):
    genero = None

    def selecionar_genero(self, genero, active):
        if active:
            self.genero = genero
        else:
            self.genero = None

    def calcular_imc(self):
        peso = self.ids.peso_input.text
        altura = self.ids.altura_input.text

        if not peso or not altura:
            self.ids.resultado.text = "Por favor, preencha todos os campos."
            return

        try:
            peso = float(peso)
            altura = float(altura)
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc, self.genero)
            self.ids.resultado.text = f"Seu IMC é: {imc:.2f}\nClassificação: {classificacao}"
        except:
            self.ids.resultado.text = "Por favor, preencha todos os campos."


class MoedaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_origem = None
        self.menu_destino = None

    def abrir_menu_moedas(self, caller, tipo):
        moedas = listar_moedas()
        if isinstance(moedas, list):
            menu_items = [
                {
                    "text": moeda,
                    "on_release": lambda x=moeda, t=tipo: self.selecionar_moeda(x, t),
                } for moeda in moedas
            ]
            if tipo == "origem":
                self.menu_origem = MDDropdownMenu(caller=caller, items=menu_items, position="center")
                self.menu_origem.open()
            elif tipo == "destino":
                self.menu_destino = MDDropdownMenu(caller=caller, items=menu_items, position="center")
                self.menu_destino.open()

    def selecionar_moeda(self, moeda, tipo):
        if tipo == "origem":
            self.ids.moeda_origem.text = moeda
            if self.menu_origem:
                self.menu_origem.dismiss()
        elif tipo == "destino":
            self.ids.moeda_destino.text = moeda
            if self.menu_destino:
                self.menu_destino.dismiss()

    def converter(self):
        valor = self.ids.valor_input.text
        moeda_origem = self.ids.moeda_origem.text
        moeda_destino = self.ids.moeda_destino.text

        if valor and moeda_origem != "Selecione a moeda de origem" and moeda_destino != "Selecione a moeda de destino":
            try:
                valor = float(valor)
                resultado = converter_moeda(valor, moeda_origem, moeda_destino)
                self.ids.resultado.text = f"{moeda_destino} {resultado:.2f}"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Preencha todos os campos."


class PesoScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "kg_para_g":
                        resultado = quilogramas_para_gramas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} g"
                    case "g_para_kg":
                        resultado = gramas_para_quilogramas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} kg"
                    case "kg_para_lb":
                        resultado = quilogramas_para_libras(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} lb"
                    case "lb_para_kg":
                        resultado = libras_para_quilogramas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} kg"
                    case "t_para_kg":
                        resultado = toneladas_para_quilogramas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} kg"
                    case "kg_para_t":
                        resultado = quilogramas_para_toneladas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} t"
                    case "oz_para_g":
                        resultado = oncas_para_gramas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} g"
                    case "g_para_oz":
                        resultado = gramas_para_oncas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} oz"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class PressaoScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "pascal_para_bar":
                        resultado = pascal_para_bar(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.6f} bar"
                    case "bar_para_pascal":
                        resultado = bar_para_pascal(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} Pa"
                    case "pascal_para_psi":
                        resultado = pascal_para_psi(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.6f} psi"
                    case "psi_para_pascal":
                        resultado = psi_para_pascal(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} Pa"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class TemperaturaScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "celsius_para_fahrenheit":
                        resultado = celsius_para_fahrenheit(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} °F"
                    case "fahrenheit_para_celsius":
                        resultado = fahrenheit_para_celsius(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} °C"
                    case "celsius_para_kelvin":
                        resultado = celsius_para_kelvin(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} K"
                    case "kelvin_para_celsius":
                        resultado = kelvin_para_celsius(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} °C"
                    case "fahrenheit_para_kelvin":
                        resultado = fahrenheit_para_kelvin(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} K"
                    case "kelvin_para_fahrenheit":
                        resultado = kelvin_para_fahrenheit(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} °F"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class TempoScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "segundos_para_minutos":
                        resultado = segundos_para_minutos(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} minutos"
                    case "minutos_para_segundos":
                        resultado = minutos_para_segundos(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} segundos"
                    case "minutos_para_horas":
                        resultado = minutos_para_horas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} horas"
                    case "horas_para_minutos":
                        resultado = horas_para_minutos(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} minutos"
                    case "horas_para_dias":
                        resultado = horas_para_dias(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} dias"
                    case "dias_para_horas":
                        resultado = dias_para_horas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} horas"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class VelocidadeScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "kmh_para_mph":
                        resultado = kmh_para_mph(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} mph"
                    case "mph_para_kmh":
                        resultado = mph_para_kmh(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} km/h"
                    case "mps_para_kmh":
                        resultado = mps_para_kmh(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} km/h"
                    case "kmh_para_mps":
                        resultado = kmh_para_mps(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} m/s"
                    case "nos_para_kmh":
                        resultado = nos_para_kmh(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} km/h"
                    case "kmh_para_nos":
                        resultado = kmh_para_nos(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} nós"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido."
        else:
            self.ids.resultado.text = "Digite um valor."


class VolumeScreen(Screen):
    def on_pre_enter(self):
        self.manager.transition = SlideTransition(direction='right')

    def converter(self, tipo):
        valor = self.ids.valor_input.text
        if valor:
            try:
                valor = float(valor)
                match tipo:
                    case "litros_para_ml":
                        resultado = litros_para_mililitros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} ml"
                    case "ml_para_litros":
                        resultado = mililitros_para_litros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} litros"
                    case "litros_para_galoes":
                        resultado = litros_para_galoes(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} galões"
                    case "galoes_para_litros":
                        resultado = galoes_para_litros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} litros"
                    case "xicaras_para_ml":
                        resultado = xicaras_para_mililitros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} ml"
                    case "ml_para_xicaras":
                        resultado = mililitros_para_xicaras(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} xícaras"
                    case "oncas_para_litros":
                        resultado = oncas_liquidas_para_litros(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.4f} litros"
                    case "litros_para_oncas":
                        resultado = litros_para_oncas_liquidas(valor)
                        self.ids.resultado.text = f"Resultado: {resultado:.2f} onças"
            except ValueError:
                self.ids.resultado.text = "Erro: Valor inválido"
        else:
            self.ids.resultado.text = "Digite um valor"


CACHE_FILE = "cache.json"


class HighMetric(MDApp):
    def build(self):
        Window.size = (360, 640)

        self.carregar_tema()
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.5

        return Builder.load_file("tela.kv")

    def trocar_tema(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.primary_palette = "LightBlue"
            self.theme_cls.theme_style = "Light"
        self.salvar_tema()

    def salvar_tema(self):
        tema_config = {
            "tema": self.theme_cls.theme_style,
            "cor_primaria": self.theme_cls.primary_palette
        }
        with open(CACHE_FILE, "w",) as arquivo:
            json.dump(tema_config, arquivo, indent=4)

    def carregar_tema(self):
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r",) as arquivo:
                    tema_config = json.load(arquivo)
                    self.theme_cls.theme_style = tema_config.get("tema", "Light")
                    self.theme_cls.primary_palette = tema_config.get("cor_primaria", "Blue")
            except:
                self.theme_cls.theme_style = "Light"
                self.theme_cls.primary_palette = "Blue"
        else:
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"

    def abrir_documentacao(self):
        url = "https://github.com/gabedev0/highmetric-PISI-1"
        webbrowser.open(url)


if __name__ == "__main__":
    HighMetric().run()