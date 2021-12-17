import os

import PySimpleGUI as sg
import yaml

HOME_DIR = os.path.expanduser('~')
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_VERSION = 'v1.0'
AUTHOR = 'Luke & Alan'

main_icon = b'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'
sg.DEFAULT_BASE64_ICON = main_icon

class BarcodeGUI:
    POPUP_FONT = 'Courier 30 bold'
    SCAN_INFO_FONT = 'Courier 20 bold'
    SCAN_INFO_COLOR = 'yellow'
    DEFAULT_INFO_NAME_SIZE = (18, 1)

    TITLE_FRAME_SCAN = 'SCAN SN'

    EVENT_SKU_LIST = '-sku_list-'

    def __init__(self):
        print('Init Barcode GUI')

        self.main_window = None

        # GUI Configuration
        self._gui_setting_path = os.path.join(HOME_DIR, 'gui_setting.yaml')
        self._current_gui_setting = None
        self.update_gui_setting()

        # sku configuration
        self.sku_config = None
        self.scan_events = []
        self.init_sku_config()

    def generator_default_gui_setting(self):
        default = {
            'sku_path': os.path.join(WORKING_DIR, 'sku_configure.yaml'),
            'current_sku': 'HDX-2961',
            'window_location': [200, 200],
        }
        return default

    @property
    def current_gui_setting(self):
        return self._current_gui_setting

    def update_gui_setting(self):
        default_setting = self.generator_default_gui_setting()
        self._current_gui_setting = default_setting

        try:
            if not os.path.exists(self._gui_setting_path):
                with open(self._gui_setting_path, 'a') as f:
                    yaml.dump(default_setting, f, indent=2, sort_keys=False)
                    f.close()
            else:
                with open(self._gui_setting_path, 'r') as f:
                    tmp_setting = yaml.load(f, Loader=yaml.FullLoader)
                    f.close()
                for k, v in self._current_gui_setting.items():
                    setting_value = tmp_setting.get(k, None)
                    if setting_value and setting_value != v:
                        self._current_gui_setting[k] = setting_value
                print('Updated gui setting!')
        except Exception as e:
            print(f'update_gui_setting Error: {e}')
            import traceback
            traceback.print_exc(limit=5)

    def save_gui_setting(self):
        ret = True
        with open(self._gui_setting_path, 'w+', encoding='utf-8') as f:
            try:
                yaml.dump(self._current_gui_setting, f, indent=2, sort_keys=False)
            except Exception as e:
                print(e)
                ret = False
            f.close()
        return ret

    def init_sku_config(self):
        with open(self.current_gui_setting['sku_path'], 'r') as f:
            self.sku_config = yaml.load(f, Loader=yaml.FullLoader)
            print('Load sku configure Done!')

    def scan_layout(self):
        scan_layout = []
        self.scan_events = []
        sku_data_name = self._current_gui_setting['current_sku']
        sku_data = self.sku_config.get(sku_data_name, None)
        if sku_data is None:
            scan_layout.append([sg.T('SKU Empty!'), sg.InputText('Please Choose other SKU!', k=f'-not_found-', font=self.SCAN_INFO_FONT)])
            self.scan_events.append(f'-not_found-')
            return scan_layout

        for item_name, data in sku_data.items():
            scan_layout.append([sg.T(item_name, size=self.DEFAULT_INFO_NAME_SIZE, text_color=self.SCAN_INFO_COLOR, font=self.SCAN_INFO_FONT),
                                sg.InputText('', k=f'-{item_name}-', font=self.SCAN_INFO_FONT),
                                sg.InputText(f'{data}', k=f'target-{item_name}-', font=self.SCAN_INFO_FONT, size=(15, 1), readonly=True)
                                ])
            self.scan_events.append(f'-{item_name}-')
        return scan_layout

    def generate_layout(self):
        menu_def = [['&File', ['&Open SKU File', 'E&xit']],
                    # ['&Settings...', ['Configure'], ],
                    # ['&Debugger', ['Popout', 'Launch Debugger']],
                    # ['!&Disabled', ['Popout', 'Launch Debugger']],
                    # ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
                    ['&Help', ['&Scanner Configure', '&About...']], ]

        layout = [
            [sg.Menu(menu_def, key='_MENU_', font='Courier 15', background_color='grey', text_color='black', disabled_text_color='grey', tearoff=True)],
            [sg.T('SKU:'), sg.DropDown(list(self.sku_config.keys()), default_value=self._current_gui_setting['current_sku'], k=self.EVENT_SKU_LIST, enable_events=True, readonly=True)],
            [sg.Frame(self.TITLE_FRAME_SCAN, self.scan_layout(), font=self.SCAN_INFO_FONT)],
            [sg.Frame('Result', [[sg.T('Status', size=(35, 1), pad=(100, 30, 30, 30), font="Courier 40 bold", k='-status-')]], font=self.SCAN_INFO_FONT)]
        ]
        return layout

    def is_scan_event(self, event):
        return event in self.scan_events

    def barcode_validation(self, barcode, event, all_values):
        # Check valid
        target_barcode = all_values[f'target{event}']
        if barcode != target_barcode:
            sg.popup_error(f'Mã Không đúng!\n\nScanned: {barcode}\nTarget: {target_barcode}', title='ERROR', font=self.POPUP_FONT, text_color=self.SCAN_INFO_COLOR, keep_on_top=True, auto_close=True, auto_close_duration=5)
            self.set_status(f'WRONG "{event.replace("-", "")}"', text_color='red')
            return False
        # Duplicated
        for key, val in all_values.items():
            if event != key and barcode == val and key in self.scan_events:
                sg.popup_error(f'Đã Scan mã này. Scan Mã khác.\nSN: {barcode}', title='ERROR', font=self.POPUP_FONT,
                         text_color=self.SCAN_INFO_COLOR, keep_on_top=True)
                self.set_status(f'DUPLICATED "{event.replace("-", "")}"', text_color='red')
                return False
        return True

    def set_status(self, text='', text_color='white'):
        self.main_window['-status-'].update(text, text_color=text_color)

    def init_main_window(self, sku_name=None):
        if sku_name:
            self._current_gui_setting['current_sku'] = sku_name
        layout = self.generate_layout()
        self.main_window = sg.Window(f'Barcode Auto - {PROJECT_VERSION}', layout, finalize=True, icon=main_icon,
                                     location=self.current_gui_setting['window_location'])

        # First Focus to first element
        el_name = self.scan_events[0]
        element = self.main_window[el_name]
        element.update(disabled=False)
        element.SetFocus(True)
        self.set_status(f'CHECKING "{el_name.replace("-", "")}"')

        # Add event 'Enter' on Keyboard or '\r\n' when using scanner
        for key in self.scan_events:
            self.main_window[key].bind('<Return>', '')

        focus_key = el_name
        return focus_key

    def run(self):
        focus_key = self.init_main_window()

        while True:
            event, values = self.main_window.read(2000)
            if event in [sg.WINDOW_CLOSED, 'Exit']:
                break
            elif event == sg.TIMEOUT_EVENT:
                self._current_gui_setting['window_location'] = list(self.main_window.CurrentLocation())
                self.save_gui_setting()
                # do it
                a = 5
            elif event == 'Open SKU File':
                config_path = sg.popup_get_file('Choose SKU file', file_types=(("SKU Files", "*.yaml"),))
                if config_path is not None:
                    self._current_gui_setting['sku_path'] = config_path
                    self.init_sku_config()
                    # Reload GUI
                    self.main_window.close()
                    focus_key = self.init_main_window()
            elif event == self.EVENT_SKU_LIST:
                print(f'Selected: {values[self.EVENT_SKU_LIST]}')
                # Reload GUI
                self.main_window.close()
                focus_key = self.init_main_window(values[self.EVENT_SKU_LIST])
            elif self.is_scan_event(event):
                print(f'scan event {event}')
                focus_val = values[event]
                focus_idx = self.scan_events.index(event)
                if focus_val != '':
                    if self.barcode_validation(focus_val, event, values):
                        try:
                            if focus_idx != -1:
                                self.main_window[event].update(disabled=True)  # Disable input
                                next_element = self.scan_events[focus_idx + 1]  # Focus and Enable next element
                                self.main_window[next_element].update(disabled=False)
                                self.main_window[next_element].SetFocus(True)
                                focus_key = next_element
                                self.set_status(f'CHECKING "{focus_key.replace("-", "")}"')
                        except:
                            print('End of scanning!')
                            for event in self.scan_events:
                                self.main_window[event].update('')
                            # First Focus to first element
                            el_name = self.scan_events[0]
                            element = self.main_window[el_name]
                            element.update(disabled=False)
                            element.SetFocus(True)
                            self.set_status(f'PASS - Next "{el_name.replace("-", "")}"', text_color='green')
                    else:
                        self.main_window[event].update('')
            elif event == 'About...':
                sg.popup('Barcode Auto Scan and Validation!', 'Usage: Choose SKU File -> Choose SKU -> Begin Scanning',
                         'Note: Choose SKU File: File->Open SKU File',
                         PROJECT_VERSION, title='About...', keep_on_top=True, image=main_icon, icon=main_icon)
            elif event == 'Scanner Configure':
                sg.popup_animated('document\\enable_auto_mode.png', title='Scanner Configure', no_titlebar=False, icon=main_icon)
            else:
                print(f'Event: {event}')
        print('Bye!')
        self.main_window.close()


if __name__ == '__main__':
    barcode_gui = BarcodeGUI()
    barcode_gui.run()
