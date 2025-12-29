def order():
    chai_type="Masala"

    def order_update():
        nonlocal chai_type   #use to modify enclosing scop
        chai_type="ginger"

    order_update()
    print(f"first order :{chai_type} updated order: {chai_type}")  #modify the output

order()