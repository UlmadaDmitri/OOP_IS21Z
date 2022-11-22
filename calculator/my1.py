from tkinter import *
import math


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.formula = "0"
        self.blocked = False
        self.memory = ""
        self.operand = ""
        self.saved = 0
        self.resulted = False
        self.error = False
        self.showSave = False
        self.sign = False
        self.lbl = Label(text=self.formula, font=("Candara Bold", 21, "bold"), bg="steelblue1", foreground="#FFF")
        self.build()

    def build(self):
        self.lbl.place(x=11, y=50)

        btns = [
            "M+", "M-", "Ms", "Mc", "DEL",
            "bin", "oct", "hex", "tg", "cos",
            "7", "8", "9", "sin", "sqrt",
            "4", "5", "6", "*", "/",
            "1", "2", "3", "+", "-",
            "X^2", "0", ".", "=", "C"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            # com = lambda x=bt: self.calculations(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 120
            if x > 500:
                x = 10
                y += 81

    def logicalc(self, operation):
        try:
            if operation == "C":
                self.formula = ""
                self.error = False
                self.blocked = False

            elif operation == "DEL":
                if self.error:
                    self.formula = ""
                    self.error = False
                elif self.blocked:
                    self.blocked = False
                else:
                    self.formula = self.formula[0:-1]

            elif operation == "+":
                if self.resulted:
                    self.blocked = False
                    self.memory = "0+"
                    self.formula = ""
                    self.resulted = False
                    self.update()
                elif self.blocked:
                    self.blocked = False
                    self.formula += "+"
                elif self.error:
                    self.formula = "0+"
                    self.error = False
                elif not self.find_symbol("+") and not self.sign:
                    self.formula += "+"
                    self.sign = True
                else:
                    self.formula += ""

            elif operation == "-":
                if self.resulted:
                    self.blocked = False
                    self.memory = "0-"
                    self.formula = ""
                    self.resulted = False
                    self.update()
                elif self.blocked:
                    self.blocked = False
                    self.formula += "-"
                elif self.error:
                    self.formula = "0-"
                    self.error = False
                elif not self.find_symbol("-") and not self.sign:
                    self.formula += "-"
                    self.sign = True
                else:
                    self.formula += ""

            elif operation == "*":
                if self.resulted:
                    self.blocked = False
                    self.memory = "0*"
                    self.formula = ""
                    self.resulted = False
                    self.update()
                elif self.blocked:
                    self.blocked = False
                    self.formula += "*"
                elif self.error:
                    self.formula = "0*"
                    self.error = False
                elif not self.find_symbol("*") and not self.sign:
                    self.formula += "*"
                    self.sign = True
                else:
                    self.formula += ""

            elif operation == "/":
                if self.resulted:
                    self.blocked = False
                    self.memory = "0/"
                    self.formula = ""
                    self.resulted = False
                    self.update()
                elif self.blocked:
                    self.blocked = False
                    self.formula += "/"
                elif self.error:
                    self.formula = "0/"
                    self.error = False
                elif not self.find_symbol("/") and not self.sign:
                    self.formula += "/"
                    self.sign = True
                else:
                    self.formula += ""

            elif operation == "X^2":
                self.formula = str((eval(self.formula))**2)
                self.blocked = True

            elif operation == ".":
                if self.resulted:
                    self.blocked = False
                    self.memory = "0."
                    self.formula = ""
                    self.resulted = False
                    self.update()
                elif self.blocked:
                    self.blocked = False
                    self.formula = "0."
                elif self.error:
                    self.formula = "0."
                    self.error = False
                else:
                    self.formula += "."

            elif operation == "bin":
                if not self.resulted:
                    self.formula = str(bin(int(self.formula)))[2:]
                    self.display(self.formula)
                    self.blocked = True
                    self.resulted = True
                else:
                    self.formula = ""

            elif operation == "oct":
                if not self.resulted:
                    self.formula = str(oct(int(self.formula)))[2:]
                    self.display(self.formula)
                    self.blocked = True
                    self.resulted = True
                else:
                    self.formula = ""

            elif operation == "hex":
                if not self.resulted:
                    self.formula = str(hex(int(self.formula)))[2:]
                    self.display(self.formula)
                    self.blocked = True
                    self.resulted = True
                else:
                    self.formula = ""

            elif operation == "sqrt":
                self.formula = str(math.sqrt(float(self.formula)))
                self.blocked = True
                self.resulted = True

            elif operation == "sin":
                self.formula = str(math.sin(float(self.formula)))
                self.blocked = True
                self.resulted = True

            elif operation == "cos":
                self.formula = str(math.cos(float(self.formula)))
                self.blocked = True
                self.resulted = True

            elif operation == "tg":
                self.formula = str(math.tan(float(self.formula)))
                self.blocked = True
                self.resulted = True

            elif operation == "M+":
                if not self.resulted:
                    self.saved += float(self.formula)

            elif operation == "M-":
                if not self.resulted:
                    self.saved -= float(self.formula)

            elif operation == "Ms":
                self.display(self.saved)
                self.blocked = True
                self.showSave = True

            elif operation == "Mc":
                self.saved = 0

            elif operation == "=":
                self.formula = str(eval(self.formula))
                self.display(self.formula)
                self.blocked = True
                self.sign = False

            else:
                if self.formula == "0":
                    self.formula = ""

                self.formula += operation

                if self.blocked:
                    self.reset(operation)

                self.error = False
                self.resulted = False

            self.update()
        except ZeroDivisionError:
            print("Zero division error")
            self.display("Zero division error")
            self.formula = ""
            self.error = True
        except:
            print("Smth went wrong")
            self.display("Error in formula")
            self.formula = ""
            self.error = True

    def display(self, result):
        print(result, "result")
        self.lbl.configure(text=result)

    def reset(self, op):
        self.blocked = False
        self.formula = ""
        self.memory = str(op)
        self.update()

    def find_symbol(self, symbol):
        # count = 0
        # for s in self.formula:
        #     if s == symbol:
        #         count += 1
        # print(count)
        return self.formula.find(symbol) > -1

    def update(self):
        if self.formula == "":
            if self.memory:
                self.formula = self.memory
                self.memory = ""
            else:
                self.formula = "0"
        if self.blocked:
            if self.showSave:
                self.display(self.saved)
                self.showSave = False
            else:
                self.display(self.formula)
        else:
            self.lbl.configure(text=self.formula)
        if len(self.formula) > 30:
            self.display("Too long formula")
            self.formula = ""
            self.error = True


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "steelblue1"
    root.geometry("630x630+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()