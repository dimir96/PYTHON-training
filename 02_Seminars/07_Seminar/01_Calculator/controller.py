import model
import view
import loger

def button_click():
    while True:
        value = view.get_data()
        model.init(value)
        result = model.math_do_it()
        view.view_data(result)
        data = [value, result]
        loger.calc_logger(data)