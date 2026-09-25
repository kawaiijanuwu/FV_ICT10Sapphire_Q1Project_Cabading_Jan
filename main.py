from pyscript import display, document

# jan cabading

# receipt generator (from skills test)
def order(e):
    # prices (php)
    spanish_price = 130
    coldbrew_price = 110
    caramac_price = 125

    # checkbox status
    ordered_spanish = float(document.getElementById("spanish").checked)
    ordered_coldbrew = float(document.getElementById("coldbrew").checked)
    ordered_caramac = float(document.getElementById("caramac").checked)

    # calculate subtotal
    subtotal = (
        (spanish_price * ordered_spanish) + (coldbrew_price * ordered_coldbrew) + (caramac_price * ordered_caramac)
    )

    # 12%
    vat = subtotal * 0.12

    # total
    total = subtotal + vat

    # update currency
    document.getElementById("subtotal").innerText = f"₱{subtotal}"
    document.getElementById("vat").innerText = f"₱{vat}"
    document.getElementById("total").innerText = f"₱{total}"


#sku, code from the guide in classfeed
def generate_sku(e):
    # Clear the div content
    document.getElementById("div_id").innerHTML = " "

    category_var = document.getElementById("category").value
    productname_var = document.getElementById("pname").value
    stock_qty = document.getElementById("qty").value

    SKU_name = (
        category_var[:3].upper()
        + "-"
        + productname_var[:4].upper()
        + "-"
        + str(stock_qty)
    )

    display("SKU: ", SKU_name, target="div_id")