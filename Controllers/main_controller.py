import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QApplication


class Application:
    def __init__(self):
        self.operation = {"plus": False, "sub": False, "mult": False, "div": False, "percent": False, "Result": False}
        self.args = []

        self.app = QApplication(sys.argv)
        self.form = uic.loadUi("../Views/main_calc.ui")

        # Buttons events
        self.form.btn_0.clicked.connect(self.btn_0_event_click)
        self.form.btn_1.clicked.connect(self.btn_1_event_click)
        self.form.btn_2.clicked.connect(self.btn_2_event_click)
        self.form.btn_3.clicked.connect(self.btn_3_event_click)
        self.form.btn_4.clicked.connect(self.btn_4_event_click)
        self.form.btn_5.clicked.connect(self.btn_5_event_click)
        self.form.btn_6.clicked.connect(self.btn_6_event_click)
        self.form.btn_7.clicked.connect(self.btn_7_event_click)
        self.form.btn_8.clicked.connect(self.btn_8_event_click)
        self.form.btn_9.clicked.connect(self.btn_9_event_click)
        self.form.btn_enter.clicked.connect(self.btn_enter_event_click)
        self.form.btn_plus.clicked.connect(self.btn_plus_event_click)
        self.form.btn_sub.clicked.connect(self.btn_sub_event_click)
        self.form.btn_mult.clicked.connect(self.btn_mult_event_click)
        self.form.btn_div.clicked.connect(self.btn_div_event_click)
        self.form.btn_comma.clicked.connect(self.btn_comma_event_click)
        self.form.btn_clear.clicked.connect(self.btn_clear_event_click)
        self.form.btn_clear_all.clicked.connect(self.btn_clear_all_event_click)
        self.form.btn_cancel_calc.clicked.connect(self.btn_cancel_calc_event_click)
        self.form.btn_percent.clicked.connect(self.btn_percent_event_click)

        self.form.show()
        sys.exit(self.app.exec_())

    def fill_lbl_calc(self, message):
        self.form.txt_show_calc.setText(self.form.txt_show_calc.text() + message)

    def btn_0_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("0")

    def btn_1_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("1")

    def btn_2_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("2")

    def btn_3_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("3")

    def btn_4_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("4")

    def btn_5_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("5")

    def btn_6_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("6")

    def btn_7_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("7")

    def btn_8_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("8")

    def btn_9_event_click(self):
        if self.operation["Result"] is True and self.operation["percent"] is False:
            self.args.clear()
            self.operation["Result"] = False
            self.form.txt_show_calc.clear()
        self.fill_lbl_calc("9")

    def btn_plus_event_click(self):
        if len(self.args) == 1:
            self.form.txt_show_calc.clear()
        else:
            self.args.append(float(str(self.form.txt_show_calc.text()).replace(",", ".")))
            self.form.txt_show_calc.clear()
        self.operation["Result"] = False
        self.operation["plus"] = True

    def btn_sub_event_click(self):
        if len(self.args) == 1:
            self.form.txt_show_calc.clear()
        else:
            self.args.append(float(str(self.form.txt_show_calc.text()).replace(",", ".")))
            self.form.txt_show_calc.clear()
        self.operation["Result"] = False
        self.operation["sub"] = True

    def btn_mult_event_click(self):
        if len(self.args) == 1:
            self.form.txt_show_calc.clear()
        else:
            self.args.append(float(str(self.form.txt_show_calc.text()).replace(",", ".")))
            self.form.txt_show_calc.clear()
        self.operation["Result"] = False
        self.operation["mult"] = True

    def btn_div_event_click(self):
        if len(self.args) == 1:
            self.form.txt_show_calc.clear()
        else:
            self.args.append(float(str(self.form.txt_show_calc.text()).replace(",", ".")))
            self.form.txt_show_calc.clear()
        self.operation["Result"] = False
        self.operation["div"] = True

    def btn_percent_event_click(self):
        self.form.txt_show_calc.clear()
        self.operation["percent"] = True

    def btn_comma_event_click(self):
        if str(self.form.txt_show_calc.text()).find(",") == -1:
            self.form.txt_show_calc.setText(self.form.txt_show_calc.text() + ",")

    def btn_clear_event_click(self):
        if len(str(self.form.txt_show_calc.text())) > 0:
            self.form.txt_show_calc.setText(str(self.form.txt_show_calc.text())[0:-1])

    def btn_clear_all_event_click(self):
        self.form.txt_show_calc.clear()

    def btn_cancel_calc_event_click(self):
        self.args.clear()
        self.operation["plus"] = False
        self.operation["sub"] = False
        self.operation["mult"] = False
        self.operation["div"] = False
        self.operation["percent"] = False
        self.operation["Result"] = False
        self.form.txt_show_calc.clear()

    def btn_enter_event_click(self):
        if len(self.args) == 1 and self.operation["percent"] is False:
            self.args.append(float(str(self.form.txt_show_calc.text()).replace(",", ".")))
        if self.operation["Result"] is True and self.operation["percent"] is True and len(str(self.form.txt_show_calc.text()).strip()) > 0:
            self.args[0] = self.args[0] * (float(str(self.form.txt_show_calc.text()).replace(",", ".")) / 100)
            self.form.txt_show_calc.setText(str(self.args[0]).replace(".", ","))
            self.operation["percent"] = False
        elif (self.operation["plus"] is True or self.operation["sub"] is True or self.operation["mult"] is True or self.operation["div"] is True) and self.operation["percent"] is True and len(str(self.form.txt_show_calc.text()).strip()) > 0:
            self.args.append(self.args[0] * (float(str(self.form.txt_show_calc.text()).replace(",", ".")) / 100))
            self.form.txt_show_calc.setText(str(self.args[1]).replace(".", ","))
            self.operation["percent"] = False
        if self.operation["plus"] is True and len(self.args) > 1:
            operacao = self.args[0] + self.args[1]
            self.args.clear()
            self.args.append(operacao)
            self.operation["Result"] = True
            self.operation["plus"] = False
            self.form.txt_show_calc.setText(str(operacao).replace(".", ","))
        elif self.operation["sub"] is True and len(self.args) > 1:
            operacao = self.args[0] - self.args[1]
            self.args.clear()
            self.args.append(operacao)
            self.operation["Result"] = True
            self.operation["sub"] = False
            self.form.txt_show_calc.setText(str(operacao).replace(".", ","))
        elif self.operation["mult"] is True and len(self.args) > 1:
            operacao = self.args[0] * self.args[1]
            self.args.clear()
            self.args.append(operacao)
            self.operation["Result"] = True
            self.operation["mult"] = False
            self.form.txt_show_calc.setText(str(operacao).replace(".", ","))
        elif self.operation["div"] is True and len(self.args) > 1:
            operacao = self.args[0] / self.args[1]
            self.args.clear()
            self.args.append(operacao)
            self.operation["Result"] = True
            self.operation["div"] = False
            self.form.txt_show_calc.setText(str(operacao).replace(".", ","))


if __name__ == '__main__':
    Application()
