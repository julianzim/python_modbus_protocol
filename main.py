import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp
from tkinter import *

SLAVE_IP = "192.168.0.1"
master = modbus_tcp.TcpMaster(host=SLAVE_IP, port=502)
master.set_timeout(1.0)

# out_DI = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10)
# out_DI = master.execute(1, cst.READ_INPUT_REGISTERS, 0, 10)
# out_DI = master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 10)

# print(out_DI)

window = Tk()
window.title("Modbus TCP")
window.geometry('500x300')

lbl = Label(window, text='Ответ:', font=('Arial Bold', 15))
lbl.grid(column=0, row=0)


window.mainloop()
