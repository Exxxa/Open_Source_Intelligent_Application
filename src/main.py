# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.core.window import Window

class DataAnalysisApp(App):
    def build(self):
        
        Window.size = (800, 600)
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        title = Label(
            text='Intelligent Data Analysis',
            size_hint_y=None,
            height=50,
            font_size=24
        )
        main_layout.add_widget(title)
        content = BoxLayout(orientation='horizontal', spacing=10)
        left_panel = BoxLayout(orientation='vertical', size_hint_x=0.3, spacing=10)
        data_source_spinner = Spinner(
            text='Select Data Source',
            values=('Source 1', 'Source 2', 'Source 3', 'Source 4'),
            size_hint_y=None,
            height=40
        )
        left_panel.add_widget(data_source_spinner)
        analysis_spinner = Spinner(
            text='Select Analysis Type',
            values=('Analysis 1', 'Analysis 2', 'Analysis 3'),
            size_hint_y=None,
            height=40
        )
        left_panel.add_widget(analysis_spinner)
        
        fetch_button = Button(
            text='Fetch Data',
            size_hint_y=None,
            height=40
        )
        analyze_button = Button(
            text='Analyze Data',
            size_hint_y=None,
            height=40
        )
        left_panel.add_widget(fetch_button)
        left_panel.add_widget(analyze_button)
        right_panel = BoxLayout(orientation='vertical', size_hint_x=0.7)
        results_label = Label(
            text='Results will appear here',
            valign='top'
        )
        right_panel.add_widget(results_label)
        
        
        content.add_widget(left_panel)
        content.add_widget(right_panel)

        main_layout.add_widget(content)
        
        return main_layout

if __name__ == '__main__':
    DataAnalysisApp().run()